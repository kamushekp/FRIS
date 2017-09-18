class Pattern():
    """
    Паттерн, или образ - собранные в силу чего-либо в группу объекты.
    Для инициализации требуется список объектов, предположительно
    принадлежащих одному паттерну. Предлагается иметь отдельно 
    список кластеризованных объектов (например, FRiS функцией),
    и отдельно список некластеризованных. Так же, для получения
    просто списка всех объектов данного паттерна есть метод objects
    """
    def __init__(self, elems):
        self.clasters = []
        self.unbounded = elems

    def __repr__(self):
        clasterStr = ""
        for elem in self.clasters:
            clasterStr+= "[ "
            for subElem in elem:
                clasterStr += str(subElem) + " "
            clasterStr += (" ]\n")
        return "\n\nclasters:\n" + clasterStr + "\nnot in clasters: " + "".join([str(e) for e in self.unbounded])
        
    def __str__(self):
        
        clasterStr = ""
        for elem in self.clasters:
            clasterStr+= "[ "
            for subElem in elem:
                clasterStr += str(subElem) + " "
            clasterStr += (" ]\n")
        return "There are " + str(len(self.clasters)) + " different clasters:\n\nclasters:\n"\
           + clasterStr + "\nnot in clasters: " + "".join([str(e) for e in self.unbounded])

    def objects(self):
        objs = [e for sublist in self.clasters for e in sublist]
        objs.extend(self.unbounded)
        return objs




