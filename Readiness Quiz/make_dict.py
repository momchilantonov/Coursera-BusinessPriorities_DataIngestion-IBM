def make_dict(lst1, lst2):
    '''
    INPUT: LST1, LST2
    OUTPUT: DICT (LST 1 are the keys and LST2 are the values)
    Given equal length lists create a dictionary where the first list is the keys
    '''
    return dict(zip(lst1, lst2))


print(make_dict(['a', 'b', 'c'], [1, 2, 3]))
