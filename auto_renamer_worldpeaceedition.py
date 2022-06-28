#FYEO AGENT CF88 !!!

import os

folderPath = input("Enter folder path: ")
fileNumber = int(input("Enter starting point of numbering: "))
fileFormat = input("Enter the file format (without the .): ")
extraTextFlag = int(input("Would you like to add some extra text after the num? 0 for no (ie. only number) 1 for yes: "))

if extraTextFlag == 0:
    for filename in os.listdir(folderPath):
        os.rename(folderPath + '\\' + filename, folderPath + '\\' + str("%03d" % (fileNumber,)) + '.' + fileFormat)
        fileNumber += 1
elif extraTextFlag == 1:
    extraText = input("Enter the extra text: ")
    for filename in os.listdir(folderPath):
        os.rename(folderPath + '\\' + filename, folderPath + '\\' + str("%03d" % (fileNumber,)) + extraText + '.' + fileFormat)
        fileNumber += 1
else:
    print("Something is wrong Yoru-san XD haha jk unless????!!!!")
