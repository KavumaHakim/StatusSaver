from Status import Status
from glob import glob
import os
import sys
from tqdm import tqdm
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
    args = sys.argv
    if (len(args) == 2) and (args[1] in ["1","2","3"]):
        choice = args[1]
    else:
        choice = 0
        
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
        main()