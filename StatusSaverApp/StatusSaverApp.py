from kivy.uix.image import Image
from kivymd.app import MDApp
from kivymd.uix.card import MDCard
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window 
from kivy.lang import Builder


image_paths = []
for i in range(10):
	image_paths.append('sample_image.jpg')


class MyScreenManager(ScreenManager):
	pass

class HomeScreen(Screen):
	def picture(self):
		self.load_images()
		self.manager.current = 'image_screen'

	def load_images(self, image_path=image_paths):
		image_screen = self.manager.get_screen('image_screen')  # Get ImageScreen
		for image in image_path:
			preview = ImageCard()
			img = Image(source=image, pos_hint={'center_x': .5, 'center_y': .5})
			preview.add_widget(img)
			image_screen.ids.layout.add_widget(preview)  # Use ImageScreen's layout


class ImageScreen(Screen):
	pass

class ImageCard(MDCard):
	pass

class StatusSaverApp(MDApp):
	def build(self):
		Builder.load_file('StatusSaver.kv')
		Window.clearcolor = (1, 1, 1, 1)
		my_manager = MyScreenManager()
		home_screen = HomeScreen(name = 'home')
		image_screen = ImageScreen(name = 'image_screen')
		my_manager.add_widget(home_screen)
		my_manager.add_widget(image_screen)
		return my_manager



if __name__ == '__main__':
	StatusSaverApp().run()