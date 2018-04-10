import sys
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang.builder import Builder
from kivy.properties import StringProperty, ObjectProperty

class save(BoxLayout):

    def __init__(self, **kwargs):
        super(save, self).__init__(**kwargs)

    def name(self, name):
        self.content = name
        self.out = self.content

    def text(self, text):
        self.content = text
        self.out = self.content

    def fullname(self, name, x):
        str(self.name(name)) + str(x)

    def save(self, name, text, x):
        with open(str(self.fullname(name, x)), 'w') as output_file:
            output_file.write(text(text))

    def quit(self):
        sys.exit()

class SaveApp(App):

    def build(self):
        return save()

if __name__ == '__main__':
    SaveApp().run()