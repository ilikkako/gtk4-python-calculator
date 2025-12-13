""" Basic calculator for GNOME. Programmed as a practice project."""

import sys
import gi
import window
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw, Gdk


class Application(Adw.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.connect('activate', self.on_activate)


    def on_activate(self, app):
        win = window.MainWindow(application=self)
        win.present()

        css_provider = Gtk.CssProvider()
        css_provider.load_from_path('stylesheet.css')

        display = Gdk.Display.get_default()
        Gtk.StyleContext.add_provider_for_display(display, css_provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)


if __name__ == '__main__':
    app = Application(application_id="com.github.ilkkako.gtk4-python-calculator")
    app.run(sys.argv)