#!/data/data/com.termux/files/usr/bin/python
from glob import glob
import os
from time import sleep
import datetime
from tqdm import tqdm

class Status:
    banner = '''
░██████╗ ████████╗ ░█████╗░ ████████╗ ██╗░░░██╗ ░██████╗
██╔════╝ ╚══██╔══╝ ██╔══██╗ ╚══██╔══╝ ██║░░░██║ ██╔════╝
╚█████╗░ ░░░██║░░░ ███████║ ░░░██║░░░ ██║░░░██║ ╚█████╗░
░╚═══██╗ ░░░██║░░░ ██╔══██║ ░░░██║░░░ ██║░░░██║ ░╚═══██╗
██████╔╝ ░░░██║░░░ ██║░░██║ ░░░██║░░░ ╚██████╔╝ ██████╔╝
╚═════╝░ ░░░╚═╝░░░ ╚═╝░░╚═╝ ░░░╚═╝░░░ ░╚═════╝░ ╚═════╝░ 

        ░██████╗ ░█████╗░ ██╗░░░██╗ ███████╗ ██████╗░
        ██╔════╝ ██╔══██╗ ██║░░░██║ ██╔════╝ ██╔══██╗
        ╚█████╗░ ███████║ ╚██╗░██╔╝ █████╗░░ ██████╔╝
        ░╚═══██╗ ██╔══██║ ░╚████╔╝░ ██╔══╝░░ ██╔══██╗
        ██████╔╝ ██║░░██║ ░░╚██╔╝░░ ███████╗ ██║░░██║
        ╚═════╝░ ╚═╝░░╚═╝ ░░░╚═╝░░░ ╚══════╝ ╚═╝░░╚═╝
        '''

    def __init__(self):
        self.ANDROID = glob("/storage/emulated/0/*")
        self.PICS = "/storage/emulated/0/Statuses/Pics"
        self.VIDS = "/storage/emulated/0/Statuses/Videos"
        self.videos = glob('/storage/emulated/0/Android/media/com.whatsapp/Whatsapp/Media/.Statuses/*.mp4')
        self.pics = glob('/storage/emulated/0/Android/media/com.whatsapp/Whatsapp/Media/.Statuses/*.jpg')
    
    def check_folders(self):
        self.__init__()
        if "/storage/emulated/0/Statuses" in self.ANDROID:
            print("Statuses folder Exists")
        else:
            print("Making Statuses Folder")
            os.makedirs("/sdcard/Statuses")
            os.makedirs("/sdcard/Statuses/Pics")
            os.makedirs("/sdcard/Statuses/Videos")
    def save_pics(self):
        for i in tqdm(self.pics, colour="GREEN", desc="Saving Pictures", unit="pics", unit_scale=True, unit_divisor=1024, dynamic_ncols=True):
            date_made = datetime.datetime.fromtimestamp(os.path.getmtime(i))
            extension = os.path.splitext(i)[1]
            new_name = f"{date_made.strftime('%Y-%m-%d %H:%M:%S')}{extension}"
            new_file_path = os.path.join(self.PICS, new_name)
            with open(i, 'rb') as f:
                picture = f.read()
            with open(new_file_path, "wb") as f:
                f.write(picture)
            sleep(0.5)
    def save_video(self):
        for i in tqdm(self.videos, colour="RED", desc="Saving Videos", unit="vids", unit_scale=True, unit_divisor=1024, dynamic_ncols=True):
            date_made = datetime.datetime.fromtimestamp(os.path.getmtime(i))
            extension = os.path.splitext(i)[1]
            new_name = f"{date_made.strftime('%Y-%m-%d %H:%M:%S')}{extension}"
            new_file_path = os.path.join(self.VIDS, new_name)
            with open(i, 'rb') as f:
                video = f.read()
            with open(new_file_path, "wb") as f:
                f.write(video)
            sleep(0.5)

    def save_both(self):
        all_ = tqdm(self.videos + self.pics, colour="MAGENTA", desc="Saving all", unit="files", unit_scale=True, unit_divisor=1024, dynamic_ncols=True)
        for i in all_:
            date_made = datetime.datetime.fromtimestamp(os.path.getmtime(i))
            extension = os.path.splitext(i)[1]
            new_name = f"{date_made.strftime('%Y-%m-%d %H:%M:%S')}{extension}"
            if extension == ".mp4":
                new_file_path = os.path.join(self.VIDS, new_name)
            elif extension == ".jpg":
                new_file_path = os.path.join(self.PICS, new_name)
            with open(i, 'rb') as f:
                file = f.read()
            with open(new_file_path, "wb") as f:
                f.write(file)
        sleep(0.2)
    def delete_old(self):
        pass
        # TODO: implement this method
        # _old = 7
        # for i in tqdm(self.videos + self.pics):
        #     if datetime.datetime.now().strftime("%Y-%m-%d") - datetime.datetime.fromtimestamp(os.path.getmtime(i)).strftime("%Y-%m-%d") >= _old:
        #         print("Old")


def main():
    os.system("clear")
    print(Status.banner)
    print("Choose What Statuses to save:")
    print("1. Pictures")
    print("2. Videos")
    print("3. Both")
    print("4. Exit")
    global choice 
    Status().check_folders()
    n = 1
    while n:
        choice = input('Enter choice: ')
        if choice == '1':
            print('Saving Pics')
            Status().save_pics()
            n = 0
        elif choice == '2':
            print('Saving videos')
            Status().save_video()
            n = 0
        elif choice == '3':
            print('Saving all')
            Status().save_both()
            n = 0
        elif choice == '4':
            exit('Thank you for using Status saver')
        else:
            print("Invalid Input!!")
            continue
    else:
        print('Thank you for Using status saver')
        if input('Save sth else? y/n > ').lower() == 'y':
            main()

if __name__ == "__main__":
    main()
