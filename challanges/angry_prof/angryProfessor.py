
import math
import os
import random
import re
import sys


def angry_professor(k, a):
    ''' Takes in k and a returns string '''
    arrived_on_time = 0
    for i in range(len(a)):
        if a[i] <= 0:
            arrived_on_time += 1
    if arrived_on_time >= k:
        return str('NO')
    else:
        return str('YES')
