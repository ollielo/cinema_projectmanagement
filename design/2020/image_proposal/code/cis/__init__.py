from . import image

import h5py

class cis:

    def __init__(self, filename):
        self.fname         = filename
        self.classname     = "COMPOSABLE_IMAGE_SET"
        self.size          = [0,0]
        self.version       = "1.0"
        self.flags         = "CONSTANT_CHANNELS"
        self.parameterlist = []
        self.p_table       = None
        self.variablelist  = {} 
        self.images        = {} 


    def set_parameter_table(self, table):
        self.p_table = table.copy(deep=True)

    def add_parameter(self, name, type):
        # check for duplicates
        self.parameterlist.append([name, type])

    def add_variable(self, name, type, min, max):
        # check for duplicates
        self.variablelist[name] = [type, min, max]

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

    def read_hdf5(self, fname):
        self.fname = fname
        with h5py.File(fname, "r") as f:
            self.classname  = f.attrs["class"]
            self.size       = f.attrs["size"]
            self.version    = f.attrs["version"]
            self.flags      = f.attrs["flags"]
            for i in f["image"]:
                im = self.add_image(i)
                im.read_hdf5(f["image"][i])

    def write_hdf5(self):
        with h5py.File(self.fname, "w") as f:
            f.attrs["class"]    = self.classname
            f.attrs["size"]     = self.size
            f.attrs["version"]  = self.version
            f.attrs["flags"]    = self.flags

            vlist = f.create_group("variablelist")
            for v in self.variablelist:
                var = vlist.create_group(v)
                values = self.variablelist[v]
                var.attrs["type"] = values[0] 
                var.attrs["min"]  = values[1]
                var.attrs["max"]  = values[2]

            self.write_parameter_table(f)

            imagegroup = f.create_group("image")
            for i in self.images:
                self.get_image(i).write_hdf5(imagegroup)


    def write_parameter_table(self, h5file):
        if not self.p_table is None:
            data = self.p_table
            table = h5file.create_group("parametertable")
            table.attrs["columns"] = ','.join(data.columns)
            table.attrs["num_rows"] = data.shape[0]
            table.attrs["num_cols"] = data.shape[1]
            cols = table.create_group("columns")
            for col in data.columns:
                cols.create_dataset( col, data=data[col].values, 
                                     dtype=h5py.string_dtype(encoding='ascii') 
                                   )
