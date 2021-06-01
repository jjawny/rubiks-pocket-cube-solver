#████████╗███████╗░██████╗████████╗  ██████╗░░█████╗░████████╗░█████╗░
#╚══██╔══╝██╔════╝██╔════╝╚══██╔══╝  ██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗
#░░░██║░░░█████╗░░╚█████╗░░░░██║░░░  ██║░░██║███████║░░░██║░░░███████║
#░░░██║░░░██╔══╝░░░╚═══██╗░░░██║░░░  ██║░░██║██╔══██║░░░██║░░░██╔══██║
#░░░██║░░░███████╗██████╔╝░░░██║░░░  ██████╔╝██║░░██║░░░██║░░░██║░░██║
#░░░╚═╝░░░╚══════╝╚═════╝░░░░╚═╝░░░  ╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝

#  Instances for testData  | min number of steps to solve | total unique permutations generated after applying a certain number of steps |
#--------------------------|------------------------------|------------------------------------------------------------------------------|
#WSDAWKLDM33ML3MDSLKCMDLE                   n/a                        n/a = INVALID CUBE
#wwwwggggrrrrbbbbooooyyyy               0 steps                          1 = ALREADY SOLVED but demonstrates that lowercase is allowed
#WWWWGGGGRRRRBBBBOOOOYYYY               0 steps                          1 = ALREADY SOLVED
#WWBBGWGWRRRRYBYBOOOOGGYY               1 steps                          7 = previous total (1) + new unique permutations (6)
#WWBBGWOORRGWYBRROOYBYGYG               2 steps                         34 = previous total (7) + new unique permutations (27)
#WYBOGWOORWGBBRYRGOGBYRYW               3 steps                        154 = previous total (34) + new unique permutations (120)
#WYBOGWGBRWYRBRGBGOOORWYY               4 steps                        688 = previous total (154) + new unique permutations (534)
#WYBWGRGWYRRWBROBGOOOGBYY               5 steps                      2,944 = previous total (688) + new unique permutations (2,256)
#WYBWGROOYRGWBRRWGOOBYGYB               6 steps                     11,913 = previous total (2,944) + new unique permutations (8,969)
#WYBWGROBYROOBRGWGORWYYBG               7 steps                     44,971 = previous total (11,913) + new unique permutations (33,058)
#WYBRGYOYOYORBRWWGORWGBBG               8 steps                    159,120 = previous total (44,971) + new unique permutations (114,149)
#WYYYGGOBOORYBRRWGORWWBBG               9 steps                    519,628 = previous total (159,120) + new unique permutations (360,508)
#WRYGGGOBOYRYRWBRGOBWWOBY              10 steps                  1,450,216 = previous total (519,628) + new unique permutations (930,588)
#WRRBGGOYYYOROWWRGOBWGBBY              11 steps                  2,801,068 = previous total (1,450,216) + new unique permutations (1,350,852)
#       no example                     12 steps                  3,583,604 = previous total (2,801,068) + new unique permutations (782,536)
#       no example                     13 steps                  3,673,884 = previous total (3,583,604) + new unique permutations (90,280)
#       no example                     14 steps                  3,674,160 = previous total (3,673,884) + new unique permutations (276)
#
#OBBBWWRORRBYYYOGOGWGWGYR               6 steps                              NEW testData from Assignment PDF Section 6

testData = "OBBBWWRORRBYYYOGOGWGWGYR"


#██████╗░███████╗░██████╗
#██╔══██╗██╔════╝██╔════╝
#██████╦╝█████╗░░╚█████╗░
#██╔══██╗██╔══╝░░░╚═══██╗
#██████╦╝██║░░░░░██████╔╝
#╚═════╝░╚═╝░░░░░╚═════╝░

# Breadth-First Search function from https://stackoverflow.com/a/50575971
# Since the permutations can go up to over 3.6 million, this performs the best
# Was unsure if I was allowed to reference external code but checked with Matt and it's okay!
def breadthFirst(graph, start, end):

    queue = [(start,[start])]
    visited = set()

    print("Performing a Breadth-first search...")
    while queue:
        vertex, path = queue.pop(0)
        visited.add(vertex)

        for node in graph[vertex]:
            if node == end: return path + [end]
            elif node not in visited:
                    visited.add(node)
                    queue.append((node, path + [node]))


#░██████╗░█████╗░██╗░░░░░██╗░░░██╗████████╗██╗░█████╗░███╗░░██╗
#██╔════╝██╔══██╗██║░░░░░██║░░░██║╚══██╔══╝██║██╔══██╗████╗░██║
#╚█████╗░██║░░██║██║░░░░░██║░░░██║░░░██║░░░██║██║░░██║██╔██╗██║
#░╚═══██╗██║░░██║██║░░░░░██║░░░██║░░░██║░░░██║██║░░██║██║╚████║
#██████╔╝╚█████╔╝███████╗╚██████╔╝░░░██║░░░██║╚█████╔╝██║░╚███║
#╚═════╝░░╚════╝░╚══════╝░╚═════╝░░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚══╝

