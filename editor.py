import gi
gi.require_version("Gtk", "3.0")
gi.require_version("GtkSource", "3.0")
from gi.repository import Gtk, GtkSource

win = Gtk.Window()
win.connect("delete-event", Gtk.main_quit)

grid = Gtk.Grid()

sourceview = GtkSource.View()
sourceview.set_show_line_numbers(True)
grid.attach(sourceview, 0, 0, 10, 10)
"""
label2 = Gtk.Label()
label2.set_markup("Label2")
grid.attach(label2, 1, 1, 2, 2)
"""
win.add(grid)
win.show_all()
Gtk.main()
