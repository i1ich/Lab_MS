import numpy as np

def Med(list):
    return float(sum(list)) / float(len(list))


def ingroup(llist):
    list2 = []
    res = 0
    for list in llist:
        M = Med(list)
        sum = 0
        for j in list:
            sum += (j - M)*(j - M)
        sum /= float(len(llist) - 1)
        res += sum

    return res * 1/float(len(llist))




def intergroup(llist):
    res = 0.0
    list = []
    for i in llist:
        sum = Med(i)
        list.append(sum)
    med = Med(list)
    sum = 0
    for j in list:
        sum += (j - med) * (j - med)
    sum /= float(len(llist) - 1)

    return sum * float(len(list))


def Fisher(llist):
    return float(intergroup(llist)) / float(ingroup(llist))