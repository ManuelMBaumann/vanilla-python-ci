import numpy as np

def calc_square(x):
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
    return np.power(x, 2)

def calc_square_root(x):
    return np.sqrt(x)
