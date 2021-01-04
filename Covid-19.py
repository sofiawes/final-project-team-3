# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 16:14:56 2020

@author: Sofia
"""

from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

# describe the model
def deriv(y, t, N, beta, gamma, delta):
    S, E, I, R = y
    dSdt = -beta * S * I / N
    dEdt = beta * S * I / N - delta * E 
    dIdt = delta * E - gamma * I
    dRdt = gamma * I
    return dSdt, dEdt, dIdt, dRdt




# describe the parameters
#N =  1113               # population
N = 10000000             #Sveriges befolkning
beta = 1    
delta = 1/5             #fem inkubationsdagar enligt https://www.folkhalsomyndigheten.se/smittskydd-beredskap/utbrott/aktuella-utbrott/covid-19/fragor-och-svar/      
gamma=1/7               #sju sjukdagar enligt https://www.folkhalsomyndigheten.se/smittskydd-beredskap/utbrott/aktuella-utbrott/covid-19/fragor-och-svar/  

# initial conditions: one infected, rest susceptible
S0 = N-1
E0 = 1
I0 = 0
R0 = 0



t = np.linspace(0, 119, 120) # Grid of time points (in days)
y0 = S0, E0, I0, R0 # Initial conditions vector


# Integrate the SIR equations over the time grid, t.
ret = odeint(deriv, y0, t, args=(N, beta, gamma, delta))
S, E, I, R = ret.T #delar upp resultatet i fyra separata delar




def plotsir(t, S, E, I, R):
  f, ax = plt.subplots(1,1,figsize=(10,4))
  ax.plot(t, S, 'b', alpha=0.7, linewidth=2, label='Susceptible')
  ax.plot(t, E, 'y', alpha=0.7, linewidth=2, label='Exposed')
  ax.plot(t, I, 'r', alpha=0.7, linewidth=2, label='Infected')
  ax.plot(t, R, 'g', alpha=0.7, linewidth=2, label='Recovered')

  ax.set_xlabel('Time (days)')

  ax.yaxis.set_tick_params(length=0)
  ax.xaxis.set_tick_params(length=0)
  ax.grid(b=True, which='major', c='w', lw=2, ls='-')
  legend = ax.legend()
  legend.get_frame().set_alpha(0.5)
  for spine in ('top', 'right', 'bottom', 'left'):
      ax.spines[spine].set_visible(False)
    
  # plt.savefig("Plot.png")  
  plt.show();
  
plotsir(t, S, E, I, R)
