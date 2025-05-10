from collections import deque
def create_graph():
    graph={}
    edges = int(input('no. of edges: '))
    for _ in range(edges):
        u,v = input('Enter edge (u v): ').split()
        if u not in graph:
            graph[u]=[]
        if v not in graph:
            graph[v]=[]
        graph[u].append(v)
        graph[v].append(u)
    return graph


def bfs(graph,start):
    visited = set()
    queue = deque([start])
    result=[]
    
    while queue:
        current = queue.popleft()
        if current not in visited:
            result.append(current)
            visited.add(current)
        
        for neighbours in graph[current]:
            if neighbours not in visited:
                queue.append(neighbours)
    return result

def dfs(graph,start):
    visited=set()
    stack=[start]
    result=[]
    while stack:
        current = stack.pop()
        if current not in visited:
            result.append(current)
            visited.add(current)
            for neighbours in reversed(graph[current]):
                if neighbours not in visited:
                    stack.append(neighbours)
    return result
    

def main():
    graph = create_graph()
    while True:
        print('1. BFS\n2. DFS\n3. Exit')
        choice = int(input('Enter your choice: '))  
        if choice == 1:
            start = input('Enter starting node: ')
            print('BFS:',bfs(graph,start))
        elif choice == 2:
            start = input('Enter starting node: ')
            print('DFS:',dfs(graph,start))
        elif choice == 3:
            break
        else:
            print('Invalid choice!')
    print('Exiting...')


if __name__ == "__main__":
    main()