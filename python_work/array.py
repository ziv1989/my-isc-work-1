#!/bin/env python

import numpy as np

def wind_mag(arr_u,arr_v):
    arr_u=np.array(arr_u)
    arr_v=np.array(arr_v)
    arr_mag=(arr_u*arr_u+arr_v*arr_v)**0.5
    boo=np.greater(arr_mag,0.1)
    mod_arr=np.where(boo,arr_mag,0.1)   
    return mod_arr