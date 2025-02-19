from glob import glob
import os
import datetime

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

def main(c: int = 0) -> None:
    v = glob('/sdcard/Android/media/com.whatsapp/WhatsApp/Media/.Statuses/*mp4')
    p = glob('/sdcard/Android/media/com.whatsapp/WhatsApp/Media/.Statuses/*jpg')

    os.system("clear")
    print(banner)
    print("Choose What Statuses to save:")
    print("1. Pictures")
    print("2. Videos")
    print("3. Both")
    print("4. Exit")
    n = 1
    choice = c
    while n:
        if choice == 0:
            choice = input('Enter choice: ')
        if choice == '1':
            print('Saving Pics')
            for i in tqdm(p, colour="yellow", desc="Pics"):
                Status(file_type='pics', path=i)    
            n = 0
        elif choice == '2':
            print("Saving Videos")
            for i in tqdm(v, colour="Red", desc="Vids"):
                Status(file_type="video", path=i)
            n = 0
        elif choice == '3':
            print("Saving Pics and Videos")
            for i in tqdm(v, colour="Red", desc="Vids"):
                Status(file_type="video", path=i)
            for j in tqdm(p, colour="yellow", desc="Pics"):
                Status(file_type="pics", path=j)
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
    try:
        main(sys.argv[1])
    except:
        main()


    