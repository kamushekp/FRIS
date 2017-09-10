import numpy as np
import sys
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Point ( " + str(self.x) + " : " + str(self.y) + " )"

    def __str__(self):
        return "Point ( " + str(self.x) + " : " + str(self.y) + " )"

def Euclid2(obj1, obj2):
    return ( (obj1.x - obj2.x)**2 + (obj1.y - obj2.y)**2 )**0.5

def Find_nearest(Set, obj):
    min = sys.float_info.max
    for elem in Set:
        if elem is not obj:
            ro = Euclid2(elem, obj)
            if ro < min:
                min = ro
                minObj = elem
    return minObj

def FRiS_Stolp(distanse_func, *args):
    func = distanse_func
    F = 0
    A = args[0]
    B = args[1]

    D = [0] * len(A)
    T = [0] * len(A)
    for i in range(0, len(A)):
        stolpA = A[i]

        for object in A:
            if object is not stolpA:
                r1 = func(stolpA, object)
                r2 = func( Find_nearest(B, object), object )
                Fj = 1 - r1 / (r1 + r2)
                if  Fj > F:
                    D[i] += Fj

        for object in B:
            r2 = func(stolpA, object)
            r1 = func ( Find_nearest(B, object), object )
            Fj = 1 - r1 / (r1 + r2)
            if Fj > F:
                T[i] += Fj

    print(D)
    print(T)


A = [Point(1,2), Point(1,3), Point(2,4)]
B = [Point(4,3), Point(4,1), Point(5,4), Point(2,3)]
FRiS_Stolp(Euclid2, A, B)    