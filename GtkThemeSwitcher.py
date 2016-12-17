#!/usr/bin/env python3
import gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk as gtk
import os, subprocess

# New window
main_window = gtk.Window()
main_window.set_default_size(800,800)
main_window.connect('delete-event', gtk.main_quit)
main_window.set_border_width(10)
main_window.set_title("GTK Theme Switcher")

# Window container
main_container = gtk.Box()
main_container.set_orientation(gtk.Orientation.VERTICAL)
main_container.set_spacing(10)

# Themes container 
themes_container = gtk.Box()
themes_container.set_orientation(gtk.Orientation.VERTICAL)
themes_container.set_spacing(5)
scroll = gtk.ScrolledWindow(hexpand=True, vexpand=True)

# Current theme
def refresh():
    current_theme = subprocess.Popen(['gsettings','get','org.gnome.desktop.interface','gtk-theme'], stdout=subprocess.PIPE).communicate()[0].decode('UTF-8')
    current_theme_label.set_text("Current theme: " + current_theme)

# Add themes to scrollbar
def change_theme(button):
    print("User clicked theme " + button._theme_name)
    os.system("gsettings set org.gnome.desktop.interface gtk-theme '{}'".format(button._theme_name))
    refresh()

for theme_name in os.listdir("/usr/share/themes"):
    print("Found theme " + theme_name)
    theme_button = gtk.Button(label="{}".format(theme_name))
    theme_button._theme_name = theme_name
    theme_button.connect("clicked",change_theme)
    themes_container.add(theme_button)

scroll.add(themes_container)
main_container.add(scroll)

current_theme_label = gtk.Label("")
main_container.add(current_theme_label)

refresh()
main_window.add(main_container)

main_window.show_all()
gtk.main()
