from kivy.app import App
from kivy.lang import Builder


class DynamicLabelsApp(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ["Vineet", "Ron", "Charlie", "Clark", "Ethan"]


    def build(self):
        self.title = "Dynamic Labels"
        self.root = Builder.load_file("dynamic_labels.kv")
        return self.root

DynamicLabelsApp().run()
