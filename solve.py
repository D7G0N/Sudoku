import copy
import random

BLANK = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
]

ORG = [
    [2, 9, 5, 3, 1, 4, 6, 8, 7],
    [3, 7, 8, 2, 5, 6, 1, 4, 9],
    [1, 6, 4, 8, 7, 9, 5, 3, 2],
    [6, 4, 9, 7, 8, 5, 3, 2, 1],
    [8, 3, 7, 6, 2, 1, 4, 9, 5],
    [5, 1, 2, 4, 9, 3, 8, 7, 6],
    [9, 8, 6, 1, 4, 7, 2, 5, 3],
    [7, 2, 3, 5, 6, 8, 9, 1, 4],
    [4, 5, 1, 9, 3, 2, 7, 6, 8]
]

def printSudoku(s):
    line = ''
    if type(s) != list or type(s[0]) != list or len(s) != 9:
        line += 'ERROR'
        return line
    for i in range(9):
        if i % 3 == 0:
            line += " -" * 12 + '\n'
            print(" -" * 12) 
        for j in range(9):
            if j % 3 == 0:
                line += "| "
                print("| ", end = '') 
            if s[i][j] == 0:
                line += '  '
                print(" ", end = ' ') 
            else:
                line += str(s[i][j]) + ' '
                print(s[i][j], end = ' ') 
        line += '|\n'
        print('|') 
    line += " -" * 12 + '\n'
    print(" -" * 12) 

    return line

def getBlock(s, t: tuple):
    r, c = t
    block_r = int(r / 3) * 3
    block_c = int(c / 3) * 3

    block = []
    for i in range(3):
        block += s[block_r + i][block_c : block_c + 3]
    
    return block

def checkChange(s: list, n: int, t: tuple):
    r, c = t
    
    if s[r][c] != 0:
        #print('f0')
        return False

    if n in s[r]:
        #print('fr')
        return False
    
    for row in s:
        if row[c] == n:
            #print('fc')
            return False
    
    if n in getBlock(s, t):
        #print('fb')
        #print(t)
        #print(getBlock(s, t))
        return False

    #print("t")
    return True

def solveBlock(s):
    for each in range(9):
        block_r = int(each / 3) * 3
        block_c = (each % 3) * 3
        t = (block_r, block_c)
        block = getBlock(s, t)

        for n in range(1, 10):
            if n not in block:
                new = -1
                mem = []
                for place in range(9):
                    if block[place] == 0:
                        r = block_r + int(place / 3)
                        c = block_c + (place % 3)
                        if checkChange(s, n, (r, c)):
                            if new == -1:
                                new = place
                                mem = [r, c]
                            else:
                                new = 10
                if new != -1 and new != 10:
                    block[new] = n
                    s[mem[0]][mem[1]] = n

def solveCol(s):
    for c in range(9):
        for n in range(1,10):
            col = [row[c] for row in s] 
            if n not in col:
                new = -1
                mem = []
                for r in range(9):
                    if col[r] == 0:
                        if checkChange(s, n, (r, c)):
                            if new == -1:
                                new = r
                                mem = [r, c]
                            else:
                                new = 10
                if new != -1 and new != 10:
                    col[new] = n
                    r, c = mem
                    s[r][c] = n  

def solveRow(s):
    for r in range(9):
        for n in range(1, 10):
            row = s[r]
            if n not in row:
                new = -1
                mem = []
                for c in range(9):
                    if row[c] == 0:
                        if checkChange(s, n, (r, c)):
                            if new == -1:
                                new = c
                                mem = [r, c]
                            else:
                                new = 10
                if new != -1 and new != 10:
                    row[new] = n
                    r, c = mem
                    s[r][c] = n  

def listToMatrix(l):
    m = []
    for i in range(9):
        m.append(l[i * 9: i + 9])

def solve(alt):
    for t in range(5):
        solveBlock(alt)
        solveCol(alt)
        solveRow(alt)
        
        all = [each for row in alt for each in row]
        if 0 not in all:
            #print('done')
            return True
    return False
        
def simplify(s):
    nums = list(range(81))
    random.shuffle(nums)
    for n in nums:
        r = int(n / 9)
        c = n % 9
        if s[r][c] != 0:
            n = s[r][c]
            s[r][c] = 0
            if solve(copy.deepcopy(s)):
                #print(True)
                ''
            else:
                s[r][c] = n
    return s

def score(s):
    flat = [each for row in s for each in row]
    score = 0
    for each in flat:
        if each != 0:
            score += 1
    return score

def mostSimple(s):
    min = 100
    ms = []
    for each in range(20):
        alt = copy.deepcopy(s)
        simplify(alt)
        sc = score(alt)
        #print(sc, end = ', ')
        if sc < min:
            min = sc
            ms = copy.deepcopy(alt)
    #print(' ')
    return ms

def add(s):
    solve(s)
    flat = [each for row in s for each in row]
    start = random.randint(0, 80)
    i = start
    while flat[i] != 0:
        i += 1
        if i >= 81:
            i = 0
        if i == start:
            return('done')

    for n in range(1, 10):
        r = int(i / 9)
        c = i % 9 
        if checkChange(s, n, (r, c)):
            s[r][c] = n
            break

def create():
    alt = copy.deepcopy(BLANK)
    while 0 in [each for row in alt for each in row]:
        past = copy.deepcopy(alt)
        add(alt)
        if past == alt:
            alt = copy.deepcopy(BLANK)
        printSudoku(alt)
    return alt


def main():
    #alt = copy.deepcopy(ORG)
    #solve(alt)
    alt = create()
    alt = mostSimple(alt)
    #printSudoku(ORG)
    printSudoku(alt)

#main()