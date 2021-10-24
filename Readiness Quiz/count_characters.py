def count_characters(string):
    '''
    INPUT: STRING
    OUTPUT: DICT (with counts of each character in input string)

    Return a dictionary of character counts
    '''
    s = [(string[i:i+1]) for i in range(len(string))]

    cnt = {}.fromkeys(s, 0)

    for c in s:
        cnt[c] = s.count(c)
    return cnt


print(count_characters('abbcccddddeeeeeffffffggggggghhhhhhhh'))
