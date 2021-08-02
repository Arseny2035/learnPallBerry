import math


def get_middle(s):
    print(s)
    print('math.floor(len(s)/2) = ', math.floor(len(s)/2))
    print('math.ceil(len(s)/2) = ', math.ceil(len(s)/2))
    return s[math.ceil(len(s)/2)-1:math.floor(len(s)/2)+1]



# your code here

print(get_middle("test"))
print(get_middle("testing"))
print(get_middle("middle"))
print(get_middle("A"))
print(get_middle("of"))
