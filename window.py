import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw

import calculator

@Gtk.Template(filename="calculator.ui")
class MainWindow(Gtk.ApplicationWindow):
    __gtype_name__ = "main_window"
    display = Gtk.Template.Child()


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.calculator = calculator.CalculatorEngine()
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