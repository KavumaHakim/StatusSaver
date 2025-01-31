from kivymd.app import MDApp
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window 
from kivy.lang import Builder

class MyScreenManager(ScreenManager):
	pass


class HomeScreen(Screen):
	pass

class ImageScreen(Screen):
	pass


class MyApp(MDApp):
	def build(self):
		Builder.load_file('StatusSaver.kv')
		Window.clearcolor = (1, 1, 1, 1)
		my_manager = MyScreenManager()
		home_screen = HomeScreen(name = 'home') 
		image_screen = ImageScreen(name = 'images')
		my_manager.add_widget(home_screen)
		my_manager.add_widget(image_screen)
		return my_manager



if __name__ == '__main__':
	MyApp().run()