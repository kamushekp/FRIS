from FrisStolp import FrisStolp
from point import Point
from pattern import Pattern
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors

def Euclid2(obj1, obj2):
    return ( (obj1.x - obj2.x)**2 + (obj1.y - obj2.y)**2 )**0.5

def trivial_test():
    A = Pattern(Point.ManyPoints([1, 1, 2],[1, 2, 1]))
    B = Pattern(Point.ManyPoints([1, 1, 2], [4, 5, 4]))
    FrisStolp(Euclid2, A, B)
    FrisStolp(Euclid2, B, A)
    PrintPattern(A, "s")
    PrintPattern(B, "^")
    print(A)
    print(B)
    plt.show()

def artificialClaster(centerX, centerY, scale, size):
    return Point.ManyPoints(np.random.normal(loc = centerX, scale = scale, size = size),\
       np.random.normal(loc = centerY, scale = scale, size = size))

def normal_test():

    A = Pattern(artificialClaster(1, 1, 1, 50))
    B = Pattern(artificialClaster(7, 7, 1, 50))

    FrisStolp(Euclid2, A, B)
    FrisStolp(Euclid2, B, A)

    PrintPattern(A, "s")
    PrintPattern(B, "^")
    print(A)
    print(B)
    plt.show()


def unif_test():
    B = Pattern(Point.ManyPoints(np.random.rand(25, 1), np.random.rand(25, 1)))
    x1 = list(5 + np.random.rand(25, 1))
    y1 = list(np.random.rand(25, 1))
    x2 = list(2 + np.random.rand(25, 1))
    y2 = list(2 + np.random.rand(25, 1))
    x3 = list(np.random.rand(25, 1))
    y3 = list(5 + np.random.rand(25, 1))

    temp = Point.ManyPoints(x1+x2+x3, y1+y2+y3)
    A = Pattern(temp)
    FrisStolp(Euclid2, A, B)
    FrisStolp(Euclid2, B, A)
    print(A)
    print(B)
    PrintPattern(A, "s")
    PrintPattern(B, "^")
    plt.show()

def PrintPattern(pattern, sign):
    colors = "bgcmyk"
    i = 0
    for elem in pattern.clasters:
        stolp = elem[0]
        plt.plot(stolp.x, stolp.y, "r" + sign, ms = 7.0)
        plt.plot([e.x for e in elem[1:]], [e.y for e in elem[1:]], colors[np.random.randint(6)] + sign)
        i += 1

np.random.seed(12346)
normal_test()

#import tensorflow as tf



