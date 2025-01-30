#!/data/data/com.termux/files/usr/bin/python
from glob import glob
import os
from time import sleep
import datetime
from tqdm import tqdm

ANDROID = glob("/storage/emulated/0/*")
PICS = "/storage/emulated/0/Statuses/Pics"
VIDS = "/storage/emulated/0/Statuses/Videos"

def copy_selection():
    os.system("clear")
    print("Choose What to Copy:")
    print("1. Pictures")
    print("2. Videos")
    print("3. Both")
    print("4. Exit")
    global choice 
    choice = input('Enter choice: ')

copy_selection()
if choice == '4':
	print('\nThank you for using Status Saver.')

while choice != '4':
	if "/storage/emulated/0/Statuses" in ANDROID:
		print("Statuses folder Exists")
	else:
		print("Making Statuses Folder")
		os.makedirs("/sdcard/Statuses")
		os.makedirs("/sdcard/Statuses/Pics")
		os.makedirs("/sdcard/Statuses/Videos")
	sleep(3)

	if choice.lower() == '1':
		pics = glob('/storage/emulated/0/Android/media/com.whatsapp/Whatsapp/Media/.Statuses/*.jpg')
		print("Saving Pictures")
		for i in tqdm(pics):
			date_made = datetime.datetime.fromtimestamp(os.path.getmtime(i))
			extension = os.path.splitext(i)[1]
			new_name = f"{date_made.strftime("%Y-%m-%d %H:%M:%S")}{extension}"
			new_file_path = os.path.join(PICS, new_name)
			with open(i, 'rb') as f:
				picture = f.read()
			with open(new_file_path, "wb") as f:
				f.write(picture)
			sleep(0.3)

	elif choice.lower() == '2':
		print("Saving Videos")
		videos = tqdm(glob('/storage/emulated/0/Android/media/com.whatsapp/Whatsapp/Media/.Statuses/*.mp4'))
		for i in videos:
			date_made = datetime.datetime.fromtimestamp(os.path.getmtime(i))
			extension = os.path.splitext(i)[1]
			new_name = f"{date_made.strftime("%Y-%m-%d %H:%M:%S")}{extension}"
			new_file_path = os.path.join(VIDS, new_name)
			with open(i, 'rb') as f:
				video = f.read()
			with open(new_file_path, "wb") as f:
				f.write(video)
			sleep(0.3)

	elif choice.lower() == '3':
		print("Saving both Videos and Pictures")
		videos = glob('/storage/emulated/0/Android/media/com.whatsapp/Whatsapp/Media/.Statuses/*.mp4')
		pics = glob('/storage/emulated/0/Android/media/com.whatsapp/Whatsapp/Media/.Statuses/*.jpg')
		all_ = tqdm(videos + pics)

		sleep(2)
		for i in all_:
			date_made = datetime.datetime.fromtimestamp(os.path.getmtime(i))
			extension = os.path.splitext(i)[1]
			new_name = f"{date_made.strftime("%Y-%m-%d %H:%M:%S")}{extension}"
			if extension == ".mp4":
				new_file_path = os.path.join(VIDS, new_name)
			elif extension == ".jpg":
				new_file_path = os.path.join(PICS, new_name)
			with open(i, 'rb') as f:
				file = f.read()
			with open(new_file_path, "wb") as f:
				f.write(file)
			sleep(0.3)

	elif choice.lower() == '4':
		print('Thank you for using Status Saver.')

	print('\nWhat would you like to do next?')
	print('1. Exit')
	print('2. Copy more items')
	selection = input('Your choice: ')

	if selection.lower() == '1':
		choice = '4'
	elif selection.lower() == '2':
		copy_selection()
	else:
		print('Please select either 1 or 2')
print('\nThank you for using Status Saver.')