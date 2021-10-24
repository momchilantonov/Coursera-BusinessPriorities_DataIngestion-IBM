import numpy as np


def calculate_l1_norm(v):
    '''
    INPUT: LIST or ARRAY (containing numeric elements)
    OUTPUT: FLOAT (L1 norm of v)
    calculate and return a norm for a given vector
    '''
    # return np.linalg.norm(v)
    return sum(abs(i) for i in v)


print(calculate_l1_norm([2.0, -3.5, 5.1]))
