import pandas
import DataController
import numpy as np
import os
import sys
my_working_directory = os.getcwd()

def getContent(files):

    data = []

    for fileName in files:
        dfs = pandas.read_excel(str(my_working_directory) + str(fileName) + '.xlsx', sheet_name=None)
        dataFile = np.array([dfs[i] for i in dfs])
        
        for matrix in dataFile:
            for row in matrix:
                data.append(row)

    return data

def joinData(nameJoinedFile, filesToJoin, dir = '\JoinedData'):

    return DataController.createFile(str(nameJoinedFile),getContent(filesToJoin),'\JoinedData')

if __name__ == '__main__':

    if len(sys.argv) > 1:

        try:

            dataToJoin = []

            for argv in sys.argv[1:]:
                dataToJoin.append(argv)

            print('Nom del arxiu compost:')
            nameFile = str(input())

            lenFile = joinData(nameFile,dataToJoin)
            print('Mida total del arxiu compost ' + str(lenFile) + ' columnes/dades/partides.')
        
        except:

            print('Hi ha hagut un problema alhora de trobar els arxius. Exit code -1')
        
        answer = input()
    