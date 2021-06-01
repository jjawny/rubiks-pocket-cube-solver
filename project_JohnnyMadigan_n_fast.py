#████████╗███████╗░██████╗████████╗  ██████╗░░█████╗░████████╗░█████╗░
#╚══██╔══╝██╔════╝██╔════╝╚══██╔══╝  ██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗
#░░░██║░░░█████╗░░╚█████╗░░░░██║░░░  ██║░░██║███████║░░░██║░░░███████║
#░░░██║░░░██╔══╝░░░╚═══██╗░░░██║░░░  ██║░░██║██╔══██║░░░██║░░░██╔══██║
#░░░██║░░░███████╗██████╔╝░░░██║░░░  ██████╔╝██║░░██║░░░██║░░░██║░░██║
#░░░╚═╝░░░╚══════╝╚═════╝░░░░╚═╝░░░  ╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝

#  Instances for testData  | min number of steps |     total unique permutations after number of steps     |
#--------------------------|---------------------|---------------------------------------------------------|
#WSDAWKLDM33ML3MDSLKCMDLE           n/a                    n/a INVALID CUBE
#wwwwggggrrrrbbbbooooyyyy             0                        1 SOLVED but demonstrates that lowercase is allowed
#WWWWGGGGRRRRBBBBOOOOYYYY             0                        1 SOLVED
#WWBBGWGWRRRRYBYBOOOOGGYY             1                        7 (1 + 6 new permutations)
#WWBBGWOORRGWYBRROOYBYGYG             2                       34 (7 + 27 new permutations)
#WYBOGWOORWGBBRYRGOGBYRYW             3                      154 (34 + 120 new permutations)
#WYBOGWGBRWYRBRGBGOOORWYY             4                      688 (etc)
#WYBWGRGWYRRWBROBGOOOGBYY             5                    2,944
#WYBWGROOYRGWBRRWGOOBYGYB             6                   11,913
#WYBWGROBYROOBRGWGORWYYBG             7                   44,971
#WYBRGYOYOYORBRWWGORWGBBG             8                  159,120
#WYYYGGOBOORYBRRWGORWWBBG             9                  519,628
#WRYGGGOBOYRYRWBRGOBWWOBY            10                1,450,216
#WRRBGGOYYYOROWWRGOBWGBBY            11                2,801,068
#       no example                   12                3,583,604
#       no example                   13                3,673,884 
#       no example                   14                3,674,160
#
#
#OBBBWWRORRBYYYOGOGWGWGYR             6                NEW testData from assignment PDF section 6

testData = "OBBBWWRORRBYYYOGOGWGWGYR"

#██████╗░███████╗░██████╗
#██╔══██╗██╔════╝██╔════╝
#██████╦╝█████╗░░╚█████╗░
#██╔══██╗██╔══╝░░░╚═══██╗
#██████╦╝██║░░░░░██████╔╝
#╚═════╝░╚═╝░░░░░╚═════╝░

# Breadth First Search function modified but inspired from https://stackoverflow.com/a/50575971
# Since the permutations can go up to over 3.6 million, this performs the best
def breadthFirst(graph, solved, instance):
    queue = [(solved,[solved])]
    visited = set()
    print("Performing a Breadth-first search...")
    while queue:
        cube, path = queue.pop(0)
        visited.add(cube)
        for cube in graph[cube]:
            if cube == instance: return path + [instance] 
            elif cube not in visited:
                    visited.add(cube)
                    queue.append((cube, path + [cube]))


#░██████╗░█████╗░██╗░░░░░██╗░░░██╗████████╗██╗░█████╗░███╗░░██╗
#██╔════╝██╔══██╗██║░░░░░██║░░░██║╚══██╔══╝██║██╔══██╗████╗░██║
#╚█████╗░██║░░██║██║░░░░░██║░░░██║░░░██║░░░██║██║░░██║██╔██╗██║
#░╚═══██╗██║░░██║██║░░░░░██║░░░██║░░░██║░░░██║██║░░██║██║╚████║
#██████╔╝╚█████╔╝███████╗╚██████╔╝░░░██║░░░██║╚█████╔╝██║░╚███║
#╚═════╝░░╚════╝░╚══════╝░╚═════╝░░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚══╝

