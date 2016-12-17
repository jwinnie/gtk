import gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk as gtk
import os

class theme(gtk.Button):
    name = "Theme"
    description = "Description not available."
    def draw(self):
        self.main_container = gtk.Box(orientation=gtk.Orientation.VERTICAL)
        self.add(self.main_container)
        self.title_label = gtk.Label("<b>" + self.name + "</b>")
        self.title_label.set_use_markup(True)
        self.main_container.add(self.title_label)
        self.add(self.main_container)
        
a = theme()
a.name = "Hello"
a.description = "World"
a.draw()
print(a)

# New window
main_window = gtk.Window()
main_window.set_default_size(800,800)
main_window.connect('delete-event', gtk.main_quit)
main_window.set_border_width(10)
main_window.set_title("GTK Theme Switcher")

# List of themes container
main_container = gtk.Box()
main_container.set_orientation(gtk.Orientation.VERTICAL)
main_container.set_spacing(10)

def change_theme(button):
    print("User clicked theme " + button._theme_name)

    return os.system("gsettings set org.gnome.desktop.interface gtk-theme '{}'".format(button._theme_name))

for theme_name in os.listdir("/usr/share/themes"):
    print("Found theme " + theme_name)
    theme_button = gtk.Button(label="{}".format(theme_name))
    theme_button._theme_name = theme_name
    theme_button.connect("clicked",change_theme)
    main_container.add(theme_button)

main_window.add(main_container)
main_window.add(a)
main_window.show_all()
gtk.main()
