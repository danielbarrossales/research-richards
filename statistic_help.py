import numpy as np


def calc_squared_r(residues, real_result):
    ss_res = np.sum(np.power(residues, 2))
    ss_tot = np.sum(np.power(real_result - np.mean(real_result), 2))
    r_squared = 1 - (ss_res / ss_tot)
    return r_squared


def calc_std_deviation(real_data):
    mean = np.mean(real_data)
    value = 0
    for x in real_data:
        value += np.power(x - mean, 2)
    return np.sqrt(value/len(real_data))


def calc_error_margin(std_deviation, real_data):
    return std_deviation/np.sqrt(len(real_data))*2.56
