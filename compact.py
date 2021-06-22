class IllegalCube(Exception): pass



def breadthFirst(graph, start, end):
    queue = [(start,[start])]; visited = set(); print("Performing a Breadth-first search traversal...\n")
    while queue:
        vertex, path = queue.pop(0); visited.add(vertex)
        for node in graph[vertex]: 
            if node == end: return path + [end]
            elif node not in visited: visited.add(node); queue.append((node, path + [node]))



def solution(instance):
    solvedCube = "WWWWGGGGRRRRBBBBOOOOYYYY"; instance = instance.upper(); legalMoves = [[0,1,7,5,4,20,6,21,10,8,11,9,2,13,3,15,16,17,18,19,14,12,22,23], [0,1,12,14,4,3,6,2,9,11,8,10,21,13,20,15,16,17,18,19,5,7,22,23], [0,1,2,3,4,5,18,19,8,9,6,7,12,13,10,11,16,17,14,15,22,20,23,21], [0,1,2,3,4,5,10,11,8,9,14,15,12,13,18,19,16,17,6,7,21,23,20,22], [0,9,2,11,4,5,6,7,8,21,10,23,14,12,15,13,3,17,1,19,20,18,22,16], [0,18,2,16,4,5,6,7,8,1,10,3,13,15,12,14,23,17,21,19,20,9,22,11]]; six = [[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23], [12,13,14,15,9,11,8,10,21,23,20,22,18,16,19,17,1,0,3,2,7,6,5,4], [8,9,10,11,5,7,4,6,20,21,22,23,14,12,15,13,3,2,1,0,19,18,17,16], [20,21,22,23,7,6,5,4,19,18,17,16,15,14,13,12,9,8,11,10,0,1,2,3], [4,5,6,7,17,19,16,18,22,20,23,21,10,8,11,9,2,0,3,1,15,14,13,12], [16,17,18,19,13,15,12,14,23,22,21,20,6,4,7,5,0,1,2,3,11,10,9,8]]; four = [[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23], [2,0,3,1,8,9,10,11,12,13,14,15,16,17,18,19,4,5,6,7,21,23,20,22], [3,2,1,0,12,13,14,15,16,17,18,19,4,5,6,7,8,9,10,11,23,22,21,20], [1,3,0,2,16,17,18,19,4,5,6,7,8,9,10,11,12,13,14,15,22,20,23,21]]; instancePositions = set()
    if not sorted(solvedCube) == sorted(instance): raise IllegalCube(instance)
    if solvedCube == instance: return [solvedCube]
    for rot in range(0,len(six)):
        newOrientation = ''.join([instance[i] for i in six[rot]]); [instancePositions.add(''.join([newOrientation[i] for i in four[spin]])) for spin in range(0, len(four))]
    graph = dict(); neighbours = list(); toRotate = {solvedCube}; temporary = set(); print("\nGenerating Pocket cube group graph...\n")
    while not instancePositions.intersection(graph):
        for cube in toRotate: 
            for move in range(0,len(legalMoves)): newCube = ''.join([cube[i] for i in legalMoves[move]]); neighbours.append(newCube)
            temporary.update(neighbours); graph[cube] = neighbours; neighbours = list()
            for instance in instancePositions: 
                if instance in graph: print("Found instance after {:,} permutations\n".format(len(graph))); return (breadthFirst(graph, solvedCube, instance))
        toRotate = temporary; temporary = set()


#                                                           14 lines c:


def printSolution(solution):
    steps = len(solution) - 1; print("Steps to solve your cube:\n")
    for step in reversed(solution): print("    "+step[0]+step[1]+"\n    "+step[2]+step[3]+"\n"+step[6]+step[7]+" "+step[10]+step[11]+" "+step[14]+step[15]+" "+step[4]+step[5]+"\n"+step[8]+step[9]+" "+step[12]+step[13]+" "+step[16]+step[17]+" "+step[18]+step[19]+"\n    "+step[20]+step[21]+"\n    "+step[22]+step[23]+"\n")
    grammar = "are {0} steps!\n".format(steps); 
    if (steps == 1): grammar = "is 1 step!\n"
    print("Minimum number of steps needed " + grammar)



printSolution(solution("OBBBWWRORRBYYYOGOGWGWGYR")) # 6 step cube
