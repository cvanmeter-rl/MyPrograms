import time

class VacuumWorld:
    def __init__(self, graph, initial_pos):
        """
        Initializes the vacuum world.
        
        :param graph: A 2D matrix representing the rooms. 1 indicates dirty and 0 indicates clean.
        :param initial_pos: A tuple indicating the starting position of the vacuum.
        """
        self.graph = graph
        self.initial_pos = initial_pos
        self.ROWS = len(graph)
        self.COLS = len(graph[0])
        self.ACTION_COST = {'Left': 1.0, 'Right': 0.9, 'Up': 0.8, 'Down': 0.7, 'Suck': 0.6}
        self.nodes_expanded = 0
        self.nodes_generated = 0
        self.first_5_states = []

    def is_goal_state(self, state, goal):
        """
        Checks if the current state is the goal state.
        
        :param state: The current state of the rooms.
        :param goal: A list of dirty room positions.
        :return: True if all goal rooms are clean, False otherwise.
        """
        for g in goal:
            if state[g[0]][g[1]] == 1:
                return False
        return True

    def get_neighbors(self, row, col):
        """
        Fetches the neighboring cells to the current position.
        
        :param row: Current row position.
        :param col: Current column position.
        :return: List of neighboring cells with direction.
        """
        neighbors = []
        if row > 0:
            neighbors.append((row-1, col, 'Up'))
        if row < self.ROWS - 1:
            neighbors.append((row+1, col, 'Down'))
        if col > 0:
            neighbors.append((row, col-1, 'Left'))
        if col < self.COLS - 1:
            neighbors.append((row, col+1, 'Right'))
        return neighbors

    def dls(self, current_state, current_pos, goal, depth):
        """
        Depth limited search algorithm.
        
        :param current_state: The current state of the rooms.
        :param current_pos: The current position of the vacuum.
        :param goal: List of goal rooms.
        :param depth: The current depth.
        :return: Boolean indicating success, the path, and the total cost.
        """
        if depth == 0 and self.is_goal_state(current_state, goal):
            return True, [], 0
        if depth <= 0:
            return False, [], 0

        self.nodes_expanded += 1

        # Record the first 5 states expanded
        if len(self.first_5_states) < 5:
            self.first_5_states.append((current_state, current_pos))

        row, col = current_pos
        total_cost = 0

        for nr, nc, action in self.get_neighbors(row, col):
            self.nodes_generated += 1
            updated_state = [row[:] for row in current_state]
            if updated_state[nr][nc] == 1:
                updated_state[nr][nc] = 0
                found, path, cost = self.dls(updated_state, (nr, nc), goal, depth-1)
                if found:
                    total_cost += self.ACTION_COST[action] + self.ACTION_COST['Suck']
                    return True, [(nr, nc, 'Suck')] + [(nr, nc, action)] + path, total_cost + cost
            else:
                found, path, cost = self.dls(updated_state, (nr, nc), goal, depth-1)
                if found:
                    total_cost += self.ACTION_COST[action]
                    return True, [(nr, nc, action)] + path, total_cost + cost

        return False, [], total_cost

    def iddfs(self, goal, max_depth):
        """
        Iterative deepening depth-first search algorithm.
        
        :param goal: List of goal rooms.
        :param max_depth: The maximum depth for the search.
        :return: The solution path and its cost.
        """
        for depth in range(max_depth):
            found, path, cost = self.dls(self.graph, self.initial_pos, goal, depth)
            if found:
                return path[::-1], cost
        return [], 0

if __name__ == '__main__':
    # First instance
    graph1 = [[0,1,0,0,0],[0,0,0,1,0],[0,0,0,0,1],[0,0,0,0,0]]
    goal1 = [(0,1),(1,3),(2,4)]
    world1 = VacuumWorld(graph1, (1, 1))

    start = time.time()
    path, cost = world1.iddfs(goal1, 10)
    duration = time.time() - start

    # Display results for instance 1
    print("CPU Execution Time For Instance #1:", duration)
    print("First 5 states expanded:", world1.first_5_states)
    print("Total Nodes Expanded:", world1.nodes_expanded)
    print("Total Nodes Generated:", world1.nodes_generated)
    print("Solution Path:", path)
    print("Number of Moves:", len(path))
    print("Solution Cost:", cost)
    print()

    # Second instance
    graph2 = [[0,1,0,0,0],[1,0,0,1,0],[0,0,1,0,0],[0,0,0,0,0]]
    goal2 = [(0,1),(1,0),(1,3),(2,2)]
    world2 = VacuumWorld(graph2, (2, 1))

    start = time.time()
    path, cost = world2.iddfs(goal2, 10)
    duration = time.time() - start

    # Display results for instance 2
    print("CPU Execution Time For Instance #2:", duration)
    print("First 5 states expanded:", world2.first_5_states)
    print("Total Nodes Expanded:", world2.nodes_expanded)
    print("Total Nodes Generated:", world2.nodes_generated)
    print("Solution Path:", path)
    print("Number of Moves:", len(path))
    print("Solution Cost:", cost)
