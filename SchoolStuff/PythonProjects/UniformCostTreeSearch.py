# this is the python implementation of uniform cost tree search

import time

end_time = time.time()

# this is our environment class
# this is used to store a 2d array of the rooms and their clean status
class environment:
    def __init__(self, goal_list: list, agent_pos: tuple):
        # first we create the 2d array
        rows = 4
        cols = 5
        arr = [[None for j in range(cols)] for i in range(rows)]

        # next set up the state for each element in the 2d array
        for i in range(0,4):  # loop through the rows
            for j in range(0,5):  # loop through the columns
                coord = (i+1, j+1)
                if str(coord) in goal_list:
                    arr[i][j] = False  # room is dirty
                else:
                    arr[i][j] = True  # room is clean

        # and finally set up a few class variables
        self.env = arr
        self.remaining_goals = goal_list
        self.agent_start = agent_pos
        self.num_goal_nodes = len(goal_list)

    # clones an existing environment, returns the cloned copy
    def clone_environment(self, agent_pos: tuple):
        goal_list = self.remaining_goals.copy()
        new_env = environment(goal_list, agent_pos)
        return new_env

    # changes a room from dirty to clean
    def clean_room(self, coord):
        x = int(coord[0])
        y = int(coord[1])
        self.env[x-1][y-1] = True
        try:
            self.remaining_goals.remove(str(coord))
        except ValueError:
            print("value error")

    # returns the clean status of a room given its coordinate location, True if clean
    def get_clean_status(self, coord):
        x = int(coord[0])
        y = int(coord[1])
        return self.env[x-1][y-1]

# this is the node class, each time a node is generated it is created through this class
class node:
    # set a few variables for the node when creating a new one
    def __init__(self, env: environment, parent, will_suck: bool, pos, move_cost):
        # set the parent node and the depth
        self.parent = parent
        if self.parent is not None:
            self.depth = self.parent.depth + 1
            self.goals_obtained = self.parent.goals_obtained
            self.path_cost = move_cost + self.parent.path_cost
        else:
            self.depth = 1 
            self.goals_obtained = 0
            self.path_cost = move_cost
        
        # then set the clean state and the position in the environment
        self.env = env.clone_environment(pos)
        self.will_suck = will_suck
        self.move_cost = move_cost
        self.pos = pos
        self.children = []
        # children nodes will be set later when this node is expanded

        # if suck action is being performed, render the results of that action in the node
        if self.will_suck == True:
            self.goals_obtained += 1
            self.env.clean_room(self.pos)

    # sets the children for a node, children for a node aren't set until it is expanded
    def set_children(self, children: list):
        for child in children:
            self.children.append(child)

    # sets a node from dirty to clean
    def clean_room(self):
        self.env.clean_room(self.pos)

    # gets the clean state for a node
    def get_clean_state(self):
        return self.env.get_clean_status(self.pos)

# this is a custom priority queue class used in the tree search function
# ties are broken according to hw2 specs
class pqueue:
    def __init__(self, root_node: node):
        # we insert the root node first
        self.queue = []
        self.queue.append(root_node)
        self.len = 1

    # add a node to the queue according to cost, break tie if any
    def enqueue(self, new_node: node):
        # loop through each node already in the queue to insert new_node
        path_cost = new_node.path_cost
        queue_index = -1  # keeps track of where we're at in the queue
        for item in self.queue:
            item_cost = item.path_cost
            queue_index += 1
            if path_cost < item_cost:  # if new node has priority over current node
                break
            elif path_cost == item_cost: # we have a tie, so we break it
                node_pos = new_node.pos
                item_node_pos = item.pos

                # first compare row number, smaller gets priority
                if int(node_pos[0]) < int(item_node_pos[0]):
                    break
                elif int(node_pos[0]) > int(item_node_pos[0]):
                    continue
                else:
                    # then compare column number, if necessary
                    if int(node_pos[1]) < int(item_node_pos[1]):
                        break
                    else:
                        continue
            
        self.queue.insert(queue_index, new_node)
        self.len += 1

    # remove the lowest cost node from the queue
    def dequeue(self):
        move = self.queue.pop(0)
        return move
    
    # return the lowest cost node from the queue without removing it
    def pull(self):
        move = self.queue[0]
        return move
    
    def __len__(self):
        return self.len

# this class is the search tree that is created by searching the environment
# essentially stores stat variables, the queue, root node, and initial state
class searchTree:
    # set the root node when setting up the tree, along with some other stat keeping variables
    def __init__(self, initial_env: environment, root: node, fringe: pqueue):
        self.fringe = fringe
        self.root = root
        self.nodes_expanded = 0
        self.nodes_generated = 0
        self.total_goals = initial_env.num_goal_nodes
        self.final_node = None
        self.first_five = []

    # increment the nodes_expanded
    def inc_nodes_expanded(self, inc = 1):
        self.nodes_expanded += inc

    # increment the nodes_generated
    def inc_nodes_generated(self, inc):
        self.nodes_generated += inc

