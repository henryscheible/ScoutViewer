import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class Model(Gtk.ListStore):

    def __init__(self):
        super(Model, self).__init__(str, str)
        self.append(["Henry", "Child"])
        self.append(["Jennifer", "Child"])
        self.append(["Sophie", "Child"])
        self.append(["Paul", "Child"])
        self.columns = ["Name", "Role"]