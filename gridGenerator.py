import sys

def main():

    size = (int)(sys.argv[1])

    f = open("layouts/randomLayout.lay", "w")

    lay = [[' ' for i in range(size+2)] for j in range(size+2)]

    for i in range(0, size+2):
        for j in range(0, size+2):
            if (i == 0 or j == 0 or i == size+1 or j == size+1):
                lay[i][j] = '%'

    from util import random

    maxHoles = (int)((size*size)/2)
    minHoles = (int)((size*size)/6)

    noOfHoles = random.randint(minHoles, maxHoles)
    holesCnt = 0

    startLocSet = False
    restLocSet = False
    destLocSet = False


    for i in range(1, size+1):
        for j in range(1, size+1):
            if(holesCnt != noOfHoles):
                chance = random.randint(1, 100)
                if(chance < 26): 
                    lay[i][j] = 'H'
                    holesCnt += 1
            else:
                break    
        if(holesCnt == noOfHoles):
            break
            

    while (not startLocSet):
        x = random.randint(1, size+1)
        y = random.randint(1, size+1)
        if lay[x][y] == ' ':
            lay[x][y] = 'P'
            startLocSet = True

    while (not restLocSet):
        x = random.randint(1, size+1)
        y = random.randint(1, size+1)
        if lay[x][y] == ' ':
            lay[x][y] = 'R'
            restLocSet = True

    while (not destLocSet):
        x = random.randint(1, size+1)
        y = random.randint(1, size+1)
        if lay[x][y] == ' ':
            lay[x][y] = 'D'
            destLocSet = True
    
    for i in range(0, size+2):
        for j in range(0, size+2):
            f.write(str(lay[i][j]))
        f.write('\n')                

    f.close()

if __name__ == "__main__":
    main()