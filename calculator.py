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

class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.set_default_size(400,500)
        # self.set_title('Calculator')
        # self.arrange_calculator_gui()

    # def arrange_calculator_gui(self):

    #     self.MainBox = Gtk.Box(
    #         orientation=Gtk.Orientation.VERTICAL,
    #         margin_top = margin_all,
    #         margin_bottom = margin_all,
    #         margin_start =  margin_all,
    #         margin_end = margin_all 
    #         )
    #     self.ScreenFrame = Gtk.Frame(hexpand = True, vexpand = True, margin_bottom = margin_frame)
    #     self.Grid = Gtk.Grid(hexpand = True, vexpand = True)
    #     self.set_child(self.MainBox)
    #     self.MainBox.append(self.ScreenFrame)
    #     self.MainBox.append(self.Grid)

    #     self.Label1 = Gtk.Label()
    #     self.ScreenFrame.set_child(self.Label1)

    #     # Arrange and attach buttons to the grid!
    #     for button in buttons:
    #         self.button = Gtk.Button(
    #             label=str(button), 
    #             hexpand = True, 
    #             vexpand = True,
    #             margin_top = margin_buttons,
    #             margin_bottom = margin_buttons,
    #             margin_start =  margin_buttons,
    #             margin_end = margin_buttons
    #             )
    #         try:
    #             if button >= 1 and button <=3:
    #                 self.Grid.attach(self.button,button-1,1,1,1)   
    #             elif button >= 4 and button <= 6:
    #                 self.Grid.attach(self.button,button-4,2,1,1)  
    #             elif button >= 7:
    #                 self.Grid.attach(self.button,button-7,3,1,1) 
    #             else:
    #                 self.Grid.attach(self.button,0,4,1,1)
    #         except:
    #             if button == '.':
    #                 self.Grid.attach(self.button,1,4,1,1)
    #             elif button == '+':
    #                 self.Grid.attach(self.button,3,1,1,1)
    #             elif button == '-':
    #                 self.Grid.attach(self.button,3,2,1,1)
    #             elif button == 'x':
    #                 self.Grid.attach(self.button,3,3,1,1)
    #             elif button == '/':
    #                 self.Grid.attach(self.button,2,4,1,1)
    #             elif button == '=':
    #                 self.Grid.attach(self.button,3,4,1,1)
    #             elif button == 'C':
    #                 self.Grid.attach(self.button,0,0,1,1)
    #             elif button == '<<<':
    #                 self.Grid.attach(self.button,3,0,1,1)
    #             elif button == '(':
    #                 self.Grid.attach(self.button,1,0,1,1)
    #             elif button == ')':
    #                 self.Grid.attach(self.button,2,0,1,1)

    #         #Connect buttons to function
    #         self.button.connect('clicked', self.manage_buttons, button)
        
    def manage_buttons(self, num, button):
        global screen
        if screen == 'ERROR!':
            screen = ''

        # Change operator if there is no number
        try:
            if screen[-1] in operators and button in operators:
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

        if button == '=': # Solve the expression
            try:
                screen = screen.replace('x', '*')
                screen = eval(screen)
                screen = round(screen, 6)
            except Exception as e:
                screen = 'ERROR!'
                print(e)
            screen = str(screen)
        elif button == 'C': # Erase the whole expression
            screen = ''
        elif button == '<<<': # Erase a character
            screen = screen[:-1]
        else: # Add number or operator to the expression
            screen = screen + str(button)
        self.update_screen(screen)
    
    def update_screen(self, text):
        self.Label1.set_text(text)


class AppCalculator(Adw.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.connect('activate', self.on_activate)

    def on_activate(self, app):
        # Create UI from XML file
        builder = Gtk.Builder()
        builder.new_from_file('calculator.ui')

        # Obtain and show main window 
        self.win = builder.get_object('main_window')
        self.win.set_application(self)
        self.win.present()



app = AppCalculator(application_id="com.github.ilkkako.gtk4-python-calculator")
app.run(sys.argv)
