import random
from copy import deepcopy

def init(rows,columns, seed = None):
    #procedural generation
    random.seed(seed)
    matrix = [[0 for col in range(columns)] for row in range(rows)]
    
    for x in range(rows):
        for y in range(columns):
            if False and (x == 0 or x == rows-1 or y == 0 or y == columns-1):
                matrix[x][y] = 2
            else:
                if random.randint(0,1) == 0: 
                    matrix[x][y] = 1
                else:
                    matrix[x][y] = 0
    return matrix

def cave(matrix, generations, seed = None):
    random.seed(seed)
    replacement = []
    for z in range(generations):
        replacement = [[2 for col in range(len(matrix))] for row in range(len(matrix[0]))]
        for x in range(1,len(matrix)-1):
            for y in range(1,len(matrix[0])-1):
                total = -matrix[x][y]
                for a in range(x-1,x+2):
                    for b in range(y-1,y+2):
                        total += matrix[a][b]
                if total > 5:
                    replacement[x][y] = 2
                elif total == 4:
                    replacement[x][y] = 3
                elif total == 3:
                    replacement[x][y] = 1
                elif total < 2:
                    replacement[x][y] = 0
                else:
                    replacement[x][y] = matrix[x][y]
        replacement[len(matrix)/2][len(matrix[0])/2] = 0 
        matrix = deepcopy(replacement)
    return replacement
