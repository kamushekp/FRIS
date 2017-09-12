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
    F = 0.2
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
        claster = sorted(zip(a, [ distanse_func(trueStolp, obj) for obj in a if obj is not trueStolp]), key = lambda x: x[1], reverse = True)
        claster = [elem[0] for elem in claster if (1 - elem[1] / (elem[1] + func(Find_nearest(b, elem[0]), elem[0]) ) > F) ]
        claster.insert(0, trueStolp)

        A.clasters.append(claster)
        A.unbounded = [elem for elem in a if elem not in claster]

    if (A.unbounded):
        A.clasters.append([A.unbounded.pop()])
        
    
   
    


A = Pattern([Point(1,2), Point(1,3), Point(2,4), Point(4,3), Point(3,3), Point(5, 4.01)])
B = Pattern([Point(4,3), Point(4,1), Point(5,4), Point(2,3)])
print(A)
print(B)
FRiS_Stolp(Euclid2, A, B)
FRiS_Stolp(Euclid2, B, A)
print(A)
print(B)