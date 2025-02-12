from kivy.uix.accordion import NumericProperty
from kivy.uix.accordion import ObjectProperty
from kivy.uix.accordion import StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen, RiseInTransition, FallOutTransition
from kivymd.uix.segmentedbutton import MDSegmentedButtonItem
from kivy.uix.modalview import ModalView
# from kivy.properties import StringProperty
from kivy.graphics.texture import Texture
from kivy.core.window import Window
from kivymd.uix.card import MDCard
from kivy.uix.image import Image
from kivy.lang import Builder
from kivy.clock import Clock
from kivymd.app import MDApp
from glob import glob
import asynckivy
import cv2

'''Change this back before push'''
Window.size = (400, 650)
image_paths_all = glob('C:/Users/user/Desktop/my_folder/.Statuses/*.jpg')
image_paths_saved = glob('C:/Users/user/Desktop/my_folder/Saved/Pics/*.jpg')
video_paths_all = glob('C:/Users/user/Desktop/my_folder/.Statuses/*.mp4')
video_paths_saved = glob('C:/Users/user/Desktop/my_folder/Saved/Vids/*.mp4')

# -----READ ME------- #
#Leave the above declaractions in the code since I need them to test the UI in my computer
#I only use the phone for small adjustments

### -----  TODO  ----- ###
#	Figure out cause of the dual-popup and fix it, then enable autoplay
#	Add saving ability for both images and videos
#	Add ability to switch between videos
#	Fix end-of-stream glitch

# --------END--------#

# image_paths_all = glob('/storage/emulated/0/Android/media/com.whatsapp/Whatsapp/Media/.Statuses/*.jpg')
# image_paths_saved = glob('/storage/emulated/0/Statuses/*.jpg')
# video_paths_all = glob('/storage/emulated/0/Android/media/com.whatsapp/Whatsapp/Media/.Statuses/*.mp4')
# video_paths_saved = glob('/storage/emulated/0/Statuses/*.mp4')

class MyScreenManager(ScreenManager):
	pass


class HomeScreen(Screen):
	def change_screen(self, screen):
		self.manager.current = screen


class ImageScreen(Screen):

	async def async_load_images(self, image_list):
		content_grid = self.ids.layout
		content_grid.clear_widgets()
		for image in image_list:
			preview = ImageCard()
			img = Image(source=image, pos_hint={'center_x': .5, 'center_y': .5})
			preview.add_widget(img)
			Clock.schedule_once(lambda dt: content_grid.add_widget(preview))
			await asynckivy.sleep(0.2)  # Lets Kivy process events

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
		# Start loading asynchronously
		asynckivy.start(self.async_load_images(image_path))

	def expand(self, src):
		image_view = self.manager.get_screen('image_view')
		image_view.ids.view_img.source = src
		self.manager.transition = RiseInTransition()
		self.manager.current = 'image_view'
		global idx
		idx = image_path.index(src)


class VideoScreen(Screen):
	video_view = ObjectProperty()

	def generate_thumbnail(self, video, timestamp = .2):
		cap = cv2.VideoCapture(video)
		cap.set(cv2.CAP_PROP_POS_MSEC, timestamp * 1000)		# Setting thumbnail to 'timestamp' seconds in.
		success, frame = cap.read()								# Getting frame data
		cap.release()
		if not success:
			return None
		frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)			# Convert BGR to RGB color format
		frame = cv2.flip(frame, 0)								# Flip image vertically. (FIX)
		buf = frame.tobytes()
		height, width, _ = frame.shape
		texture = Texture.create(size=(width, height))			# Create image texture
		texture.blit_buffer(buf, colorfmt = 'rgb', bufferfmt = 'ubyte')
		return texture

	async def async_load_thumbnails(self, video_list):
		content_grid = self.ids.vid_layout
		content_grid.clear_widgets()
		added_video_ids = set()				
		for index, video in enumerate(video_list):	
			video_id = index						
			if video_id in added_video_ids:			
				continue							
			thumbnail = Image(pos_hint={'center_x': .5, 'center_y': .5})
			texture = self.generate_thumbnail(video)
			if texture:
				thumbnail.texture = texture
			preview = VideoCard()
			preview.vid_src = video
			preview.add_widget(thumbnail)
			duplicate_found = False					
			for child in content_grid.children:
				if getattr(child, 'video_id', None) == video_id:
					duplicate_found = True
					break
			if not duplicate_found:
				content_grid.add_widget(preview)
				added_video_ids.add(video_id)  # Mark this video as added
			await asynckivy.sleep(0.1)  # Lets Kivy process events

	def change_content(self, tab):
		global video_path
		content_grid = self.ids.vid_layout
		content_grid.clear_widgets()
		if tab == 'all_tab':
			video_path = video_paths_all
		elif tab == 'saved_tab':
			video_path = video_paths_saved
		else:
			return
		# Start loading asynchronously
		asynckivy.start(self.async_load_thumbnails(video_path))
		self.ids.vid_layout.clear_widgets()

	def expand(self, src):
		self.video_view = VideoPopup()
		if self.video_view.video_source != src:
			self.video_view.video_source = src  # Change source only if needed
		self.video_view.open()


class VideoPopup(ModalView):
	video_source = StringProperty()
	progress = NumericProperty(0)
	start_time = 1

	def __init__(self, **kwargs):
		super(VideoPopup, self).__init__(**kwargs)
		self.bind(on_open=self._bind_video)
		self.video_length = 1

	def _bind_video(self, *args):
		video = self.ids.video
		video.bind(on_duration = self.update_duration)
		video.bind(on_position = self.update_progress)
		Clock.schedule_interval(self.update_progress_bar, .1)

	def update_duration(self, instance, value):
		self.video_length = value if value > 0 else 1

	def update_progress(self, instance, value):
		self.progress = (value / self.video_length) * 100

	def update_progress_bar(self, dt):
		video = self.ids.video
		if video.duration > 0:
			self.progress = (video.position / video.duration) * 100

	def play_pause(self):
		video = self.ids.video
		btn_icon = self.ids.icon_play
		if video.state == 'play':
			video.state = 'pause'
		else:
			video.state = 'play'
	
	def play_next(self):
		pass

	def play_previous(self):
		pass

	def close_popup(self):
		self.dismiss()

	def end_of_video(self, instance):
		instance.state = 'stop'


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


class VideoCard(MDCard):
	vid_src = StringProperty()



class StatusSaverApp(MDApp):

	def build(self):
		Builder.load_file('StatusSaver.kv')
		Window.clearcolor = (1, 1, 1, 1)
		my_manager = MyScreenManager()
		home_screen = HomeScreen(name = 'home')
		image_screen = ImageScreen(name = 'image_screen')
		video_screen = VideoScreen(name = 'video_screen')
		image_view = ImageViewer(name = 'image_view')
		my_manager.add_widget(home_screen)
		my_manager.add_widget(image_screen)
		my_manager.add_widget(video_screen)
		my_manager.add_widget(image_view)
		my_manager.current = 'home'
		return my_manager



if __name__ == '__main__':
	StatusSaverApp().run()