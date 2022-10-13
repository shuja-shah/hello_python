''' Takes in number of test cases and returns list of strings '''
def angry_professor(k, _a):
    ''' Takes in k and a returns string '''
    arrived_on_time = 0
    for i in enumerate(_a):
        if _a[i] <= 0:
            arrived_on_time += 1
    if arrived_on_time >= k:
        return str('NO')
    return str('YES')

angry_professor(3, [0, -3, 4, 2])
