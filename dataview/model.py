import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class Model(Gtk.ListStore):

    def __init__(self):
        super(Model, self).__init__(str, str)
        self.append(["Example", "Example"])
        self.append(["Example", "Example"])
        self.append(["Example", "Example"])
        self.append(["Example", "Example"])
        self.columns = ["ExampleProperty", "ExampleProperty2"]
