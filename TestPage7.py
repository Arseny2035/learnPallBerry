import numpy as np

def sum_of_intervals(intervals):
    s = set()
    for int in intervals:
        next = set(range(int[0],int[1]+1))
        print(next)
        s |= next
    return len(s)

print(sum_of_intervals([(1, 4), (7, 10), (3, 5)]))