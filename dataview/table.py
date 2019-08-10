import gi 
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class Table(Gtk.TreeView):

    def __init__(self, model):
        super(Table, self).__init__(model)
        cols = model.columns
        self.add_text_columns(cols)

    def add_text_columns(self, names):
        renderer = Gtk.CellRendererText()
        for name in names:
            column = Gtk.TreeViewColumn(name, renderer, text=0)
            self.append_column(column)