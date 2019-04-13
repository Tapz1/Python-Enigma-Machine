##########
# Chris Tapia
# CIS 220M
# this program will fetch the drive letter/location of a USB drive
##########


from string import ascii_uppercase
import os

# finds the drive
def DriveLocation():
    for USBPATH in ascii_uppercase:
         if os.path.exists('%s:\\ProgramFile.txt' % USBPATH):
            USBPATH='%s:\\' % USBPATH
            print('USB Drive Letter is', USBPATH)
            return USBPATH + ""
    return ""
    drive = DriveLocation()

#while drive == "":
#    print('Plug in your USB and hit enter to detect drive letter', end="")
#   input()
#    drive = DriveLocation()

# this shows that the drive letter can then be used anywhere in a program
#print(drive)
