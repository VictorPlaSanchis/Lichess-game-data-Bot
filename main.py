import DataController
import DataCollector

def program(exitCode = 0):
    
    print("program ended with exit code "+str(exitCode))

    while(input()):
        exit()

def main():

    print('Digues el nom de larxiu:')
    nomArxiu = str(input())
    print('Digues elo min:')
    eloMin = int(input())
    print('Digues elo max:')
    eloMax = str(input())
    print('Digues tipus partida: [B:Bullet, R:Rapid, C:Classic]')
    tipus = str(input())

    header = ['data', 'nom blanc', 'nom negre', 'elo blanc','elo negre','obertura','resultat']

    dades = []
    dades.append(header)

    dataLichess = DataCollector.getData(eloMin, eloMax, tipus, 10)
    
    if dataLichess == -1:
        return -1

    for elem in dataLichess:
        dades.append(elem)

    DataController.createFile(nomArxiu, dades)

    return 0

if __name__ == "__main__":
    
    program(main())