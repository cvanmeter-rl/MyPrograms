#This is the implementation for uniform cost graph search
from array import *
import time
import copy

queue = []
class node:
    def __init__(self,Posx:int,Posy:int,visited:set,path:list,pathCost:int,goalsReached:int,numMoves:int,layout:list):
        #holds the x and y position of the current position
        self.Posx = Posx
        self.Posy = Posy
        #stores already visited nodes
        self.visited = visited
        #holds the current path taken up to this node
        self.path = path
        #value for path cost up to this node
        self.pathCost = pathCost
        #keeps track of the number of goal nodes reached
        self.goalsReached = goalsReached
        #keep track of how many moves made
        self.numMoves = numMoves
        #stores the layout of the clean and dirty floors
        self.layout = layout
def uniformCostGraphSearch(goal,n:node):
    #nodes expanded
    expanded = 0
    #nodes generated
    generated = 1

    #keeps track of number of goal nodes reached
    count = len(goal)

    #graph and cost arrays
    global cost

    #priority queue
    global queue

    #insert starting index
    queue.append(n)
    #used to print state of the first 5 search nodes
    num = 1

    while(len(queue) > 0): #while the queue isnt empty
        #gets the top element in the queue
        queue = sorted(queue,key = lambda a:(a.pathCost,a.Posx,a.Posy),reverse=True)
        #prints the state of the first 5 search nodes
        if num <= 5:
            print("State After Node {0}:".format(num),end="")
            for i in range(len(queue)):
                print('[{0},{1}]'.format(queue[i].Posx,queue[i].Posy),end="")
            print()
        num += 1
        #gets the next node to be expanded
        curr = queue[-1]
        
        #increment nodes expanded and moves
        expanded += 1
        curr.numMoves += 1

        #adds to the path since this node is being expanded
        curr.path.append([curr.Posx,curr.Posy])
        #pops the element from the top
        del queue[-1]
        
        #checks if a dirty/goal room is reached
        if(curr.layout[curr.Posx][curr.Posy] == 1):
            #add the same coordinates to path because we are cleaning dirty room
            curr.path.append([curr.Posx,curr.Posy])
            #increase count of goals reached
            curr.goalsReached += 1
            #increment moves
            curr.numMoves += 1
            #add step cost for cleaning room
            curr.pathCost += 0.6
            #change room to clean
            curr.layout[curr.Posx][curr.Posy] = 0

            #reduces count and if count equals 0 then we have reached all goal rooms
            if(curr.goalsReached == len(goal)):
                return curr,expanded,generated
        #check for non visited nodes which are possible options for the vacuum
        if((curr.Posx,curr.Posy) not in curr.visited):
            curr.visited[(curr.Posx,curr.Posy)] = 1
            generated += expand(curr,curr.layout)
            
    return curr,expanded,generated

def expand(p:node,graph):
    global queue
    generated = 0
    if (p.Posx-1,p.Posy) not in p.visited and p.Posx - 1 >= 0: #checks to see if we can go up
        #creates new node to be inserted and adds it to the queue 
        up = node(int(p.Posx-1),int(p.Posy),p.visited.copy(),p.path.copy(),float(p.pathCost+0.8),int(p.goalsReached),int(p.numMoves),copy.deepcopy(p.layout))
        queue.append(up)
        generated += 1
    if (p.Posx+1,p.Posy) not in p.visited and p.Posx + 1 <= 3: #checks to see if we can move down
        #creates new node to be inserted and adds it to the queue 
        down = node(int(p.Posx+1),int(p.Posy),p.visited.copy(),p.path.copy(),float(p.pathCost+0.7),int(p.goalsReached),int(p.numMoves),copy.deepcopy(p.layout))
        queue.append(down)
        generated += 1
    if (p.Posx,p.Posy-1) not in p.visited and p.Posy - 1 >= 0: #checks if we can move left
        #creates new node to be inserted and adds it to the queue 
        left = node(int(p.Posx),int(p.Posy-1),p.visited.copy(),p.path.copy(),float(p.pathCost+1.0),int(p.goalsReached),int(p.numMoves),copy.deepcopy(p.layout))
        queue.append(left)
        generated += 1
    if (p.Posx,p.Posy+1) not in p.visited and p.Posy + 1 <= 4: #checks if we can move right
        #creates new node to be inserted and adds it to the queue 
        right = node(int(p.Posx),int(p.Posy+1),p.visited.copy(),p.path.copy(),float(p.pathCost+0.9),int(p.goalsReached),int(p.numMoves),copy.deepcopy(p.layout))
        queue.append(right)
        generated += 1
    return generated
if __name__ == '__main__':
    #holds the edges for the graph and what rooms are dirty and not
    graph1 = [[0,1,0,0,0],[0,0,0,1,0],[0,0,0,0,1],[0,0,0,0,0]]
    
    #holds the coordinates for the dirty rooms/goal rooms
    goal1 = [[0,1],[1,3],[2,4]]
    #creates starting node
    n = node(1,1,{},[],0,0,0,graph1)    

    start = time.time()
    res,ex,gen = uniformCostGraphSearch(goal1,n)
    
    print()
    print("CPU Execution Time For Instance #1: ",time.time()-start)
    print("Total Action Cost For Instance #1: ",round(res.pathCost,2))
    print("Nodes Expanded For Instance #1:",ex)
    print("Nodes Generated For Instance #1:",gen)
    print("Number Of Moves For Instance #1:",res.numMoves)
    print("final path For Instance #1: ",res.path,end="\n\n")
    

    #info for instance #2

    #holds the edges for the graph and what rooms are dirty and not
    graph2 = [[0,1,0,0,0],[1,0,0,1,0],[0,0,1,0,0],[0,0,0,0,0]]
    #holds the coordinates for the dirty rooms/goal rooms
    goal2 = [[0,1],[1,0],[1,3],[2,2]]
    #creates starting node
    n = node(2,1,{},[],0,0,0,graph2)

    queue.clear()

    start = time.time()
    res,ex,gen = uniformCostGraphSearch(goal2,n)
    
    print("CPU Execution Time For Instance #2: ",time.time()-start)
    print("Total Action Cost For Instance #2: ",round(res.pathCost,2))
    print("Nodes Expanded For Instance #2:",ex)
    print("Nodes Generated For Instance #2:",gen)
    print("Number Of Moves For Instance #2:",res.numMoves)
    print("final path For Instance #2: ",res.path,end="")
    
