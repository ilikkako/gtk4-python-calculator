""" Basic calculator for GNOME. Programmed as a practice project."""

import sys, gi, re
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw, Gdk

numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
operators = ('+', '-', 'x', '/')
others = ('=', 'C', '(', ')', '<<<', '.')
buttons = numbers + operators + others
screen = "" # Stores values in calculator screen
margin_all = 10
margin_buttons = 1
margin_frame = 5
light_mode = True


@Gtk.Template(filename="calculator.ui")
class MainWindow(Gtk.ApplicationWindow):
    __gtype_name__ = "main_window"
    display = Gtk.Template.Child()


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    

    def update_display(self, content):
        self.display.set_text(content)
    

    def solve(self, expression):
        try:
            new_expression = expression.replace('x', '*') # Fix multiply symbol so eval function can solve the problem 
            solution = eval(new_expression)
            solution = round(solution, 6) # Round to avoid rounding error
        except Exception as e:
            print(e)
            return 'ERROR!'

        return str(solution)
    

    @Gtk.Template.Callback()
    def switch_mode(self, button):
        app = self.get_application()
        sm = app.get_style_manager()
        global light_mode
        if light_mode:
            sm.set_color_scheme(Adw.ColorScheme.PREFER_DARK)
            light_mode = False
        else:
            sm.set_color_scheme(Adw.ColorScheme.PREFER_LIGHT)
            light_mode = True

    @Gtk.Template.Callback()
    def on_button_clicked(self, button):
        input = button.get_label()

        global screen
        if screen == 'ERROR!':
            screen = ''

        # Change operator if there is no number
        try:
            if screen[-1] in operators and input in operators:
                screen = screen[:-1]
        except:
            pass

        # Remove first operator if it is not minus or paranthesis
        try:
            if screen[0] not in str(numbers):
                if screen[0] == '-':
                    pass
                elif screen[0] == '(':
                    pass
                else:
                    screen = screen[1:] 
        except:
            pass

        if input == '=': # Solve the expression
            screen = self.solve(screen)
        elif input == 'C': # Erase the whole expression
            screen = ''
        elif input == '<<': # Erase a character
            screen = screen[:-1]
        else: # Add number or operator to the expression
            screen = screen + str(input)
        
        self.update_display(screen)


class AppCalculator(Adw.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.connect('activate', self.on_activate)


    def on_activate(self, app):
        window = MainWindow(application=self)
        window.present()

        css_provider = Gtk.CssProvider()
        css_provider.load_from_path('stylesheet.css')

        display = Gdk.Display.get_default()
        Gtk.StyleContext.add_provider_for_display(display, css_provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)


app = AppCalculator(application_id="com.github.ilkkako.gtk4-python-calculator")
app.run(sys.argv)