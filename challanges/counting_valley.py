''' Module for Counting Velly Func'''

def counting_valleys(steps, path):
    ''' Takes in a list of steps and returns an int'''
    if int(steps) != len(path):
        return
    valley= 0
    let = 0
    for item in path:
        if item == 'U':
            let +=1
        elif item == 'D':
            let -=1
        if let == 0:
            valley += 1
    result= +1 if valley % 2 == 0 else round(valley / 2)
    print(result)
