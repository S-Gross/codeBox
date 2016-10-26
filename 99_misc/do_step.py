# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 11:52:32 2015

@author: sgr
mo"""

import os as O
import numpy as N
import pylab as p

from pyfmi import load_fmu

curr_dir = O.path.dirname(O.path.abspath(__file__));
path_to_fmus = O.path.join(curr_dir, 'FMUs')

    
fmu_name = O.path.join(path_to_fmus, 'Building_45.fmu')


# Generate input
t = N.linspace(0.,10.,100)
u = N.cos(t)
u_traj = N.transpose(N.vstack((t, u)))

# Create input object
input_object = ('u', u_traj)

# Load the dynamic library and XML data
model = load_fmu(fmu_name)

bla = type(model)
print(bla)


variable_alias = model.get_model_variables();
#print(variable_alias)

out = model.get_variable_valueref('add1.y')
res = model.get_real(out)
print(res)

mycurrent_t=0
mystep_size=1
model.do_step(mycurrent_t, mystep_size,True)


out = model.get_variable_valueref('add1.y')
res = model.get_real(out)
print(res)


# describtion = model.get_model_types_platform()
# print("Test")
# print(describtion)

print("Hier ist Schluss")

#
#
#
## Set the first input value to the model
#model.set('u', u[0])
#
## Simulate
#res = model.simulate(final_time=30, input=input_object, options={'ncp':3000})
#
#x1_sim = res['x1']
#x2_sim = res['x2']
#u_sim = res['u']
#time_sim = res['time']
#
#assert N.abs(res.final('x1')*1.e1 - (-8.3999640)) < 1e-3
#assert N.abs(res.final('x2')*1.e1 - (-5.0691179)) < 1e-3
#assert N.abs(res.final('u')*1.e1 - (-8.3907153)) < 1e-3
#
#if with_plots:
#    fig = p.figure()
#    p.subplot(2, 1, 1)
#    p.plot(time_sim, x1_sim, time_sim, x2_sim)
#    p.subplot(2, 1, 2)
#    p.plot(time_sim, u_sim, 'x-', t, u[:], 'x-')
#    p.show()
#
