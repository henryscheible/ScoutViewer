import gtk

class Model(gtk.ListStore):

    def __init__(self):
        super(Model, self).__init__(str, str)
        self.append(["Henry", "Child"])
        self.append(["Jennifer", "Child"])
        self.append(["Sophie", "Child"])
        self.append(["Paul", "Child"])
        self.columns = ["Name", "Role"]