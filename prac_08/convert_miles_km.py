from kivy.app import App
from kivy.lang import Builder

MILES_TO_KM = 1.60934


class SquareNumberApp(App):
    """Convert miles to kilometres."""

    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file("convert_miles_km.kv")
        return self.root

    def handle_convert(self):
        """Convert miles input to kilometres."""
        try:
            miles = float(self.root.ids.input_miles.text)
            km = miles * MILES_TO_KM
            self.root.ids.output_label.text = f"{km:.5f}"
        except ValueError:
            self.root.ids.output_label.text = "0.0"

    def handle_increment(self, change):
        """Increase or decrease the miles input."""
        try:
            miles = float(self.root.ids.input_miles.text)
        except ValueError:
            miles = 0
        miles += change
        self.root.ids.input_miles.text = str(miles)
        self.handle_convert()


SquareNumberApp().run()