def solution(instance):    
    solvedCube = "WWWWGGGGRRRRBBBBOOOOYYYY"; instance = instance.upper(); legalMoves = [[0,1,7,5,4,20,6,21,10,8,11,9,2,13,3,15,16,17,18,19,14,12,22,23], [0,1,12,14,4,3,6,2,9,11,8,10,21,13,20,15,16,17,18,19,5,7,22,23], [0,1,2,3,4,5,18,19,8,9,6,7,12,13,10,11,16,17,14,15,22,20,23,21], [0,1,2,3,4,5,10,11,8,9,14,15,12,13,18,19,16,17,6,7,21,23,20,22], [0,9,2,11,4,5,6,7,8,21,10,23,14,12,15,13,3,17,1,19,20,18,22,16], [0,18,2,16,4,5,6,7,8,1,10,3,13,15,12,14,23,17,21,19,20,9,22,11]]; six = [[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23], [12,13,14,15,9,11,8,10,21,23,20,22,18,16,19,17,1,0,3,2,7,6,5,4], [8,9,10,11,5,7,4,6,20,21,22,23,14,12,15,13,3,2,1,0,19,18,17,16], [20,21,22,23,7,6,5,4,19,18,17,16,15,14,13,12,9,8,11,10,0,1,2,3], [4,5,6,7,17,19,16,18,22,20,23,21,10,8,11,9,2,0,3,1,15,14,13,12], [16,17,18,19,13,15,12,14,23,22,21,20,6,4,7,5,0,1,2,3,11,10,9,8]]; four = [[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23], [2,0,3,1,8,9,10,11,12,13,14,15,16,17,18,19,4,5,6,7,21,23,20,22], [3,2,1,0,12,13,14,15,16,17,18,19,4,5,6,7,8,9,10,11,23,22,21,20], [1,3,0,2,16,17,18,19,4,5,6,7,8,9,10,11,12,13,14,15,22,20,23,21]]; pCubes = set()
    if not sorted(solvedCube) == sorted(instance): return []
    if solvedCube == instance: return [solvedCube]
    for rot in range(0,len(six)): newOrientation = ''.join([instance[i] for i in six[rot]]); [pCubes.add(''.join([newOrientation[i] for i in four[spin]])) for spin in range(0, len(four))]
    graph = dict(); neighbours = list(); toRotate = {solvedCube}; temporary = set(); print("\nsearching...\n")
    while not pCubes.intersection(graph):
        for cube in toRotate:
            for move in range(0,len(legalMoves)): newCube = ''.join([cube[i] for i in legalMoves[move]]); neighbours.append(newCube)
            graph[cube] = neighbours; temporary.update(neighbours); neighbours = list()
            for c in pCubes:
                if c in graph: print("Found instance after {:,} permutations\n".format(len(graph))); finalCubes = (breadthFirst(graph, solvedCube, c)); return finalCubes
        toRotate = temporary; temporary = set(); print("Total permutations so far... {:,}".format(len(graph)))

#                                                       13 lines c:

#██████╗░██████╗░██╗███╗░░██╗████████╗  ░██████╗░█████╗░██╗░░░░░██╗░░░██╗████████╗██╗░█████╗░███╗░░██╗
#██╔══██╗██╔══██╗██║████╗░██║╚══██╔══╝  ██╔════╝██╔══██╗██║░░░░░██║░░░██║╚══██╔══╝██║██╔══██╗████╗░██║
#██████╔╝██████╔╝██║██╔██╗██║░░░██║░░░  ╚█████╗░██║░░██║██║░░░░░██║░░░██║░░░██║░░░██║██║░░██║██╔██╗██║
#██╔═══╝░██╔══██╗██║██║╚████║░░░██║░░░  ░╚═══██╗██║░░██║██║░░░░░██║░░░██║░░░██║░░░██║██║░░██║██║╚████║
#██║░░░░░██║░░██║██║██║░╚███║░░░██║░░░  ██████╔╝╚█████╔╝███████╗╚██████╔╝░░░██║░░░██║╚█████╔╝██║░╚███║
#╚═╝░░░░░╚═╝░░╚═╝╚═╝╚═╝░░╚══╝░░░╚═╝░░░  ╚═════╝░░╚════╝░╚══════╝░╚═════╝░░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚══╝

def printSolution(solution):
    steps = len(solution) - 1 # -1 as there are no steps to GET the solved cube, the graph just starts there
    [print("\nInvalid scrambled cube, please make sure you have 4 of each colours\n") if steps == -1 else print("Minimum number of steps to solve your cube are {0} steps!\n".format(steps))]

printSolution(solution(testData))

#                                              {{{{{{{{{{{{{{{{{GUIDE TO SCRAMBLING YOUR OWN CUBE}}}}}}}}}}}}}}}}}
#                        +                               
#                     _.-"-,                    A Pocket Cube has 6 faces and 24 stickers (4 per face). When solved
#                _.-""   |  ',                  each face is a single colour, the colours are...
#             +:"        |    ',                
#              |\        |      '.+             (W) white, (R) red, (Y) yellow, (G) green, (B) blue, (O) orange
#              | \       |    _."|              
#              |  '.   _.+.,."   |              Pick any face on your scrambled cube and draw a diagram out like this:
#              |   _\-",-' ",    |                                      +-------+
#              |_-" "+'      ",  |                                      |  1 2  |
#             +{     |         ".|                                      |  3 4  |
#               \    |          ,+                              +-------+-------+-------+-------+
#                ".  |      ,-'                                 |  5 6  |  9 10 | 13 14 | 17 18 |
#                  \ |   ,-'                                    |  7 8  | 11 12 | 15 16 | 19 20 |
#                   \|,-'                                       +-------+-------+-------+-------+
#                    +                                                  | 21 22 |
#        {{{DESIGNED by JOHNNY MADIGAN}}}                               | 23 24 |
#                                                                       +-------+
#                                               Finally, follow the order in the diagram above and note down the colour
#                                               of the 24 stickers and you should end up with something like this: 
#
#                                                                   WWBBGWOORRGWYBRROOYBYGYG
