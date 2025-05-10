def a_star(graph, start, goal, heuristic): 
    frontier = [start]  # list of nodes to explore 
    cost_so_far = {start: 0}  # cost from start to each node 
    came_from = {start: None}  # for reconstructing path 
 
    while frontier: 
        # Select node with lowest f(n) = g(n) + h(n) 
        current = min(frontier, key=lambda node: cost_so_far[node] + 
heuristic[node]) 
 
        if current == goal: 
            break  # goal reached 
 
        frontier.remove(current) 
 
        for neighbor, cost in graph[current]: 
            new_cost = cost_so_far[current] + cost  # g(n) 
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]: 
                cost_so_far[neighbor] = new_cost 
                came_from[neighbor] = current 
                if neighbor not in frontier: 
                    frontier.append(neighbor) 
 
    # Reconstruct path from goal to start 
    path = [] 
    current = goal 
    while current is not None: 
        path.append(current) 
        current = came_from[current] 
    path.reverse() 
 
    return path, cost_so_far[goal] 
 
 
 
# Sample graph and heuristic 
graph = { 
'S': [('A', 2), ('C', 12)], 
'A': [('B', 2), ('C', 1)], 
'B': [('D', 5)], 
'C': [('D', 3), ('G', 4)], 
'D': [('G', 4)], 
'G': [] 
} 
heuristic = {'S': 5, 'A': 3, 'B': 4, 'C': 2, 'D': 6, 'G': 0} 
# Run A* Search 
start_node = 'S' 
goal_node = 'G' 
path, cost = a_star(graph, start_node, goal_node, heuristic) 
print("Path:", path) 
print("Total cost:", cost)