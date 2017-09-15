from FrisStolp import FrisStolp
from point import Point
from pattern import Pattern
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
np.random.seed(12345)

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
    
def normal_test():

    A = Pattern(Point.ManyPoints(np.random.normal(loc = 6, scale = 1, size = 50), np.random.normal(loc = 6, scale = 1, size = 50)))
    B = Pattern(Point.ManyPoints(np.random.normal(loc = 2, scale = 1, size = 50), np.random.normal(loc = 2, scale = 1, size = 50)))

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
        plt.plot([e.x for e in elem], [e.y for e in elem], colors[i % 6] + sign)
        i += 1

normal_test()



