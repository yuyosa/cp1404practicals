from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.label import Label


names = ["yuyosa", "Rouboute", "Badan", "Dovalo"]

class Names_lists(App):

    def build(self):
        Window.size = (300, 200)
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_buttons()
        return self.root

    def create_buttons(self):
        for name in names:
            name_button = Label(text=name)
            self.root.ids.main.add_widget(name_button)

Names_lists().run()