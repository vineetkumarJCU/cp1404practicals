from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934


class SquareNumberApp(App):
    """Convert miles to kilometres app using StringProperty."""

    output_km = StringProperty("0.0")

    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file("convert_miles_km.kv")
        return self.root

    def handle_convert(self):
        """Convert miles input to kilometres."""
        try:
            miles = float(self.root.ids.input_miles.text)
            km = miles * MILES_TO_KM
            self.output_km = f"{km:.5f}"
        except ValueError:
            self.output_km = "0.0"

    def handle_increment(self, change):
        """Increase or decrease miles input."""
        try:
            miles = float(self.root.ids.input_miles.text)
        except ValueError:
            miles = 0
        miles += change
        self.root.ids.input_miles.text = str(miles)
        self.handle_convert()

SquareNumberApp().run()