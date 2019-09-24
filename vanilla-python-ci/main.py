#!/usr/bin/env python
"""Two function out of which one is covered by unit tests"""

import numpy as np

def calc_square(arg1):
    r'''A simple function.

    Parameters
    ----------
    x : NumPy array
        Array input.

    Returns
    -------
    NumPy array
        The element-wise square.

    '''
    return np.power(arg1, 2)

def calc_square_root(arg1):
    r'''A second function that is not tested.'''
    return np.sqrt(arg1)