# our main search function
def uniformCostTreeSearch(env: environment):
    # get the global time variable
    global end_time
    start_time = time.time()

    # get the starting position of the agent and make a node and then the tree
    start_pos = env.agent_start
    root = node(env, None, False, start_pos, 0)
    search_tree = searchTree(env, root, pqueue(root))

    # then we begin our tree searching loop
    count = 0
    fringe = search_tree.fringe
    while len(fringe) != 0:
        # make sure we don't run for over an hour
        end_time = time.time()
        if end_time - start_time > 3600:
            end_time -= start_time
            return search_tree

        # we grab the cheapest cost node and then check if its a goal
        cur_node = fringe.dequeue()

        # make sure to store the first five expanded nodes
        if count < 5:
            search_tree.first_five.append(cur_node)
            count += 1

        # see if the node meets the goal state
        if goal_test(search_tree, cur_node) == True:
            search_tree.final_node = cur_node
            return search_tree

        # expand the current node and add children to queue
        successors = expand(cur_node)
        generated = len(successors)
        search_tree.inc_nodes_generated(generated)
        search_tree.inc_nodes_expanded()
        for successor in successors:
            fringe.enqueue(successor)

    return None

# expands a node and generates its children
def expand(par_node: node):
    successors = []  # list of successor/child nodes
    env = par_node.env  # get the environment state from the parent node
    move_list = successor(par_node) # get all possible actions

    for move in move_list:
        cost, pos = move
        will_suck = False
        if cost == 6:  # if agent will perform suck action
            will_suck = True
        #path_cost = cost + par_node.path_cost
        new_node = node(env, par_node, will_suck, pos, cost)
        successors.append(new_node)
    par_node.set_children(successors)
    return successors

# determines the possible moves for an agent in a particular node
# i.e. move left, right, up, down, and suck
def successor(par_node: node):
    # first we create a list that will hold possible moves from this node
    move_list = []
    coords = par_node.pos
    row = int(coords[0])
    col = int(coords[1])

    # check to see if room is dirty
    if par_node.get_clean_state() == False:
        move_list.append((6, (row, col)))  # append to move list if room is dirty

    # next check to see if agent can move left, right, up, and down
    if col - 1 >= 1:  # checks left
        move_list.append((10, (row, col - 1)))
    if col + 1 <= 5:  # checks right
        move_list.append((9, (row, col + 1)))
    if row - 1 >= 1:  # checks up
        move_list.append((8, (row - 1, col)))
    if row + 1 <= 4:  # checks down
        move_list.append((7, (row + 1, col)))

    return move_list

# evaluates whether we have reached the goal state
# i.e. all rooms are clean at cheapest cost
def goal_test(tree: searchTree, poss_node: node):
    # check to make sure we've found all goals
    goals_obtained = poss_node.goals_obtained
    total_goals = tree.total_goals
    if goals_obtained < total_goals:  # if we haven't found all of the goals yet
        return False
    
    # next check to see if our proposed solution is the cheapest
    path_cost = poss_node.path_cost
    next_node = tree.fringe.pull()
    next_node_cost = next_node.path_cost
    if next_node_cost < path_cost:
        return False
    
    # at this point poss_node is the final node in the cheapest solution in the environment
    return True

# sets up the environments specified in the hw2 handout
def createEnvironments():
    # first set up a list of the dirty rooms  and agent starting position depending on which instance
    dirty_rooms_1 = ["(1, 2)", "(2, 4)", "(3, 5)"]
    agent_pos_1 = (2, 2)
    dirty_rooms_2 = ["(1, 2)", "(2, 1)", "(2, 4)", "(3, 3)"]
    agent_pos_2 = (3, 2)

    # then set up the environment through the environment class
    environment_1 = environment(dirty_rooms_1, agent_pos_1)
    environment_2 = environment(dirty_rooms_2, agent_pos_2)

    return environment_1, environment_2

# prints the results of a uniform cost tree search
def print_results(tree: searchTree, time, phrase):
    # do a few calculations
    fin_node = tree.final_node
    temp_node = fin_node
    first_five = tree.first_five
    seq_list = []
    while(temp_node is not None):
        seq_list.append(temp_node)
        temp_node = temp_node.parent
    moves = len(seq_list) - 1  # must account for the root node
    seq_list.reverse()

    # then print all of the results
    print(phrase)
    print("First five expanded nodes:", end="")
    for node in first_five:
        print(node.pos, end=" ")
    print("")
    print("Nodes expanded:", tree.nodes_expanded)
    print("Nodes generated:", tree.nodes_generated)
    print("Execution time:", time)
    print("The Solution:\n\tSequence: ", end="")
    for sequence in seq_list:
        print(sequence.pos, end=" => ")
    print(" ")
    print("\tNumber of moves:", moves)
    print("\tCost:", fin_node.path_cost / 10)


def main():
    # grab the global time variable
    global end_time
    
    # first create our two environments
    environment_1, environment_2 = createEnvironments()

    # then run tree search on instance 1
    tree_1 = uniformCostTreeSearch(environment_1)
    duration_1 = end_time
    print_results(tree_1, duration_1, "Instance #1:")

    # then run it on instance 2
    tree_2 = uniformCostTreeSearch(environment_2)
    duration_2 = end_time
    print_results(tree_2, duration_2, "Instance #2:")

if __name__ == "__main__":
    main()