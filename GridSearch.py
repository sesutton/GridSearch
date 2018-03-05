#coding: utf-8
import socket
#import spynnaker8 as p
from pyNN.random import NumpyRNG, RandomDistribution
import datetime
import argparse
import numpy as np
plot_figs = False 


# === Define parameters ===
def run_script(p, options):
    
    Gexc = options.Gexc
    Ginh = options.Ginh
    pconn = options.pconn
    n = options.n
    tstop = options.tstop
   

    rngseed = 98766987
    parallel_safe = True

    r_ei = 4.0        # number of excitatory cells:number of inhibitory cells

    rconn = 0.01
    stim_dur = 50.    # (ms) duration of random stimulation
    rate = 100.       # (Hz) frequency of the random stimulation

    dt = 1.0          # (ms) simulation timestep
    delay = 2

# Cell parameters
    area = 20000.     # (µm²)
    tau_m = 20.       # (ms)
    cm = 1.           # (µF/cm²)
    g_leak = 5e-5     # (S/cm²)

    E_leak = -60.     # (mV)
    v_thresh = -50.   # (mV)
    v_reset = -60.    # (mV)
    t_refrac = 5.     # (ms) (clamped at v_reset)
    v_mean = -60.     # (mV) mean membrane potential, for calculating CUBA weights
    tau_exc = 5.      # (ms)
    tau_inh = 10.     # (ms)

# Synapse parameters
    Erev_exc = 0.     # (mV)
    Erev_inh = -80.   # (mV)

# === Calculate derived parameters ===
    area = area * 1e-8                     # convert to cm²
    cm = cm * area * 1000                  # convert to nF
    Rm = 1e-6 / (g_leak * area)            # membrane resistance in MΩ
    assert tau_m == cm * Rm                # just to check

    n_exc = int(round((n * r_ei / (1 + r_ei))))  # number of excitatory cells
    n_inh = n - n_exc                            # number of inhibitory cells

    celltype = p.IF_cond_exp
    w_exc = Gexc * 1e-3              # We convert conductances to uS
    w_inh = Ginh * 1e-3

    print w_exc, w_inh


    node_id = p.setup(
    timestep=dt, min_delay=delay, max_delay=delay,
    db_name='va_benchmark.sqlite')

    p.set_number_of_neurons_per_core(p.IF_cond_exp, 50)      # this will set

    host_name = socket.gethostname()
    print "Host #%d is on %s" % (1, host_name)

    cell_params = {'tau_m': tau_m,
               'tau_syn_E': tau_exc,
               'tau_syn_I': tau_inh,
               'v_rest': E_leak,
               'v_reset': v_reset,
               'v_thresh': v_thresh,
               'cm': cm,
               'tau_refrac': t_refrac,
               'i_offset': 0,
               'e_rev_E':Erev_exc,
               'e_rev_I':Erev_inh
               }

    print cell_params

    pops = []

    print "%s Creating cell populations..." % node_id
    exc_cells = p.Population(n_exc, celltype(**cell_params), label="Excitatory_Cells")
    inh_cells = p.Population(n_inh, celltype(**cell_params), label="Inhibitory_Cells")

    ext_stim = p.Population(20, p.SpikeSourcePoisson(rate=rate, duration=stim_dur), label="expoisson")

    print "%s Initialising membrane potential to random values..." % node_id
    rng = NumpyRNG(seed=rngseed, parallel_safe=parallel_safe)
    uniformDistr = RandomDistribution('uniform', [v_reset, v_thresh], rng=rng)
    exc_cells.set(v=uniformDistr)
    inh_cells.set(v=uniformDistr)

    pops.append(exc_cells)
    pops.append(inh_cells)

    pops.append(ext_stim)

    print "%s Connecting populations..." % node_id
    exc_conn = p.FixedProbabilityConnector(pconn, rng=rng)
    inh_conn = p.FixedProbabilityConnector(pconn, rng=rng)
    ext_conn = p.FixedProbabilityConnector(rconn)

    connections = {
    'e2i': p.Projection(
        exc_cells, inh_cells, exc_conn, receptor_type='excitatory',
        synapse_type=p.StaticSynapse(weight=w_exc, delay=delay)),
    'i2e': p.Projection(
        inh_cells, exc_cells, inh_conn, receptor_type='inhibitory',
        synapse_type=p.StaticSynapse(weight=w_inh, delay=delay)),
    'ext2e': p.Projection(
        ext_stim, exc_cells, ext_conn, receptor_type='excitatory',
        synapse_type=p.StaticSynapse(weight=0.1)),
    'ext2i': p.Projection(
        ext_stim, inh_cells, ext_conn, receptor_type='excitatory',
        synapse_type=p.StaticSynapse(weight=0.1))
    }

    print "%s Setting up recording..." % node_id

    for pop in pops:
        pop.record("spikes")

# === Run simulation ===
    print "%d Running simulation..." % node_id

    print "timings: number of neurons:", n
    print "timings: number of synapses:", n * n * pconn

    p.run(tstop)


    pop_labels = ['exc', 'inh', 'ext']
    pop_spikes = []
    for i in range(len(pops)):
        pop_spikes.append(pops[i].get_data("spikes"))

# === Finished with simulator ===

    p.end()

# === Post Processing ===


    stw = SpikeTrainWriter()
    
    for i in range(len(pop_spikes)):
        filename = "Pop: " + pop_labels[i] + ' '
        filename += "Gexc: " + str(Gexc) + ' '
        filename += "Ginh: " + str(Ginh) + ' '
        filename += "Pconn: " + str(pconn) + ' '
        filename += "N: " + str(n)

        stw.write(pop_spikes[i], fname=filename,
                  fname_time=False)


class SpikeTrainProcessor():
    def Process(self, data):
        spiketrains = data.segments[0].spiketrains

        neurons = np.concatenate(map(lambda x:np.repeat(x.annotations['source_index'], len(x)), spiketrains))
        spike_times = np.concatenate(spiketrains, axis=0)
        
        return neurons, spike_times

class SpikeTrainWriter():
    
    def __init__(self):
        import os
        self.results_dir = os.getcwd() + '/results/'
        if not os.path.exists(self.results_dir):
            os.makedirs(self.results_dir)
    
    def write(self, data, fname, fname_time=True):
        
        stp = SpikeTrainProcessor()
        neurons, spike_times = stp.Process(data)
        
        file_name = self.results_dir
        if fname == None:
            file_name += datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        else:
            if fname_time:
                file_name += datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file_name += fname
        file_name += '.csv'
        
        with open(file_name, 'w') as f:
            f.write('Time/ms,NeuronID\n')
            for i in range(neurons.shape[0]):
                line = '{},{}'.format(spike_times[i], neurons[i])
                f.write(line + '\n')



if __name__ == '__main__':
    from pyNN.utility import get_simulator
    Gexc = ("Gexc","Excitatory Conductance", {"action":"store", "type": float})
    Ginh = ("Ginh","Inhibitory Conductance", {"action":"store", "type": float})
    pconn = ("pconn", "Probability of Connectivity", {"action":"store", "type":
                                                      float})
    n = ("n", "Number of Neurons", {"action":"store", "type":int})
    tstop = ("tstop", "Length of Sim", {"action":"store", "type":int})

    p, options = get_simulator(Gexc, Ginh, pconn, n, tstop)

    run_script(p, options)
