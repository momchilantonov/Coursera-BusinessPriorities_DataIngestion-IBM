def get_squared_evens(lst):
    '''
    INPUT: LIST (containing numeric elements)
    OUTPUT: LIST (squared value of each even number in originals list)
    return squared evens in a list
    '''
    return [i ** 2 for i in lst if i % 2 == 0]


print(get_squared_evens([1, 2, 3, 4, 5, 6, 7]))
