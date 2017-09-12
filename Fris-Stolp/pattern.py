class Pattern():
    def __init__(self, elems):
        self.clasters = []
        self.unbounded = elems

    def __repr__(self):
        cl = ""
        for elem in self.clasters:
            cl+= "[ "
            for subElem in elem:
                cl += str(subElem) + " "
            cl += (" ]\n")
        return "\n\nclasters:\n" + cl + "\nnot in clasters: " + "".join([str(e) for e in self.unbounded])
        
    def __str__(self):
        cl = ""
        for elem in self.clasters:
            cl+= "[ "
            for subElem in elem:
                cl += str(subElem) + " "
            cl += (" ]\n")
        return "\n\nclasters:\n" + cl + "\nnot in clasters: " + "".join([str(e) for e in self.unbounded])

    def objects(self):
        objs = [e for sublist in self.clasters for e in sublist]
        objs.extend(self.unbounded)
        return objs




