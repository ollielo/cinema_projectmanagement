from . import channel

class layer:

    name = None 
    offset = [0,0]
    size = [0,0]
    parameters = {}
    channels = {}

    def __init__(self, name):
        self.name = name

    def set_parameter(self, name, value):
        self.parameters[name] = value

    def set_offset(self, x, y):
        self.offset = [x, y]

    def set_size(self, w, h):
        self.size = [w, h]

    def print(self):
        print("            {}/".format(self.name))
        print("                size:   {}".format(self.size))
        print("                offset: {}".format(self.offset))
        for p in self.parameters:
            print("                {}: {}".format(p, self.parameters[p]))
        print("            channel/")
        for c in self.channels:
            self.channels[c].print()

    def add_channel(self, name):
        self.channels[name] = channel.channel(name)
        self.channels[name].set_size(self.size[0], self.size[1])

        return self.channels[name]

    
