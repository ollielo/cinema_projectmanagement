from . import image
from . import hdf5

class cis:

    fname         = None
    classname     = "COMPOSABLE_IMAGE_SET"
    size          = [0,0]
    version       = "1.0"
    flags         = "CONSTANT_CHANNELS"
    parameterlist = []
    images        = {} 

    def __init__(self, filename):
        self.fname = filename

    def print(self):
        print("fname:   {}".format(self.fname))
        print("class:   {}".format(self.classname))
        print("size:    {}".format(self.size))
        print("version: {}".format(self.version))
        print("flags:   {}".format(self.flags))

        print("parameterlist/")
        for i in self.parameterlist:
            print("    {}: {}".format(i[0], i[1]))

        print("image/")
        for i in self.images:
            self.get_image(i).print()

    def add_parameter(self, name, type):
        # check for duplicates
        self.parameterlist.append([name, type])

    def add_image(self, name):
        # check for duplicates
        self.images[name] = image.image(name)

    def get_image(self,name):
        image = None

        if name in self.images:
            image = self.images[name]

        return image

    def set_size(self, w, h):
        self.size = [w, h]
