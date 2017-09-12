import numpy as np
import sys
from point import Point
from pattern import Pattern

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

def similarity(searchableSet, comparativeSet, possibleStolp, F, func):
        """
        если searchableSet и comparativeSet разные, значит
        мы ищем обороноспособность объекта possibleStolp для объектов
        из searchableSet по отношению к объектам другого образа - comparativeSet

        если searchableSet = comparativeSet = B: одинаковые, значит мы оцениваем
        непохожесть объектов из B на столп possibleStolp из другого образа.

        F - параметр для сравнения
        func - функция расстояния
        """
        property = 0    #сходство aj с ai в конкуренции с bj
                        #или несходство bi c ai по сравнению с bj

        for object in searchableSet:
            if object is not possibleStolp:
                r1 = func(possibleStolp, object)
                r2 = func( Find_nearest(comparativeSet, object), object )

                if searchableSet is comparativeSet:
                    Fj = 1 - r2 / (r1 + r2)
                else:
                    Fj = 1 - r1 / (r1 + r2)

                if  Fj > F:
                    property += Fj

        return property

def FRiS_Stolp(distanse_func, A, B):
    func = distanse_func
    F = 0.5
    while( len(A.unbounded) > 1):
        a = A.unbounded
        b = B.objects()

        defensive = [0] * len(a)
        tolerance = [0] * len(a)


        for i in range(0, len(a)):
            possibleStolp = a[i]
            defensive[i] = similarity(a, b, possibleStolp, F, func)
            tolerance[i] = similarity(b, b, possibleStolp, F, func)

        s = [ (tt + dt) / 2 for (tt, dt) in zip(tolerance, defensive)]
        """
        Выберем столп и сформируем вокруг него кластер (столп - нулевой элемент)
        """
        trueStolp = sorted(zip(s, a), key = lambda x: -x[0])[0][1]
        claster = list(zip(a, [ distanse_func(trueStolp, obj) for obj in a if obj is not trueStolp]))
        claster = [elem[0] for elem in claster if (1 - elem[1] / (elem[1] + func(Find_nearest(b, elem[0]), elem[0]) ) > F) ]
        claster.insert(0, trueStolp)

        A.clasters.append(claster)
        A.unbounded = [elem for elem in a if elem not in claster]

    if (A.unbounded):
        A.clasters.append([A.unbounded.pop()])
        
    
import matplotlib.pyplot as plt
import matplotlib.colors as colors
np.random.seed(12345)
    
def normal_test():

    A = Pattern(Point.ManyPoints(np.random.normal(loc = 6, scale = 1, size = 50), np.random.normal(loc = 6, scale = 1, size = 50)))
    B = Pattern(Point.ManyPoints(np.random.normal(loc = 2, scale = 1, size = 50), np.random.normal(loc = 2, scale = 1, size = 50)))

    FRiS_Stolp(Euclid2, A, B)
    FRiS_Stolp(Euclid2, B, A)

    PrintPattern(A, "s")
    PrintPattern(B, "^")
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
    FRiS_Stolp(Euclid2, A, B)
    FRiS_Stolp(Euclid2, B, A)

    PrintPattern(A, "s")
    PrintPattern(B, "^")
    plt.show()

def PrintPattern(pattern, sign):
    colors = "bgcmyk"
    i = 0
    for elem in pattern.clasters:
        stolp = elem[0]
        plt.plot(stolp.x, stolp.y, "r" + sign, ms = 7.0)
        plt.plot([e.x for e in elem if elem is not stolp], [e.y for e in elem if elem is not stolp], colors[i] + sign)
        i += 1



unif_test()


