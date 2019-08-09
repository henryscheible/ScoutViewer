import gtk

class Table(gtk.TreeView):

    def __init__(self, model):
        super(Table, self).__init__(model)
        cols = model.columns
        self.add_text_columns(cols)

    def add_text_columns(self, names):
        renderer = gtk.CellRendererText()
        for name in names:
            column = gtk.TreeViewColumn(name, renderer, text=0)
            self.append_column(column)