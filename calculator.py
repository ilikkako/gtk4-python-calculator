""" This is where project description comes. Right now I am testing how to commit changes through visual code. """

import sys, gi, re
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw

buttons = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, '.', '+', '-', '*', '/', '=', 'C', '<<<')
screen = "" # Stores values in calculator screne

class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_default_size(600,600)
        self.set_title('Calculator')

        self.MainBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.HorizontalBox1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.Grid = Gtk.Grid()
        self.set_child(self.MainBox)
        self.MainBox.append(self.HorizontalBox1)
        self.MainBox.append(self.Grid)

        self.Label1 = Gtk.Label(label='This is where the number screen will be!')
        self.HorizontalBox1.append(self.Label1)

        # Arrange and attach buttons to the grid!
        for but in buttons:
            self.button = Gtk.Button(label=str(but))
            try:
                if but >= 1 and but <=3:
                    self.Grid.attach(self.button,but-1,1,1,1)   
                elif but >= 4 and but <= 6:
                    self.Grid.attach(self.button,but-4,2,1,1)  
                elif but >= 7:
                    self.Grid.attach(self.button,but-7,3,1,1) 
                else:
                    self.Grid.attach(self.button,0,4,1,1)
            except:
                if but == '.':
                    self.Grid.attach(self.button,1,4,1,1)
                elif but == '+':
                    self.Grid.attach(self.button,4,1,1,1)
                elif but == '-':
                    self.Grid.attach(self.button,4,2,1,1)
                elif but == '*':
                    self.Grid.attach(self.button,4,3,1,1)
                elif but == '/':
                    self.Grid.attach(self.button,2,4,1,1)
                elif but == '=':
                    self.Grid.attach(self.button,4,4,1,1)
                elif but == 'C':
                    self.Grid.attach(self.button,0,0,1,1)
                elif but == '<<<':
                    self.Grid.attach(self.button,1,0,4,1)

            #Connect buttons to function
            self.button.connect('clicked', self.manage_buttons, but)
        
    def manage_buttons(self, button, num):
        global screen
        if screen == 'ERROR!':
            screen = ''
        if num == '=':
            for c in screen:
                if c[0] == '0.':
                    pass
                elif c[0] == '0':
                    screen = screen[1:]
            try:
                screen = eval(screen)
            except Exception as e:
                screen = 'ERROR!'
                print(e)
            screen = str(screen)
        elif num == 'C':
            screen = ''
        elif num == '<<<':
            screen = screen[:-1]
        else:
            screen = screen + str(num)
        self.update_screen(screen)
    
    def update_screen(self, text):
        self.Label1.set_text = text
        print(text)


class AppCalculator(Adw.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.connect('activate', self.on_activate)

    def on_activate(self, app):
        self.win = MainWindow(application=app)
        self.win.present()


app = AppCalculator(application_id="com.github.ilkkako.gtk4-python-calculator")
app.run(sys.argv)
