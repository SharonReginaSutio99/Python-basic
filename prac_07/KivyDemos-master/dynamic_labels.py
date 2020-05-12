"""
Name: Sharon Regina Sutio
Link: https://github.com/SharonReginaSutio99/cp1404practicals
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """Main program - Kivy app to make dynamic labels."""

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        self.names = ["Alan", "Jack", "Bob", "Sarah"]

    def build(self):
        """Build Kivy GUI."""
        self.title = 'Dynamic Labels'
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create labels from list entries and add them to GUI."""
        for name in self.names:
            temp_label = Label(text=name)
            self.root.ids.labels_box.add_widget(temp_label)


DynamicLabelsApp().run()
