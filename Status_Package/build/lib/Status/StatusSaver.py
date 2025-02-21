from glob import glob
import os
import datetime
import sys
from tqdm import tqdm

class Status:
    def __init__(self,file_type:str ="video", path:str = ''):
        self.ANDROID = glob("/storage/emulated/0/*")
        self.PICS = "/storage/emulated/0/Statuses/Pics"
        self.VIDS = "/storage/emulated/0/Statuses/Videos"
        self.types = ['video', 'pics']

        if path not in glob("/storage/emulated/0/Android/media/com.whatsapp/WhatsApp/Media/.Statuses/*") + glob("/sdcard/Android/media/com.whatsapp/WhatsApp/Media/.Statuses/*"):
            raise FileNotFoundError(f"{path} - File not found among  Whatsapp Statuses")
        try:
            if file_type in self.types:
                if file_type == "video":
                    n = self.VIDS
                elif (file_type == 'pics'):
                    n = self.PICS
                date_made = datetime.datetime.fromtimestamp(os.path.getmtime(path))
                extension = os.path.splitext(path)[1]
                new_name = f"{date_made.strftime('%Y-%m-%d %H:%M:%S')}{extension}"
                new_file_path = os.path.join(n, new_name)
                with open(path, 'rb') as f:
                    video = f.read()
                with open(new_file_path, "wb") as f:
                    f.write(video)
            else:
                raise ValueError(f"{file_type} - Not known: valid values are 'video', 'pics'")
        except FileNotFoundError :
            if "/storage/emulated/0/Statuses" in self.ANDROID:
                print("Statuses folder Exists")
            else:
                print("Making Statuses Folder")
                os.makedirs("/sdcard/Statuses")
                os.makedirs("/sdcard/Statuses/Pics")
                os.makedirs("/sdcard/Statuses/Videos")
            Status(file_type, path)
