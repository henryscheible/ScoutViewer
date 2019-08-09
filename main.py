import gtk
from scoutviewer.dataview import Dataview

class App(gtk.Window):

    def __init__(self):
        super(App, self).__init__()
        self.set_title("ScoutViewer")
        
        self.notebook = gtk.Notebook()
        self.notebook.set_tab_pos(gtk.POS_BOTTOM)
        
        views = [Dataview]
        for view in views:
            self.add_view(view)
            
        self.add(notebook)
        self.show_all()

    def add_view(self, mainclass):
        widget = mainclass()
        self.notebook.append_page(widget)