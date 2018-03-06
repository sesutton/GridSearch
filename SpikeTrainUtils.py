import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.use('Agg')

class SpikeTrainProcessor():
    def Process(self, data):
        spiketrains = data.segments[0].spiketrains

        neurons = np.concatenate(map(lambda x:np.repeat(x.annotations['source_index'], len(x)), spiketrains))
        spike_times = np.concatenate(spiketrains, axis=0)
        
        return neurons, spike_times

class SpikeTrainWriter():
    
    def init(self):

        self.results_dir = os.getcwd() + '/results/'
        if not os.path.exists(results_dir):
            os.makedirs(results_dir)
    
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



class SpikeTrainPlotter():

    def init(self):

        self.results_dir = os.getcwd() + '/results/'
        if not os.path.exists(results_dir):
            os.makedirs(results_dir)
    
    def plot(self, data):
        stp = SpikeTrainProcessor()
        neurons, spike_times = stp.Process(data)

        plt.figure()
        f, ax = plt.subplots()

        ax.set_title('Spikes for Pop ' + pop_labels[i])  
        ax.plot(spike_times, neurons, ',', ms=0.1)
        ax.set_ylabel('Neuron id')
        ax.set_xlabel('Time/ms')

        plt.savefig(self.results_dir +
                  datetime.datetime.now().strftime("%Y-%m-%d%H:%M:%S") + ' ' +
                  pop_labels[i] + '.png')


class SpikeTrainReader():
    def read(self, fname):
        
        self.neurons = []
        self.spike_times = []
        with open(fname, 'rt') as f:
            header = True
            for line in f:
                if header:
                    header = False
                    continue
                cells = line.split(',')
                n_id = cells[1]
                t = cells[0].split(' ')[0]
                self.spike_times.append(float(t))
                self.neurons.append(float(n_id))
        return self.neurons, self.spike_times

class SpikeTrainStats():
    
    def get_data(self, fname):
        stre = SpikeTrainReader()
        neurons, spike_times = stre.read(fname)
        return neurons, spike_times

    def calculate(self, fname):
        self.data = []
        neurons, spike_times = self.get_data(fname)
        for i in range(len(neurons)):
            self.data.append([spike_times[i], neurons[i]])

        self.data = np.array(self.data) 
        self.min_time = np.amin(self.data[:,0])
        self.max_time = np.amax(self.data[:,0])
        
        ids, cnts = np.unique(self.data[:,1], return_counts=True)
        time_range = self.max_time - self.min_time
        t_r_seconds = time_range / 1000
       
        max_value = np.amax(cnts)
        min_value = np.amin(cnts)
        avg_value = np.average(cnts)
        
        firing_rate = self.calculate_FiringRate(cnts, t_r_seconds)
        CV_of_ISI = self.calculate_CVISI(ids, cnts)
        return firing_rate, CV_of_ISI, self.min_time, self.max_time
   
    def calculate_CVISI(self, ids, cnts):
        
        rows = np.where(cnts > 2)
         
        ids = ids[rows]
        
        isi = []
        for i in range(ids.shape[0]):
            data_rows = np.where(self.data[:,1] == ids[i])
            spikes = self.data[data_rows][:,0]
            diffs = np.diff(spikes)
            avg = np.average(diffs)
            stdev = np.std(diffs, dtype=np.float64)
            cv = stdev / avg
            isi.append(cv)
        isi = np.array(isi)
        avg_isi = np.average(isi)
        return avg_isi

    def calculate_FiringRate(self, cnts, t_r_seconds):
        firing_rates = cnts / t_r_seconds
        avg_firing_rate = np.average(firing_rates)
        return avg_firing_rate
    
  

