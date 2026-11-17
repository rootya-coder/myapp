from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label


class Root(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", padding=24, spacing=16, **kwargs)
        self.counter = 0
        self.label = Label(text="Привет! Нажми кнопку", font_size="22sp")
        btn = Button(text="Нажми", size_hint_y=None, height=120, font_size="22sp")
        btn.bind(on_release=self.on_press)
        self.add_widget(self.label)
        self.add_widget(btn)

    def on_press(self, *_):
        self.counter += 1
        self.label.text = f"Нажатий: {self.counter}"


class MyApp(App):
    def build(self):
        return Root()


if __name__ == "__main__":
    MyApp().run()
