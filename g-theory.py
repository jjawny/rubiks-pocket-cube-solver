graph = {'A': ['B', 'C'],
         'B': ['D', 'A', 'E'],
         'C': ['F', 'A'],
         'D': ['B'],
         'E': ['B', 'F'],
         'F': ['E', 'C']}

#if 'F' in graph:
#    print(graph['F'])
#    print(graph['F'][0])

#    print("works")

visited = set() # Set to keep track of visited nodes.



def bfs(graph, start, end):
    # maintain a queue of paths
    queue = []
    # push the first path into the queue
    queue.append([start])
    while queue:
        # get the first path from the queue
        path = queue.pop(0)
        # get the last node from the path
        node = path[-1]
        # path found
        if node == end:
            return path
        # enumerate all adjacent nodes, construct a new path and push it into the queue
        for adjacent in graph.get(node, []):
            new_path = list(path)
            new_path.append(adjacent)
            queue.append(new_path)


yeet = bfs(graph, 'A', 'F')
#print(yeet)
s = set(yeet)
#print(s)

e = (("lass","gass"), ("ass","pass"))
for eee in e:
    print(eee[0])


