from . import layer

class image:

    def __init__(self, name):
        self.name   = name
        self.layers = {} 

    def add_layer(self, name):
        self.layers[name] = layer.layer(name)

        return self.layers[name]

    def write_hdf5(self, imagegroup):
        image = imagegroup.create_group(self.name)
        layergroup = image.create_group("layer")
        for l in self.layers:
            self.layers[l].write_hdf5(layergroup)


