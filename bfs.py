graph = {
    '10': ['2', '4', '6', '8'],
    '6': ['11'],
    '4': ['1'],
    '2': ['5', '3'],
    '5': ['9'],
    '3': ['7']
}

visited = set()

def dfs(visited, graph, vertex):
    if vertex not in visited:
        print(vertex, end=" ")
        visited.add(vertex)
        for neighbor in graph.get(vertex, []):
            dfs(visited, graph, neighbor)

dfs(visited, graph, '2')
