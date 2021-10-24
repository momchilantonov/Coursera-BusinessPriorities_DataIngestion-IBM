def matrix_multiplication(A, B):
    '''
    INPUT: LIST (of length n) OF LIST (of length n) OF INTEGERS
    LIST (of length n) OF LIST (of length n) OF INTEGERS
    OUTPUT: LIST OF LIST OF INTEGERS
    (storing the product of a matrix multiplication operation)
    Return the matrix which is the product of matrix A and matrix B
    where A and B will be (a) integer valued (b) square matrices
    (c) of size n-by-n (d) encoded as lists of lists, e.g.
    A = [[2, 3, 4], [6, 4, 2], [-1, 2, 0]] corresponds to the matrix
    | 2 3 4 |
    | 6 4 2 |
    |-1 2 0 |
    You may not use numpy. Write your solution in straight python
    '''

    r = []
    m = []
    for i in range(len(A)):
        for j in range(len(B[0])):
            sums = 0
            for k in range(len(B)):
                sums = sums+(A[i][k] * B[k][j])
            r.append(sums)
        m.append(r)
        r = []
    return m


print(matrix_multiplication([[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]))
