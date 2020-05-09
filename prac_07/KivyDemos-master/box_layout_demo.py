"""
CP1404/CP5632 Practical
Kivy GUI program to square a number
Sharon Regina Sutio
Link: https://github.com/SharonReginaSutio99/cp1404practicals
"""

from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    def build(self):
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        print('greet')
        print("test")
        self.root.ids.output_label.text = "Hello " + self.root.ids.input_name.text

    def event_handler(self):
        self.root.ids.input_name.text = ""
        self.root.ids.output_label.text = ""


BoxLayoutDemo().run()
