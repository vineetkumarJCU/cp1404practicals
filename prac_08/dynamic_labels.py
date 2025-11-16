"""
CP1404 Practical 08
Dynamic Labels App
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """App that dynamically creates Labels from a list of names."""

    def __init__(self, **kwargs):
        """Initialise the app."""
        super().__init__(**kwargs)
        self.names = ["Vineet", "Ron", "Charlie", "Clark", "Ethan"]

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file("dynamic_labels.kv")
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create and display labels from list of names."""
        for name in self.names:
            temp_label = Label(text=name, color=(1, 0.6, 0, 1), font_size=24)
            self.root.ids.main.add_widget(temp_label)


DynamicLabelsApp().run()

