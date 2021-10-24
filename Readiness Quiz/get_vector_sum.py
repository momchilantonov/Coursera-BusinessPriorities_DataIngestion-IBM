import numpy as np


def get_vector_sum(vectorLower, vectorUpper):
    '''
    INPUT: vector lower and upper bounds
    OUTPUT: calculated value for vector sum
    (1) create a vector ranging from 1:150
    (2) transform the vector into a matrix with 10 rows and 15 columns
    (3) print the sum for the 10 rows

    '''
    vector = np.arange(vectorLower, vectorUpper)
    matrix = vector.reshape(10, 15)

    return [sum(v) for v in matrix]


print(get_vector_sum(1, 151))
