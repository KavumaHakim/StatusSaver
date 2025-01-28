#!/data/data/com.termux/files/usr/bin/python
from glob import glob
import os
from time import sleep

pics = glob("/sdcard/Android/media/com.whatsapp/WhatsApp/Media/.Statuses/*.jpg")
videos = glob("/sdcard/Android/media/com.whatsapp/WhatsApp/Media/.Statuses/*.mp4")
ANDROID = glob("/sdcard/*")
print("Choose What to Copy:")
print("1. Pictures")
print("2. Videos")
print("3. Both")
print("4. Exit")
choice = input('Enter choice:' )

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
