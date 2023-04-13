import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button

kivy.require('2.0.0')  # Ensure you're using the correct Kivy version

# Create the screen classes for the main page and pages 1, 2, and 3
class MainPage(Screen):
    name = 'main'

class Page1(Screen):
    pass

class Page2(Screen):
    pass

class Page3(Screen):
    pass

class BackButton(Button):
    pass

# Create the screen manager to handle navigation between screens
class MyAppScreenManager(ScreenManager):
    pass

# Load the .kv files
gui_kv_files = ['app_kv/main.kv', 'app_kv/page1.kv', 'app_kv/page2.kv', 'app_kv/page3.kv', 'app_kv/back_button.kv']
for kv_file in gui_kv_files:
    Builder.load_file(kv_file)

# Create the main application class
class MyApp(App):
    def build(self):
        return MyAppScreenManager()

if __name__ == '__main__':
    MyApp().run()
