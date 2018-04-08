import sys
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.lang.builder import Builder
from kivy.uix.widget import Widget
from kivy.properties import StringProperty, ObjectProperty

def cel(fahr):
    return (5 / 9 * (fahr - 32)) 

class Convert(GridLayout):

    inputElement = ObjectProperty(None)
    content = StringProperty(None)
    name = StringProperty(None)
    out = StringProperty(None)

    def __init__(self, **kwargs):
        super(Convert, self).__init__(**kwargs)

    def convert_press(self, fahr):
        self.content = fahr
        self.out = str(round(cel(int(self.content)), 4))

    def quit(self):
        sys.exit()

class ConvertApp(App):

    def build(self):
        return Convert()

Builder.load_file('Convert.kv')

if __name__ == '__main__':
    ConvertApp().run()