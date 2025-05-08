import heapq

def a_star(graph,start,goal,heuristic):
	open_set=[]
	heapq.heappush(open_set,(0,start))
	
	came_from={}
	
	g_score = {node : float('inf') for node in graph}
	g_score[start]=0
	
	f_score={node : float('inf') for node in graph}
	f_score[start]=heuristic[start]

	while open_set:
		
		_,current = heapq.heappop(open_set)
		
		if current == goal:
			path = []
			while current:
				path.append(current)
				current = came_from.get(current)
			return path[::-1]
		
		for neighbour,weight in graph[current].items():
			tentative_g_score = g_score[current] + weight
			
			if tentative_g_score < g_score[neighbour]:
				came_from[neighbour] = current
				g_score[neighbour] = tentative_g_score
				f_score[neighbour] = g_score[neighbour] + heuristic[neighbour]
				heapq.heappush(open_set,(f_score[neighbour],neighbour))
	return "No path found"


def get_user_input():
    graph = {}
    nodes = input("Enter all nodes separated by spaces: ").split()
    
    for node in nodes:
        graph[node] = {}  # Initialize the dictionary for each node
        neighbors = input(f"Enter neighbors of {node} with weights (a:b format): ").split()
        
        for n in neighbors:
            if ':' in n:  # Check if the format is correct
                try:
                    neighbor, weight = n.split(':')
                    graph[node][neighbor] = int(weight)
                except ValueError:
                    print(f"Invalid format for neighbor {n}. It should be 'A:10'.")
            else:
                print(f"Skipping invalid neighbor format: {n}")

    heuristic = {}
    print("\nEnter heuristic values for each node:")
    
    for node in nodes:
        heuristic[node] = int(input(f"{node}: "))
    
    start = input("\nEnter the start node: ")
    goal = input("Enter the goal node: ")
    return graph, heuristic, start, goal



def main():
	graph,heuristic,start,goal = get_user_input()
	path = a_star(graph,start,goal,heuristic)
	print("shortest path: ",path)
	
if __name__ == "__main__":
	main()