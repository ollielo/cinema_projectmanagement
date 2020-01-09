import numpy

class channel:

    name = None
    type = "float" 
    data = None
    size = [0,0]

    def __init__(self, name):
        self.name = name

    def set_type(self, type):
        self.type = type

    def set_size(self, w, h):
        self.size = [w, h]
        self.create_test_data()

    def create_test_data(self):
        self.data = numpy.random.rand(self.size[0], self.size[1])

    def print(self):
        print("                {}".format(self.name))
        print("                    type: {}".format(self.type))

