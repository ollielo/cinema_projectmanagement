from . import channel

class layer:


    def __init__(self, name):
        self.name     = name
        self.offset   = [0,0]
        self.size     = [0,0]
        self.channels = {}

    def set_offset(self, x, y):
        self.offset = [x, y]

    def set_size(self, w, h):
        self.size = [w, h]

    def add_channel(self, name):
        self.channels[name] = channel.channel(name)
        self.channels[name].set_size(self.size[0], self.size[1])

        return self.channels[name]

    def write_hdf5(self, layergroup):
        layer = layergroup.create_group(self.name)
        layer.attrs["offset"] = str(self.offset[0]) + "," + str(self.offset[1])
        layer.attrs["size"]   = str(self.size[0]) + "," + str(self.size[1])
        channelgroup = layer.create_group("channel")
        for c in self.channels:
            self.channels[c].write_hdf5(channelgroup)
    
