""" Basic calculator for GNOME. Programmed as a practice project."""

import sys
import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw, Gdk


@Gtk.Template(filename="calculator.ui")
class MainWindow(Gtk.ApplicationWindow):
    __gtype_name__ = "main_window"
    display = Gtk.Template.Child()


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.calculator = CalculatorEngine()
        self.light_mode = True
    

    def update_display(self, content):
        self.display.set_text(content)
    

    @Gtk.Template.Callback()
    def switch_light_mode(self, button):
        app = self.get_application()
        sm = app.get_style_manager()
        if self.light_mode:
            sm.set_color_scheme(Adw.ColorScheme.PREFER_DARK)
            self.light_mode = False
        else:
            sm.set_color_scheme(Adw.ColorScheme.PREFER_LIGHT)
            self.light_mode = True

    @Gtk.Template.Callback()
    def on_button_clicked(self, button):
        input = button.get_label()

        self.calculator.remove_error()
        self.calculator.add_zero(input) # Add 0 automatically if inputting point in empty expression
        self.calculator.validate_operator(input) # Change operator if user tries to input two in a row


        match input:
            case '=':
                self.calculator.calculate()
            case 'C':
                self.calculator.clear()
            case '<<':
                self.calculator.erase()
            case _:
                self.calculator.add_input(input)
        
        self.update_display(self.calculator.get_expression())


class Application(Adw.Application):
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


class CalculatorEngine():
    def __init__(self):
        self.expression = ''
        self.operators = ('+', '-', 'x', '/')


    def add_input(self, value):
        self.expression += value


    def clear(self):
        self.expression = ''
    

    def erase(self): 
        self.expression = self.expression[:-1]


    def calculate(self):
        try:
            new_expression = self.expression.replace('x', '*')
            solution = eval(new_expression)
            solution = round(solution, 6)
            self.expression = str(solution)
        except:
            self.expression = 'ERROR!'


    def get_expression(self):
        return self.expression
    

    def remove_error(self):
        if self.expression  == 'ERROR!':
            self.clear()
    

    def add_zero(self, input):
        if self.expression == '' and input == '.':
            self.add_input('0')
    

    def validate_operator(self, input):
        if self.expression and self.expression[-1] in self.operators and input in self.operators:
            self.erase()



if __name__ == '__main__':
    app = Application(application_id="com.github.ilkkako.gtk4-python-calculator")
    app.run(sys.argv)
