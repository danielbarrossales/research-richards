import math
import array
import pylab
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.optimize import least_squares
from statistic_help import calc_squared_r


def richards(t, k, r, tm, a):
    try:
        return [k / (1 + float(np.power(float((np.exp(-r * (ti - tm)))), float(1 / a*1.0)))) for ti in t]
    except TypeError:
        return k / (1 + np.power((np.exp(-r * (t - tm))), 1 / a))


def residues_calc(params, t, y):
    return[richards(t[i], *params) - y[i] for i in range(len(t))]


def residues_calc_min(params, t, y):
    return richards_min(t, params) - y


def richards_min(t, params):
    return params['k'] / (1 + np.power((np.exp(-params['r'] * (t - params['tm']))), 1 / params['a']))
