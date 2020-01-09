import h5py

class writer:

    def write(self, CISimage):
        with h5py.File(CISimage.fname, "w") as f:
            f.attrs["class"]    = CISimage.classname
            f.attrs["size"]     = CISimage.size
            f.attrs["version"]  = CISimage.version
            f.attrs["flags"]    = CISimage.flags

            parameters = f.create_group("parameterlist")
            for p in CISimage.parameterlist:
                parameters.attrs[p[0]] = p[1]

            images = f.create_group("image")

            for i in CISimage.images:
                image = images.create_group(i)
