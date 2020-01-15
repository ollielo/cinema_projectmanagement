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

            self.write_parameter_table(CISimage, f)


            images = f.create_group("image")
            for i in CISimage.images:
                image = images.create_group(i)

    def write_parameter_table(self, CISimage, h5file):
        if not CISimage.p_table is None:
            data = CISimage.p_table
            table = h5file.create_group("parametertable")
            table.attrs["columns"] = ','.join(data.columns)
            table.attrs["num_rows"] = data.shape[0]
            table.attrs["num_cols"] = data.shape[1]
            cols = table.create_group("columns")
            for col in data.columns:
                cols.create_dataset( col, data=data[col].values, 
                                     dtype=h5py.string_dtype(encoding='ascii') 
                                   )
                        
