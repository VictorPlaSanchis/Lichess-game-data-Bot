################################################################################
#                                                                              #
#   Victor Pla i Oriol Jariod : 04 / 04 / 2021                                 #
#                                                                              #
#   Bot per al B7 de l'assignatura de PE a la FIB.                             #
#                                                                              #
#   Ús:                                                                        #
#                                                                              #
#       Input => Hi han 4 parametres de input                                  #
#       1. Nom del arxiu on es guardaran les dades a recollir                  #
#       2. Nivell minim dels jugadors blancs en les partides                   #
#       3. Nivell maxim dels jugadors blancs en les partides                   #
#       4. Tipus de partida ( Bullet, Rapid, Classic )                         #
#                                                                              #
#       Ouput => l'output esta generat i guardat en un arxiu 'xlsx' on cada    #
#       fila de la matriu es una partida recollida                             #
#                                                                              #
################################################################################

# next one: 00_05_04_21_R_1400_1900
# next:     00_05_04_21_C_1400_1900
# next:     00_05_04_21_B_0600_1400
# next:     00_05_04_21_R_0600_1400
# next:     00_05_04_21_C_0600_1400
# next:     01_...

import DataJoinner
import DataController
import DataCollector
import sys

def program(exitCode = 0):
    
    print("program ended with exit code "+str(exitCode))
    answer = input()

def main():

    try:

        nomArxiu = None
        eloMin = None
        eloMax = None
        tipus = None

        if len(sys.argv) > 1:

            #XX_DD_MM_YY_T_ELOm_ELOM
            # shorter way via value argument

            nomArxiu = str(sys.argv[1])
            eloMin = str(sys.argv[1][14:18])
            eloMax = str(sys.argv[1][19:])
            tipus = str(sys.argv[1][12])

            print(nomArxiu, eloMin, eloMax, tipus)

        else:

            print('Digues el nom de larxiu:')
            nomArxiu = str(input())
            print('Digues elo min:')
            eloMin = int(input())
            print('Digues elo max:')
            eloMax = str(input())
            print('Digues tipus partida: [B:Bullet, R:Rapid, C:Classic]')
            tipus = str(input())

        header = ['nom blanc', 'nom negre', 'elo blanc','elo negre','obertura','resultat']

        dades = []
        dades.append(header)

        dataLichess = DataCollector.getData(eloMin, eloMax, tipus)
        
        if dataLichess == -1:
            return -1

        for elem in dataLichess:
            dades.append(elem)

        DataController.createFile(nomArxiu, dades)

        return 0
    
    except:

        return -1

if __name__ == "__main__":
    program(main())