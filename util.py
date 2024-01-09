"""
=======================================================================
Constants
=======================================================================
"""
import numpy as np
import astropy.constants as const

G = const.G.cgs.value
au = const.au.cgs.value
Msun = const.M_sun.cgs.value
Mjup = const.M_jup.cgs.value
Mearth = const.M_earth.cgs.value

pi = np.pi


"""
=======================================================================
Generate diagnostics / plots from data table
=======================================================================
"""
def func_example(data, **kwargs):
    # return number of planets
    n = len(data['m_p_mearth'])
    return n
def process_data(data, func=func_example, pass_counter=False, **kwargs):
    output = []
    i = 0
    for s in set(data['system']):
        I = data['system'] == s
        data1 = {}
        for k in data:
            data1[k] = data[k][I]
        i+=1
        if pass_counter:
            output1 = func(i, data1, **kwargs)
        else:
            output1 = func(data1, **kwargs)
        if output1 is not None:
            output.append(output1)
    return output