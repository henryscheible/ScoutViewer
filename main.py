import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from dataview import Dataview

class App(Gtk.Window):

    def __init__(self):
        self.logger = []
        super(App, self).__init__()
        self.set_title("ScoutViewer")
        
        self.notebook = Gtk.Notebook()
        self.notebook.set_tab_pos(Gtk.POS_BOTTOM)
        self.logger.append("Adding Views...")
        self.add_view(Dataview)
        self.logger.append("Adding Notebook...")
        self.add(self.notebook)
        self.logger.append("Showing window...")
        self.show_all()

    def add_view(self, mainclass):
        widget = mainclass()
        self.logger.append(repr(mainclass))
        self.logger.append(repr(widget))
        self.logger.append(type(widget))
        self.notebook.append_page(widget)
    
    def get_logger(self):
        return self.logger