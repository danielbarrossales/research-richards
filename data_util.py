import numpy as np


def get_data(programming_language="CSharp", period="month", root_folder="/shared/phd-data/",
             source="github/programmers/"):
    """
    :return: return a 2 dimensional array with the content of
    {root_folder+source+period+"/"+programming_language+"_"period+".dat"} file
    """
    data_path = str(root_folder+source+period+"/"+programming_language+"_"+period+".dat")
    data = open(data_path, "r")
    data_x = []
    data_y = []

    while data is not None:
        line = data.readline().split()
        if len(line) == 2:
            data_x.append(int(line[0]))
            data_y.append(int(line[1]))
        else:
            break

    return [data_x, data_y]
