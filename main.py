from data_util import get_data
from scipy.optimize import curve_fit
from richards import richards
from richards import residues_calc
from statistic_help import calc_squared_r
import numpy as np
import matplotlib.pyplot as plt

time, infected = get_data()
time = np.array(time)
infected = np.array(infected)

times, infecteds = get_data(source="stackoverflow/individuals/")
times = np.array(times)
infecteds = np.array(infecteds)

pars, pcov = curve_fit(richards, time[0:76], infected[0:76])
pars2, pcov2 = curve_fit(richards, times[0:76], infecteds[0:76], p0=pars)

print("Squared R of fit from git= " + str(calc_squared_r(residues_calc(pars, time, infected), infected)))
print("Squared R of fit from stack= " + str(calc_squared_r(residues_calc(pars2, times, infecteds), infecteds)))

i = 50
print(richards(i, *pars))
print(richards(i, *pars2))
print(infected[i])
print(infecteds[i])

plt.plot(time, infected, label="real data git")
plt.plot(times, infecteds, label="real data stack")
plt.plot(time, richards(time, *pars), label="curve_fit")
plt.plot(times, richards(times, *pars2), label="curve_fit_stack")
plt.legend(loc='best')
plt.show()
