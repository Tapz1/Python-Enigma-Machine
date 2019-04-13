##########
# My Encryptor
# Enigma Machine
# Chris Tapia
# 06/25/18
# CIS 220M
# Synopsis: classes for creating the wheel
##########


import DriveLoc


# file = DriveLoc.DriveLocation()+"\plugboard\character set.txt"
# file_2= DriveLoc.DriveLocation()+"\plugboard\pbwheel1.txt"




class Wheel:


    def __int__(self, x):
        self.pbwheel = x


    def __pbwheel(self, file_location, file_location_2):
        with open(DriveLoc.DriveLocation() + file_location) as list_1, open(DriveLoc.DriveLocation() + file_location_2) as list_2:
            keys = []
            values = []
            contents = list_1.read().splitlines()
            contents_1 = list_2.read().splitlines()
            for i in range(len(contents)):
                keys.extend(contents[i])


            for i in range(len(contents_1)):
                values.extend(contents_1[i])
                pbwheel = dict(zip(keys, values))
                return pbwheel


                #pbwheel_in = dict(zip(keys, values))  # zips the two read lists into a dictionary
                #print(pbwheel_in)


# c = Wheel()


# message = c._Wheel__pbwheel(file, file_2)




def create_message(message):
    print ("Each message is 10 characters long\nRun the program again for additional encryption\n")
    print("***If no more characters are needed, enter a period or a space")
    char1 = input("Enter character: ")
    char2 = input("Enter character: ")
    char3 = input("Enter character: ")
    char4 = input("Enter character: ")
    char5 = input("Enter character: ")
    char6 = input("Enter character: ")
    char7 = input("Enter character: ")
    char8 = input("Enter character: ")
    char9 = input("Enter character: ")
    char10 = input("Enter character: ")
    new_message = (message[char1], message[char2], message[char3], message[char4], message[char5],
                   message[char6], message[char7], message[char8], message[char9], message[char10])
    print("This is your encrypted message")
    return new_message




# print(create_message())




# input("Press 'enter' to end program")

### end ###
