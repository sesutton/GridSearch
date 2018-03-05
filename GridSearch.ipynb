{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "Collab Stuff"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false,
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "!pip install -U hbp_neuromorphic_platform"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "username = ''\n",
    "password = ''"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "import nmpi\n",
    "client = nmpi.Client(username, password)\n",
    "print(client.my_collabs().keys())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "aistate_collab_id = client.my_collabs()['UH AI state']['id']"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Original"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "Gexc = 4.\n",
    "Ginh = 51.\n",
    "pconn = 0.02\n",
    "n = 1500\n",
    "tstop = 60 * 1000\n",
    "\n",
    "command = \"GridSearch.py {system} %s %s %s %s %s \" % (Gexc, Ginh, pconn, n, tstop)\n",
    "print command"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "job_path = client.submit_job(source=\"https://github.com/sesutton/GridSearch\",\n",
    "                              platform=nmpi.SPINNAKER,\n",
    "                              collab_id=aistate_collab_id,\n",
    "                              command=command)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Pooled Version"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "def pooled_grid_search(command):  \n",
    "    job_path = client.submit_job(source=\"https://github.com/sesutton/GridSearch\",\n",
    "                              platform=nmpi.SPINNAKER,\n",
    "                              collab_id=aistate_collab_id,\n",
    "                              command=command) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "commands = []\n",
    "for Gexc in range(1,101, 4):\n",
    "    for Ginh in range(1,101, 4):\n",
    "        pconn = 0.02\n",
    "        n = 1500\n",
    "        tstop = 60 * 1000\n",
    "        commands.append(\"GridSearch.py {system} %s %s %s %s %s \" % (Gexc, Ginh, pconn, n, tstop))\n",
    "\n",
    "print len(commands)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "import multiprocessing\n",
    "p = multiprocessing.Pool()\n",
    "p.map(pooled_grid_search, commands)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "job_id = 100430 - 625 + 1\n",
    "ret = client.get_job(job_id, with_log=True)\n",
    "result = client.job_status(job_id)\n",
    "print result\n",
    "\n",
    "ret = client.get_job(job_id, with_log=True)\n",
    "print ret\n",
    "#filenames = client.download_data(ret, local_dir=sim_dir)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Serial Version"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "def Grid_Search(Gexc, Ginh, pconn, n, tstop):\n",
    "    command = \"GridSearch.py {system} %s %s %s %s %s \" % (Gexc, Ginh, pconn, n, tstop)\n",
    "    print command\n",
    "    \n",
    "    job_path = client.submit_job(source=\"https://github.com/sesutton/GridSearch\",\n",
    "                              platform=nmpi.SPINNAKER,\n",
    "                              collab_id=aistate_collab_id,\n",
    "                              command=command)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "for Gexc in range(1,101):\n",
    "    for Ginh in range(1,101):\n",
    "            pconn = 0.02\n",
    "            n = 1500\n",
    "            tstop = 60 * 1000\n",
    "            Grid_Search(Gexc, Ginh, pconn, n, tstop)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Download results"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "import os\n",
    "\n",
    "results_dir = os.getcwd() + '/results/'\n",
    "if not os.path.exists(results_dir):\n",
    "    os.makedirs(results_dir)\n",
    "\n",
    "job_id = 0\n",
    "for Gexc in range(1,101):\n",
    "    for Ginh in range(1,101):\n",
    "        pconn = 0.02\n",
    "        n = 1500\n",
    "        tstop = 6 * 1000\n",
    "            \n",
    "        sim_dir = results_dir + \"/Gexc=%s Ginh=%s pconn=%s n=%s tstop=%s/\" % (Gexc, Ginh, pconn, n, tstop)\n",
    "        if not os.path.exists(sim_dir):\n",
    "            os.makedirs(sim_dir)\n",
    "            \n",
    "        ret = client.get_job(job_id, with_log=True)\n",
    "        filenames = client.download_data(ret, local_dir=sim_dir)\n",
    "        \n",
    "        job_id += 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "job_id = job_path.split('/')[-1]\n",
    "print job_id"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "# execute this line until it says 'finished'\n",
    "import time\n",
    "\n",
    "result = ''\n",
    "from IPython.display import clear_output\n",
    "while True:\n",
    "    try:\n",
    "        result = client.job_status(job_id)\n",
    "    except:\n",
    "        pass\n",
    "    clear_output()\n",
    "    print result\n",
    "    time.sleep(0.1)\n",
    "    if result == 'finished' or result == 'error':\n",
    "        break\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "ret = client.get_job(job_id, with_log=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "print(ret['log'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "import os\n",
    "\n",
    "results_dir = os.getcwd() + '/results/'\n",
    "if not os.path.exists(results_dir):\n",
    "    os.makedirs(results_dir)\n",
    "sim_dir = results_dir + \"/Gexc=%s Ginh=%s pconn=%s n=%s tstop=%s/\" % (Gexc, Ginh, pconn, n, tstop)\n",
    "if not os.path.exists(sim_dir):\n",
    "    os.makedirs(sim_dir)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "filenames = client.download_data(ret, local_dir=sim_dir)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Remove Jobs from Collab"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "def remove_comp_job(job_id):\n",
    "    try:\n",
    "        client.remove_completed_job(job_id)\n",
    "        print \"success %s\" % (job_id)\n",
    "    except:\n",
    "        failed.append(job_id)\n",
    "        print \"fail %s\" % (job_id)\n",
    "\n",
    "def remove_queued_job(job_id):\n",
    "    try:\n",
    "        client.remove_queued_job(job_id)\n",
    "        print \"success %s\" % (job_id)\n",
    "    except:\n",
    "        print \"fail %s\" % (job_id)\n",
    "      "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "failed = []\n",
    "first = 98455\n",
    "last = 98455\n",
    "\n",
    "import multiprocessing\n",
    "p = multiprocessing.Pool()\n",
    "p.map(remove_comp_job, range(first, last + 1))\n",
    "p.map(remove_queued_job, range(first, last + 1))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 2",
   "language": "python",
   "name": "python2"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 2
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython2",
   "version": "2.7.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
