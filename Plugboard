##########
# Plugboard Dictionary
# Enigma Machine
# Chris Tapia
# 06/25/18
# CIS 220M
# Synopsis: creates the plugboard of the enigma machine
##########




import DriveLoc
import enigma_classes


from operator import itemgetter



# file = DriveLoc.DriveLocation()+"\plugboard\character set.txt"
# file_2 = DriveLoc.DriveLocation()+"\plugboard\pbwheel1.txt"
# file_3 = DriveLoc.DriveLocation()+"\plugboard\pbwheel2.txt"
# file_4 = DriveLoc.DriveLocation()+"\plugboard\pbwheel3.txt"


wheel_creator = enigma_classes.Wheel()


print("Let's setup your rotors..")
file_1 = input("Ignoring the drive location, type the first file location for the character set: ")
file_2 = input("Type the second file location. This completes the first rotor: ")


message = wheel_creator._Wheel__pbwheel(file_1, file_2)




#message = wheel_creator._Wheel__pbwheel(file_1, file_2)


print("now it's time to encrypt a message\n")


# enigma_classes.create_message(message)


print(enigma_classes.create_message(message))
input("Press 'enter' to end program")


### end ###
