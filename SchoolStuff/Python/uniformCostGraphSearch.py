from array import *
import time

queue = []

def uniformCostGraphSearch(goal,startR,startC,graph):
    #nodes expanded
    expanded = 0
    #nodes generated
    generated = 0
    #number of moves
    moves = 0
    num = 1

    #holds cost
    stepCost = 0.0

    #keeps track of number of goal nodes reached
    count = len(goal)

    #graph and cost arrays
    global cost

    #row and column of current node
    r = startR
    c = startC

    #stores visited nodes
    visited = {}

    #priority queue
    global queue,path

    #insert starting index
    queue.append([startR,startC])

    while(len(queue) > 0): #while the queue isnt empty
        #gets the top element in the queue
        queue = sorted(queue,key = lambda a:(cost[a[0],a[1]],a[0],a[1]),reverse=True)
        if num <= 5:
             print("State After Node {0}:{1}".format(num,queue))
             num += 1
        n = queue[-1]
        #increment nodes expanded, generated, and moves
        expanded += 1
        generated += 1
        moves += 1

        r = n[0]
        c = n[1]

        path.append([r,c])
        #pops the element from the top
        del queue[-1]
        #adds step cost for current node
        stepCost += cost[n[0],n[1]]
        #checks if a dirty/goal room is reached
        if(graph[n[0]][n[1]] == 1):
            #increase cost because we clean room and add it to step
            stepCost += 0.6
            path.append(n)
            #increment moves
            moves +=1
            #change room to clean
            graph1[n[0]][n[1]] = 0

            #reduces count and if count equals 0 then we have reached all goal rooms
            count -= 1
            if(count == 0):
                return stepCost,expanded,generated,moves
        #check for non visited nodes which are possible options for the vacuum
        if((r,c) not in visited):
            generated += expand(n[0],n[1],visited)
        #marks node as visited
        visited[(r,c)] = 1
    return stepCost,expanded,generated,moves

def expand(row,col,visited):
    global queue
    generated = 0
    if (row-1,col) not in visited and [row-1,col] not in queue and row - 1 >= 0: #checks to see if we can go up
        queue.append([row-1,col])
        cost[(row-1,col)] = 0.8
        generated += 1
    if (row+1,col) not in visited and [row+1,col] not in queue and row + 1 <= 3: #checks to see if we can move down
        queue.append([row+1,col])
        cost[(row+1,col)] = 0.7
        generated += 1
    if (row,col-1) not in visited and [row,col-1] not in queue and col - 1 >= 0: #checks if we can move left
        queue.append([row,col-1])
        cost[(row,col-1)] = 1.0
        generated += 1
    if (row,col+1) not in visited and [row,col+1] not in queue and col + 1 <= 4: #checks if we can move right
        queue.append([row,col+1])
        cost[(row,col+1)] = 0.9
        generated += 1
    return generated
if __name__ == '__main__':
    #holds cost values for each edge
    cost = {}
    #holds the edges for the graph and what rooms are dirty and not
    graph1 = [[0,1,0,0,0],[0,0,0,1,0],[0,0,0,0,1],[0,0,0,0,0]]
    
    #holds the coordinates for the dirty rooms/goal rooms
    goal1 = [[0,1],[1,3],[2,4]]
    cost[(1,1)] = 0

    #holds path values traversed
    path = []
    start = time.time()
    res,ex,gen,moves = uniformCostGraphSearch(goal1,1,1,graph1)
    
    print("CPU Execution Time For Instance #1: ",time.time()-start)
    print("Total Action Cost For Instance #1: ",round(res,2))
    print("Nodes Expanded For Instance #1:",ex)
    print("Nodes Generated For Instance #1:",gen)
    print("Number Of Moves For Instance #1:",moves)
    print("final path For Instance #1: ",path,end="\n\n")


    #info for instance #2
    graph2 = [[0,1,0,0,0],[1,0,0,1,0],[0,0,1,0,0],[0,0,0,0,0]]
    cost.clear()
    cost[(2,1)] = 0
    goal2 = [[0,1],[1,0],[1,3],[2,2]]

    path.clear()
    queue.clear()

    start = time.time()
    res,ex,gen,moves = uniformCostGraphSearch(goal2,2,1,graph2)
    
    print("CPU Execution Time For Instance #2: ",time.time()-start)
    print("Total Action Cost For Instance #2: ",round(res,2))
    print("Nodes Expanded For Instance #2:",ex)
    print("Nodes Generated For Instance #2:",gen)
    print("Number Of Moves For Instance #2:",moves)
    print("final path For Instance #2: ",path,end="")
    
