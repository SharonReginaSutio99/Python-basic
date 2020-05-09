"""
Sharon Regina Sutio
Link: https://github.com/SharonReginaSutio99/cp1404practicals
Kivy App to convert miles to KM
"""
from kivy.app import App
from kivy.lang import Builder
from kivy.app import StringProperty

__author__ = 'Sharon Regina Sutio'
MILES_TO_KM = 1.60934


class MilesToKilometresApp(App):
    """MilesToKilometresApp is a Kivy app to convert miles to kilometres"""
    output = StringProperty()

    def build(self):
        """Build kivy app from kv file"""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file("convert_miles_km.kv")
        return self.root

    def handle_convert(self):
        """Handle conversion, output result to label widget"""
        value = self.get_valid_input()
        result = value * MILES_TO_KM
        self.root.ids.output_label.text = str(result)

    def get_valid_input(self):
        """Handle invalid input. If valid, return as float and if invalid, return 0"""
        try:
            value = float(self.root.ids.input_number.text)
            return value
        except ValueError:
            return 0

    def handle_increment(self, value, change):
        """Handle change in miles by +1 or -1"""
        value = self.get_valid_input()
        changed_value = float(value) + change
        self.root.ids.input_number.text = str(changed_value)


MilesToKilometresApp().run()
