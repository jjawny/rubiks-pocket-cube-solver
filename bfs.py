# Since there are ~3.6 million (3,674,160) possible permutations, performance is crucial.
# Best performing Breadth-first search algorithm from https://stackoverflow.com/a/50575971
# Non-recursive since recursion ran slower. The following still keeps track of visited vertices.
def breadthFirst(graph, start, end):
    """
    Breadth-first search algorithm to find the shortest path from the solved cube to the instance.

    :param: graph: cube group where edges are cubes related via a quater turn
    :param: start: solved cube
    :param: end: instance cube
    :returns: smallest list of vertices from the graph (cubes)
    """

    queue = [(start,[start])]
    visited = set()

    print("Performing a Breadth-first search traversal...\n")

    while queue:
        vertex, path = queue.pop(0)
        visited.add(vertex)

        for node in graph[vertex]:
            if node == end: return path + [end]
            elif node not in visited:
                    visited.add(node)
                    queue.append((node, path + [node]))
                    