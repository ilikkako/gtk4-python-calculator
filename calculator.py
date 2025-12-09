""" Basic calculator for GNOME. Programmed as a practice project."""

import sys, gi, re
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw

# buttons = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, '.', '+', '-', '*', '/', '=', 'C', '(', ')', '<<<')
numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
operators = ('+', '-', 'x', '/')
others = ('=', 'C', '(', ')', '<<<', '.')
buttons = numbers + operators + others
screen = "" # Stores values in calculator screen
margin_all = 10
margin_buttons = 1
margin_frame = 5


@Gtk.Template(filename="calculator.ui")
class MainWindow(Gtk.ApplicationWindow):
    __gtype_name__ = "MainWindow"
    on_button_clicked = Gtk.Template.Child()
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    Gtk.Template.Callback()
    def on_button_clicked(self, widget):
        label = widget.get_label()
        print("Pressed:", label)
        


class AppCalculator(Adw.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.connect('activate', self.on_activate)


    def on_activate(self, app):
        # Create UI from XML file
        builder = Gtk.Builder()
        builder.add_from_file('calculator.ui')
        # builder.connect_signals(self)

        # Obtain and show main window 
        self.window = builder.get_object('main_window')
        self.window.set_application(self)
        self.window.present()
    

    # def on_button_clicked(self, object, data=None):
    #     global screen
    #     if screen == 'ERROR!':
    #         screen = ''

    #     # Change operator if there is no number
    #     try:
    #         if screen[-1] in operators and button in operators:
    #             screen = screen[:-1]
    #     except:
    #         pass

    #     # Remove first operator if it is not minus or paranthesis
    #     try:
    #         if screen[0] not in str(numbers):
    #             if screen[0] == '-':
    #                 pass
    #             elif screen[0] == '(':
    #                 pass
    #             else:
    #                 screen = screen[1:] 
    #     except:
    #         pass

    #     if button == '=': # Solve the expression
    #         try:
    #             screen = screen.replace('x', '*')
    #             screen = eval(screen)
    #             screen = round(screen, 6)
    #         except Exception as e:
    #             screen = 'ERROR!'
    #             print(e)
    #         screen = str(screen)
    #     elif button == 'C': # Erase the whole expression
    #         screen = ''
    #     elif button == '<<<': # Erase a character
    #         screen = screen[:-1]
    #     else: # Add number or operator to the expression
    #         screen = screen + str(button)
    #     self.update_screen(screen)
    

    def update_screen(self, text):
        self.Label1.set_text(text)


app = AppCalculator(application_id="com.github.ilkkako.gtk4-python-calculator")
app.run(sys.argv)
