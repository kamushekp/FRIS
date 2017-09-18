import numpy as np
import sys
from point import Point
from pattern import Pattern

def Find_nearest(Set, obj, func):
    min = sys.float_info.max
    for elem in Set:
        if elem is not obj:
            ro = func(elem, obj)
            if ro < min:
                min = ro
                minObj = elem
    return minObj

def Border (r1, r2):
    return 1 - r1 / (r1 + r2)

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
                r2 = func( Find_nearest(comparativeSet, object, func), object )

                if searchableSet is comparativeSet:
                    r1, r2 = r2, r1

                Fj = Border(r1, r2)
                if  Fj > F:
                    property += Fj

        return property

def FrisStolp(distanse_func, A, B):
    func = distanse_func        #метрика между объектами
    F = 0.0
    while( len(A.unbounded) > 1):
        a = A.unbounded
        b = B.objects()

        defensive = [0] * len(a)
        tolerance = [0] * len(a)

        #рассмотрим каждый объект из А в качестве возможного столпа
        for i in range(0, len(a)):
            possibleStolp = a[i]
            defensive[i] = similarity(a, b, possibleStolp, F, func)
            tolerance[i] = similarity(b, b, possibleStolp, F, func)

        s = [ (tt + dt) / 2 for (tt, dt) in zip(tolerance, defensive)]
        """
        Выберем столп и сформируем вокруг него кластер (столп - нулевой элемент)
        """
        trueStolp = sorted(zip(s, a), key = lambda x: -x[0])[0][1]
        claster = list(zip(a, [ distanse_func(trueStolp, obj) for obj in a]))
        claster = [elem[0] for elem in claster if elem[0] is not trueStolp and Border(elem[1], func(Find_nearest(b, elem[0], func), elem[0])) > F ]
        claster.insert(0, trueStolp)

        A.clasters.append(claster)
        A.unbounded = [elem for elem in a if elem not in claster]

    if (A.unbounded):
        A.clasters.append([A.unbounded.pop()])