from data_util import get_data
from scipy.optimize import curve_fit
from richards import richards
from statistic_help import rmse
import matplotlib.pyplot as plt
import numpy as np
import logging


GITHUB = 0
STACKOVERFLOW = 1
SOURCEFORGE = 2

files = [["Language, Source, Period, Parametros, RMSE"], ["Language, Source, Period, Parametros, RMSE"],
         ["Language, Source, Period, Parametros, RMSE"]]

languages = ["Assembly", "C", "CPP", "CSharp", "Dart", "Go", "Java", "JavaScript", "Julia", "ObjectiveC", "PHP",
             "Python", "R", "Ruby", "Rust", "Shell", "Swift"]
periods = ["week", "month"]

sources = [["projects", "programmers"], ["individuals", "posts"], ["analysis"]]
databases = {0: "github", 1: "stackoverflow"}

for language in languages:
    for period in periods:
        for i in range(len(databases)):
            for source in sources[i]:
                time, infected = get_data(databases[i] + "/" + source + "/", period, language)
                time = np.array(time)
                infected = np.array(infected)
                logging.basicConfig(filename='richards.log', filemode='w', level=logging.INFO)
                pars, pcov = curve_fit(richards, time, infected)
                error = rmse(infected, richards(time, *pars))
                files[i].append(str([language, source, period, pars, error]))


github = np.array(files[GITHUB])
stackoverflow = np.array(files[STACKOVERFLOW])
sourceforge = np.array(files[SOURCEFORGE])
np.savetxt("github.txt", github, fmt="%s")
np.savetxt("stackoverflow.txt", stackoverflow, fmt="%s")
np.savetxt("sourceforge.txt", sourceforge, fmt="%s")

'''
i = 50
print(richards(i, *pars))
print(richards(i, *pars2))
print(infected[i])
print(infecteds[i])
print(*pars2)
print(rmse(infected - richards(time, *pars)))
error = rmse(infected - richards(time, *pars))
plt.plot(time, infected, label="real data git")
plt.plot(times, infecteds, label="real data stack")
plt.plot(time, richards(time, *pars), label="curve_fit")
plt.plot(times, richards(times, *pars2), label="curve_fit_stack")
plt.errorbar(time, richards(time, *pars), error, label="desvio padrao")
plt.legend(loc='best')
plt.show()
'''
 