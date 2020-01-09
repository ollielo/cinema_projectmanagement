import h5py

class writer:

    def write(self, CISimage):
        with h5py.File(CISimage.fname, "w") as f:
            f.attrs["class"]    = CISimage.classname
            f.attrs["size"]     = CISimage.size
            f.attrs["version"]  = CISimage.version
            f.attrs["flags"]    = CISimage.flags

            variables = f.create_group("variablelist")
            for v in CISimage.variablelist:
                var = variables.create_group(v)
                values = CISimage.variablelist[v]
                var.attrs["type"] = values[0] 
                var.attrs["min"]  = values[1]
                var.attrs["max"]  = values[2]

            parameters = f.create_group("parameterlist")
            for p in CISimage.parameterlist:
                parameters.attrs[p[0]] = p[1]

            images = f.create_group("image")

            for i in CISimage.images:
                image = images.create_group(i)
