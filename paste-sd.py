with open("sd.py", "w") as f:
    f.write(r'''
import machine
import os
import sdcard

sck = machine.Pin(39)
mosi = machine.Pin(38)
miso = machine.Pin(40)
cs = machine.Pin(41)

spi = machine.SPI(2, baudrate=1000000, sck=sck, mosi=mosi, miso=miso)

def mnt():
    try:
        os.umount("/sd")
        print("/sd unmounted")
    except OSError:
        pass

    try:
        sd = sdcard.SDCard(spi, cs)
        vfs = os.VfsFat(sd)
        os.mount(vfs, "/sd")
        print("Files:", os.listdir("/sd"))
    except Exception as e:
        print("Mount failed:", e)

    ''')

import sd
