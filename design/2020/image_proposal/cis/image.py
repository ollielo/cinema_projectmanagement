from . import layer

class image:
    name       = None
    parameters = {}
    layers     = {} 

    def __init__(self, name):
        self.name = name

    def set_parameter(self, name, value):
        self.parameters[name] = value

    def print(self):
        print("    {}/".format(self.name))
        print("        parameter/")
        for p in self.parameters:
            print("            {}: {}".format(p, self.parameters[p]))

        print("        layer/")
        for l in self.layers:
            self.layers[l].print()

    def add_layer(self, name):
        self.layers[name] = layer.layer(name)

        return self.layers[name]

