# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 11:52:32 2015

@author: sgr
mo"""

import os as O
import numpy as np
import sys
import matplotlib.pyplot as plt

from pyfmi import load_fmu

curr_dir = O.path.dirname(O.path.abspath(__file__));
path_to_fmus = O.path.join(curr_dir, 'FMUs')
fmu_name = O.path.join(path_to_fmus, 'AixLibLowOExample_cs20.fmu')

# Load the dynamic library and XML data
model = load_fmu(fmu_name)

# simulation steps
tStart = 0
tStop = 86400
hStep = 3600
t = np.arange(tStart, tStop, hStep)


model.setup_experiment(start_time=tStart, stop_time=tStop)
model.initialize()


#variable_alias = model.get_model_variables()

# container for all results
res_all = np.zeros(len(t))


# simulate in steps
for i in range(len(t)):
    # simulation step
    res = model.do_step(current_t=t[i], step_size=hStep, new_step=True)
    # get results and save in container
    res = model.get_real(3448)
    res_all[i] = res

plt.plot(res_all)
plt.show()
#print(res_all)
