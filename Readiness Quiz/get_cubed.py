def get_cubed(lst):
    '''
    INPUT: LIST (containing numeric elements)
    OUTPUT: LIST (cubed value of each even number in originals list)
    return a list containing each element cubed
    '''
    return [i ** 3 for i in lst]


print(get_cubed([1, 2, 3, 4]))
