from kivy.uix.screenmanager import ScreenManager, Screen, RiseInTransition, FallOutTransition
from kivymd.uix.segmentedbutton import MDSegmentedButtonItem
from kivymd.uix.card import MDCard
from kivy.uix.image import Image
from kivymd.app import MDApp
from kivy.core.window import Window 
from kivy.lang import Builder
from glob import glob

# '''Change this back before push'''
# image_paths_all = glob('C:/Users/user/Desktop/my_folder/.Statuses/*.jpg')
# image_paths_saved = glob('C:/Users/user/Desktop/my_folder/Saved/Pics/*.jpg')

# -----READ ME------- #
#Leave the above declractions in the code since I need them to test the UI in my computer
#I only use the phone for small adjustments
# --------END--------#
image_paths_all = glob('/storage/emulated/0/Android/media/com.whatsapp/Whatsapp/Media/.Statuses/*.jpg')
image_paths_saved = glob('/storage/emulated/0/Statuses/*.jpg')

class MyScreenManager(ScreenManager):
	pass


class HomeScreen(Screen):
	def picture(self):
		self.manager.current = 'image_screen'


class ImageScreen(Screen):
	def expand(self, src):
		image_view = self.manager.get_screen('image_view')
		image_view.ids.view_img.source = src
		self.manager.transition = RiseInTransition()
		self.manager.current = 'image_view'
		global idx
		idx = image_path.index(src)
	def change_content(self, tab):
		content_grid = self.ids.layout
		content_grid.clear_widgets()
		global image_path
		if tab == 'all_tab':
			image_path = image_paths_all
		elif tab == 'saved_tab':
			image_path = image_paths_saved
		else:
			return
		for image in image_path:
			preview = ImageCard()
			img = Image(source=image, pos_hint={'center_x': .5, 'center_y': .5})
			preview.add_widget(img)
			content_grid.add_widget(preview)

class ImageViewer(Screen):
	def contract(self):
		self.manager.transition = FallOutTransition()
		self.manager.current = 'image_screen'
	def next_img(self):
		global idx
		idx += 1
		if idx >= len(image_path):
			idx = len(image_path)-1
		self.ids.view_img.source = image_path[idx]
	def prev_img(self):
		global idx
		idx -= 1
		if idx < 0:
			idx = 0
		self.ids.view_img.source = image_path[idx]


class CustomSegment(MDSegmentedButtonItem):
	def on_active(self, instance, value):
		self.check_visible = False


class ImageCard(MDCard):
	pass



class StatusSaverApp(MDApp):
	def build(self):
		Builder.load_file('StatusSaver.kv')
		Window.clearcolor = (1, 1, 1, 1)
		my_manager = MyScreenManager()
		home_screen = HomeScreen(name = 'home')
		image_screen = ImageScreen(name = 'image_screen')
		image_view = ImageViewer(name = 'image_view')
		my_manager.add_widget(home_screen)
		my_manager.add_widget(image_screen)
		my_manager.add_widget(image_view)
		my_manager.current = 'home'
		return my_manager



if __name__ == '__main__':
	StatusSaverApp().run()