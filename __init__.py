from main import App
import gi 
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

print("scoutviewer imported")

x = App()

for item in x.get_logger():
    print(item)
print(x.__dict__)
Gtk.main()