def solution(instance):    
    solvedCube = "WWWWGGGGRRRRBBBBOOOOYYYY" # the solved instance
    instance = instance.upper() # make sure instance is capitalised

    # The 6 legal quarter turns rather than 12 as half the moves are redundent,
    # this is because we don't care about the orientation of the cube
    legalMoves = [[0,1,7,5,4,20,6,21,10,8,11,9,2,13,3,15,16,17,18,19,14,12,22,23],  # U    up clockwise
        [0,1,12,14,4,3,6,2,9,11,8,10,21,13,20,15,16,17,18,19,5,7,22,23],            # U'   up anti-clockwise
        [0,1,2,3,4,5,18,19,8,9,6,7,12,13,10,11,16,17,14,15,22,20,23,21],            # F    front clockwise
        [0,1,2,3,4,5,10,11,8,9,14,15,12,13,18,19,16,17,6,7,21,23,20,22],            # F'   front anti-clockwise
        [0,9,2,11,4,5,6,7,8,21,10,23,14,12,15,13,3,17,1,19,20,18,22,16],            # R    right clockwise
        [0,18,2,16,4,5,6,7,8,1,10,3,13,15,12,14,23,17,21,19,20,9,22,11]]            # R'   right anti-clockwise

    # Rotating the whole cube in 3D space (each face takes a turn being on top)
    six = [[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23],
        [12,13,14,15,9,11,8,10,21,23,20,22,18,16,19,17,1,0,3,2,7,6,5,4],
        [8,9,10,11,5,7,4,6,20,21,22,23,14,12,15,13,3,2,1,0,19,18,17,16],
        [20,21,22,23,7,6,5,4,19,18,17,16,15,14,13,12,9,8,11,10,0,1,2,3],
        [4,5,6,7,17,19,16,18,22,20,23,21,10,8,11,9,2,0,3,1,15,14,13,12],
        [16,17,18,19,13,15,12,14,23,22,21,20,6,4,7,5,0,1,2,3,11,10,9,8]]

    # Spinning the whole cube keeping the same face down (4 x 90degree rotations)
    four = [[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23],
        [2,0,3,1,8,9,10,11,12,13,14,15,16,17,18,19,4,5,6,7,21,23,20,22],
        [3,2,1,0,12,13,14,15,16,17,18,19,4,5,6,7,8,9,10,11,23,22,21,20],
        [1,3,0,2,16,17,18,19,4,5,6,7,8,9,10,11,12,13,14,15,22,20,23,21]]

    # Check early to see if the cube is scrambled properly,
    # if so, return the correct data structure but empty, saving memory
    if not sorted(solvedCube) == sorted(instance): 
        return []
    
    # Check early to see if the cube is already solved,
    # if so, return the solved cube in the correct data structure, saving memory
    if solvedCube == instance: 
        return [solvedCube]

    # Since we want ultimate flexibility for user inputs, the instance may be in any orientation,
    # therefore we must get all 24 orientations of the problem instance in 3D space so we can ignore the position
    pCubes = set()
    for rot in range(0,len(six)):
        newOrientation = ''.join([instance[i] for i in six[rot]])
        [pCubes.add(''.join([newOrientation[i] for i in four[spin]])) for spin in range(0, len(four))]


#TODO need better comments below

    graph = dict()          # Adjacency list (keys are vertices (cubes) and values are edges (cubes related by transforming to one-another with a quarter turn))
    neighbours = list()     # ?
    toRotate = {solvedCube} # next set of parent cubes to rotate (starts off with the solved cube)
    temporary = set()       # temporary holding for next set of cubes to be rotated next after current rotations are done

    print("\nsearching...\n")
    while not pCubes.intersection(graph):
        
        for cube in toRotate:
            for move in range(0,len(legalMoves)):
                newCube = ''.join([cube[i] for i in legalMoves[move]])
                neighbours.append(newCube)
                
            graph[cube] = neighbours
            temporary.update(neighbours) # temporary as toRotate is in use
            neighbours = list() # reset as all the neighbours have been found for the cube

            for c in pCubes:
                if c in graph:
                    print("Found instance after {:,} permutations\n".format(len(graph)))
                    finalCubes = (breadthFirst(graph, solvedCube, c))
                    return finalCubes # return the minimum vertice path

        toRotate = temporary
        temporary = set() # reset tempor
        print("Total permutations so far... {:,}".format(len(graph))) # live update for number of permutations


#██████╗░██████╗░██╗███╗░░██╗████████╗  ░██████╗░█████╗░██╗░░░░░██╗░░░██╗████████╗██╗░█████╗░███╗░░██╗
#██╔══██╗██╔══██╗██║████╗░██║╚══██╔══╝  ██╔════╝██╔══██╗██║░░░░░██║░░░██║╚══██╔══╝██║██╔══██╗████╗░██║
#██████╔╝██████╔╝██║██╔██╗██║░░░██║░░░  ╚█████╗░██║░░██║██║░░░░░██║░░░██║░░░██║░░░██║██║░░██║██╔██╗██║
#██╔═══╝░██╔══██╗██║██║╚████║░░░██║░░░  ░╚═══██╗██║░░██║██║░░░░░██║░░░██║░░░██║░░░██║██║░░██║██║╚████║
#██║░░░░░██║░░██║██║██║░╚███║░░░██║░░░  ██████╔╝╚█████╔╝███████╗╚██████╔╝░░░██║░░░██║╚█████╔╝██║░╚███║
#╚═╝░░░░░╚═╝░░╚═╝╚═╝╚═╝░░╚══╝░░░╚═╝░░░  ╚═════╝░░╚════╝░╚══════╝░╚═════╝░░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚══╝

def printSolution(solution):
    steps = len(solution) - 1 # -1 as the first cube doesnt count
    if (steps == -1):
        print("Invalid scrambled cube, please make sure you have 4 of each colours\n")
    else:
        print("Minimum number of steps to solve your cube are {0} steps!\n".format(steps))

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
