import xlsxwriter
import csv
import openpyxl
from pathlib import Path
import shutil
import os
my_working_directory = os.getcwd()

def trashFiles(path, num = 0):
    trashpath = my_working_directory + '\TrashFiles\_' + str(num) + '.xlsx'
    try:
        os.rename(path, trashpath)
        print('Sha guardat amb el nom "' + '\_' + str(num) + '.xlsx"!')
    except:
        trashFiles(path, num + 1)

def createFile(nameFile, data, dir = '\Data'):

    # create file and write data on it
    numCol = 'A'
    numRow = 1

    file = xlsxwriter.Workbook('_' + nameFile + '.xlsx')

    fileSheet = file.add_worksheet()

    lenFile = 0

    for row in data:
        for elem in row:
            fileSheet.write(numCol + str(numRow), elem)
            numCol = chr(ord(numCol) + 1)
        numRow += 1
        numCol = 'A'
        lenFile += 1
    
    file.close()

    # move file to Data folder
        
    path = str(my_working_directory + '\_' + nameFile + '.xlsx')
    newpath = str(my_working_directory + str(dir) + '\_' + nameFile + '.xlsx')
    try:
        os.rename(path, newpath)
    except:
        print('Ja existeix un arxiu amb el nom: "' + nameFile + '"')
        trashFiles(path)
        
    return lenFile
