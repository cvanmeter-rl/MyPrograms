import copy
import time

num = 0

#this function prints the sudoku grid
def print_grid(arr):
    for i in range(9):
        for j in range(9):
            print (arr[i][j], end = " "),
        print ()
    print()
#this function takes a domain,grid,chosen val and its row and col and returns 0 if the choice is invalid and 1 if the choice is valid
def forwardCheck(domain,grid,val,row,col):
    #check rows and makes sure the val choice is valid
    for i in range(9):
        if i == row:
            continue
        if grid[i][col] == 0:
            v = domain[(i,col)]
            if len(v) == 1 and v[0] == val:
                return 0
    #check columns and makes sure the val choice is valid
    for j in range(9):
        if j == col:
            continue
        if grid[row][j] == 0:
            v = domain[(row,j)]
            if len(v) == 1 and v[0] == val:
                return 0
    #checks the 3x3 region the square is in and makes sure the choice is valid       
    boxRow = row // 3 * 3
    boxCol = col // 3 * 3
    for i in range(boxRow,boxRow+3):   
        for j in range(boxCol,boxCol+3):
            if i == row and j == col:
                continue
            if grid[i][j] == 0:
                v = domain[(i,j)]
                if len(v) == 1 and v[0] == val:
                    return 0
    return 1

#this function takes a list of the cells with the same mrv and finds the cell with the highest degree and returns it
def getDegreeHeuristic(mrvCells,grid):
    maxDegree = -1
    maxDegreeCells = []
    for cell in mrvCells:
        d = getDegreeForCell(cell,grid)
        if d == maxDegree:
            maxDegreeCells.append(cell)
        elif d > maxDegree:
            maxDegreeCells.clear()
            maxDegreeCells.append(cell)
            maxDegree = d

    return maxDegreeCells

#this function takes a cell and calculates its degree heuristic
def getDegreeForCell(cell,grid):
    row = cell[0]
    col = cell[1]

    degree = 0
    #calculates degree for column
    for i in range(9):
        if i == row:
            continue
        if grid[i][col] == 0:
            degree += 1

    #calculates degree for row
    for j in range(9):
        if j == col:
            continue
        if grid[row][j] == 0:
            degree += 1

    #calculates degree for 3x3 square the cell is in 
    boxRow = row // 3 * 3
    boxCol = col // 3 * 3

    for i in range(boxRow,boxRow+3):
        for j in range(boxCol,boxCol+3):
            if i == row and j == col:
                continue
            if grid[i][j] == 0:
                degree += 1

    return degree

#this function takes the list of empty cells and a dictionary of domains and returns a list of the cells with the lowest MRV
def minRemVal(emptyCells,domains):
    minCells = []
    minValues = float('inf')

    for cell in emptyCells:
        val = domains[cell]
        if len(val) == minValues:
            minCells.append(cell)
        elif len(val) < minValues:
            minCells.clear()
            minCells.append(cell)
            minValues = len(val)
    return minCells

#this function takes a sudoku grid and returns a list of the empty cells
def getEmptyCells(grid):
    emptyCells = []
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                emptyCells.append((i,j))
    return emptyCells

#this function figures out the domain of possible values for each empty cell, returns dictionary of domains for the grid
def getDomainForSudoku(grid):
    emptyCells = getEmptyCells(grid)
    domain = {}
    for cell in emptyCells:
        domain[cell] = getPossibleValues(grid,cell[0],cell[1])
    return domain
#returns a list of possible values for a given location on the sudoku puzzle
def getPossibleValues(grid,row,col):
    #possible values are 1-9
    values = set(range(1,10))
    #check the rows
    for c in range(9):
        if grid[row][c] in values:
            values.remove(grid[row][c])
    #check the columns
    for r in range(9):
        if grid[r][col] in values:
            values.remove(grid[r][col])
    #check the 3x3 box that the location is in
    boxRow = (row // 3) * 3
    boxCol = (col // 3) * 3
    for i in range(boxRow,boxRow + 3):
        for j in range(boxCol,boxCol + 3):
            if grid[i][j] in values:
                values.remove(grid[i][j])
    return list(values)

#this function uses forward checking and backtracking using MRV and degree heuristic
def solveSudoku(grid):
    global num
    #gets a list of empty cells
    emptyCells = getEmptyCells(grid)

    #no cells left so we are done solving
    if len(emptyCells) == 0:
        print_grid(grid)
        return 1
    #get domain and figure out mrv
    domain = getDomainForSudoku(grid)
    mrvList = minRemVal(emptyCells,domain)

    #if there are no ties in the mrv calculation
    if len(mrvList) == 1:
        cell = mrvList[0]
    else:
        #get the degree heuristic for the cells
        degreeList = getDegreeHeuristic(mrvList,grid)
        cell = degreeList[0]
    
    row = cell[0]
    col = cell[1]
    #get list of possible values for the cell
    valList = domain[cell]

    while len(valList) != 0:
        val = valList[0]
        del valList[0]
        if forwardCheck(domain,grid,val,row,col):
            grid[row][col] =  val
            if num < 4:
                print("Assignment ",num+1)
                print("Variable Selected: (%d,%d)" % (row,col))
                print("Domain: ",valList)
                print("Degree: ",getDegreeForCell((row,col),grid))
                print("Value Assigned:",val,end="\n\n")
                num += 1
            if solveSudoku(grid):
                return 1
            else:
                grid[row][col] = 0
    return 0

if __name__ == '__main__':
    #for the board a 0 represents an empty cell
    grid1 = [[0,0,1,0,0,2,0,0,0],
            [0,0,5,0,0,6,0,3,0],
            [4,6,0,0,0,5,0,0,0],
            [0,0,0,1,0,4,0,0,0],
            [6,0,0,8,0,0,1,4,3],
            [0,0,0,0,9,0,5,0,8],
            [8,0,0,0,4,9,0,5,0],
            [1,0,0,3,2,0,0,0,0],
            [0,0,9,0,0,0,3,0,0]]
    
    grid2 = [[0,0,5,0,1,0,0,0,0],
            [0,0,2,0,0,4,0,3,0],
            [1,0,9,0,0,0,2,0,6],
            [2,0,0,0,3,0,0,0,0],
            [0,4,0,0,0,0,7,0,0],
            [5,0,0,0,0,7,0,0,1],
            [0,0,0,6,0,3,0,0,0],
            [0,6,0,1,0,0,0,0,0],
            [0,0,0,0,7,0,0,5,0]]
    
    grid3 = [[6,7,0,0,0,0,0,0,0],
            [0,2,5,0,0,0,0,0,0],
            [0,9,0,5,6,0,2,0,0],
            [3,0,0,0,8,0,9,0,0],
            [0,0,0,0,0,0,8,0,1],
            [0,0,0,4,7,0,0,0,0],
            [0,0,8,6,0,0,0,9,0],
            [0,0,0,0,0,0,0,1,0],
            [1,0,6,0,5,0,0,7,0]]
    start = time.time()
    domain = getDomainForSudoku(grid1)
    solveSudoku(grid1)
    print("CPU Execution Time: ",time.time()-start,end="\n\n")
    num = 0

    start = time.time()
    domain = getDomainForSudoku(grid2)
    solveSudoku(grid2)
    print("CPU Execution Time: ",time.time()-start,end="\n\n")
    num = 0

    start = time.time()
    domain = getDomainForSudoku(grid3)
    solveSudoku(grid3)
    print("CPU Execution Time: ",time.time()-start)