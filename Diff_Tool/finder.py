



def fileObjectLocator(self,temp_type, temp_fileN):
    root = self.getPath()
    my_return = os.walk(root)

    for item in my_return:
        for filename in item[temp_type]:
            if filename == temp_fileN:
                location = (os.path.join(item[0], filename))
                return location