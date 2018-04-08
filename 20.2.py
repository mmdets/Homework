import sys
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.lang.builder import Builder
from kivy.uix.widget import Widget
from kivy.properties import StringProperty, ObjectProperty
from random import *

WordList = dict([(1 , 'Снег'), (2 , 'Солнце'), (3 , 'Лес'),\
    (4 , 'Красный'), (5 , 'Море'), (6 , 'Кот')])
Check = dict([('Snow' , 'Снег'), ('Sun' , 'Солнце'),\
    ('Forest' , 'Лес',), ('Red' , 'Красный'),\
    ('Sea' , 'Море'), ('Cat' , 'Кот')])

class translate(FloatLayout):

    inputElement = ObjectProperty(None)
    title = StringProperty(None)
    content = StringProperty(None)
    out = StringProperty(None)
    rus = StringProperty(None)

    def __init__(self, **kwargs):
        super(translate, self).__init__(**kwargs)

    def word(self):
        c = randint(1, len(WordList))
        WordList.get(c)


    def answer(self, text):
        self.content = text

        if self.content in Check:
            self.out = "Right!"
        else:
            self.out = "Try again."

    def check_press(self, a):
        self.content = text
        self.answer(self.content)

    def quit(self):
        sys.exit()

class TranslateApp(App):

    def build(self):
        return translate()

Builder.load_file('translate.kv')

if __name__ == '__main__':
    TranslateApp().run()
