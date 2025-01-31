from kivymd.app import MDApp
from kivymd.uix.card import MDCard
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window 
from kivy.lang import Builder


image_paths = []
for i in range(10):
	image_paths.append('sample_image.jpg')
print(image_paths)


class MyScreenManager(ScreenManager):
	pass

class HomeScreen(Screen):
	def picture(self):
		self.load_images(image_paths)
		self.manager.current = 'images'
	def load_images(self, image_paths):
		for image in image_paths:
			preview = ImageCard()
			self.manager.ids['images'].ids['layout'].add_widget(preview)


class ImageScreen(Screen):
	pass

class ImageCard(MDCard):
	pass

class StatusSaverApp(MDApp):
	def build(self):
		Builder.load_file('StatusSaver.kv')
		Window.clearcolor = (1, 1, 1, 1)
		my_manager = MyScreenManager()
#		home_screen = HomeScreen(name = 'home') 
#		image_screen = ImageScreen(name = 'images')
#		my_manager.add_widget(home_screen)
#		my_manager.add_widget(image_screen)
		return my_manager
	


if __name__ == '__main__':
	StatusSaverApp().run()