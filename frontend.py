from kivy.app import App
from kivy.uix.widget import Widget


class MediaBrowserWidget(Widget):
    pass


class MediaBrowserApp(App):
    def build(self):
        return MediaBrowserWidget()


def main():
    MediaBrowserApp().run()


if __name__ == "__main__":
    main()
