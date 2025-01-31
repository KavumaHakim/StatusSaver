#!/data/data/com.termux/files/usr/bin/python
from glob import glob
import os
from time import sleep

pics = glob("/sdcard/Android/media/com.whatsapp/WhatsApp/Media/.Statuses/*.jpg")
videos = glob("/sdcard/Android/media/com.whatsapp/WhatsApp/Media/.Statuses/*.mp4")
ANDROID = glob("/sdcard/*")

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
	if "/sdcard/Statuses" in ANDROID:
		print("Statuses folder Exists")
	else:
		print("Making Statuses Folder")
		os.system("mkdir /sdcard/Statuses")
		os.system("mkdir /sdcard/Statuses/Pics")
		os.system("mkdir /sdcard/Statuses/Videos")
	sleep(3)

	if choice.lower() == '1':
		print("Saving Pictures")

		for i in pics:
			print(f'Copying: {i}\n')
			os.system(f"cp {i} /sdcard/Statuses/Pics")
			sleep(0.3)

	elif choice.lower() == '2':
		print("Saving Videos")
		sleep(2)

		for i in videos:
			print(f'Copying: {i}\n')
			os.system(f"cp {i} /sdcard/Statuses/Videos")
			sleep(0.3)

	elif choice.lower() == '3':
		print("Saving both Videos and Pictures")
		sleep(2)

		for i in pics:
			print(f'Copying: {i}\n')
			os.system(f"cp {i} /sdcard/Statuses/Pics")
		for i in videos:
			print(f'Copying: {i}\n')
			os.system(f"cp {i} /sdcard/Statuses/Videos")

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