

#                        FULL NAME: JOHNNY MADIGAN
#                   STUDENT NUMBER: N????????



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

testData = "OBBBWWRORRBYYYOGOGWGWGYR" # currently set to testData from Assignment PDF Section 6

#██████╗░██╗░██████╗████████╗░█████╗░███╗░░██╗░█████╗░███████╗ ░█████╗░██╗░░░░░░█████╗░░██████╗░██████╗███████╗░██████╗
#██╔══██╗██║██╔════╝╚══██╔══╝██╔══██╗████╗░██║██╔══██╗██╔════╝ ██╔══██╗██║░░░░░██╔══██╗██╔════╝██╔════╝██╔════╝██╔════╝
#██║░░██║██║╚█████╗░░░░██║░░░███████║██╔██╗██║██║░░╚═╝█████╗░░ ██║░░╚═╝██║░░░░░███████║╚█████╗░╚█████╗░█████╗░░╚█████╗░
#██║░░██║██║░╚═══██╗░░░██║░░░██╔══██║██║╚████║██║░░██╗██╔══╝░░ ██║░░██╗██║░░░░░██╔══██║░╚═══██╗░╚═══██╗██╔══╝░░░╚═══██╗
#██████╔╝██║██████╔╝░░░██║░░░██║░░██║██║░╚███║╚█████╔╝███████╗ ╚█████╔╝███████╗██║░░██║██████╔╝██████╔╝███████╗██████╔╝
#╚═════╝░╚═╝╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚══╝░╚════╝░╚══════╝ ░╚════╝░╚══════╝╚═╝░░╚═╝╚═════╝░╚═════╝░╚══════╝╚═════╝░

# From graphys.py obtained from CAB203 Blackboard
def distanceClasses(V, E, u):
    V0 = V              # V_0 = V
    D = [ {u} ]         # D[0] = D_0 = {u}
    print("Getting distance classes...")
    return distanceClassesR(V0, E, D)

# From graphys.py obtained from CAB203 Blackboard
def distanceClassesR(V, E, D):
    Vnew = V - D[-1]            # V_{j} = V_{j-1} / D_{j-1}
    if len(Vnew) == 0: return D # Already considered all elements?
    Dnew = D + [ NS_out(Vnew, E, D[-1]) ]  # D_{j} = N_{V_j}(D_{j-1})
    return distanceClassesR(Vnew, E, Dnew)

# From graphys.py obtained from CAB203 Blackboard
def NS_out(V, E, S):
    return { v for v in V for u in S if (u,v) in E }

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
        print("Invalid scrambled cube, please make sure you have 4 of each colours")
        return ({}, None) # return nothing
    
    # Check early to see if the cube is already solved,
    # if so, return the solved cube in the correct data structure, saving memory
    if solvedCube == instance: return ([{solvedCube}], solvedCube)

    # Since we want ultimate flexibility for user inputs, the instance may be in any orientation,
    # therefore we must get all 24 orientations of the problem instance in 3D space so we can ignore the position
    # THE ONLY TIME "SIX" & "FOUR" ARE USED
    pCubes = set()
    for rot in range(0,len(six)):
        newOrientation = ''.join([instance[i] for i in six[rot]])
        [pCubes.add(''.join([newOrientation[i] for i in four[spin]])) for spin in range(0, len(four))]

    toRotate = {solvedCube} # Next set of parent cubes to rotate (starts off with the solved cube)
    temporary = set()       # Temporary holding for next set of cubes to be rotated next after current rotations are done
    E = set()               # Set of edges (cubes related by transforming to one-another with a quarter turn)
    V = {solvedCube}        # Set of vertices (cubes)

    print("\nsearching...\n")
    while not pCubes.intersection(V): # while no orientations of the problem instance intersect the set of vertices
        
        # For each parent cube we need to rotate,
        # rotate the parent cube 6 times (each quarter move)
        for cube in toRotate:
            for move in range(0,len(legalMoves)):
                newCube = ''.join([cube[i] for i in legalMoves[move]])  # Create a new instance rearranging the stickers to simulate a quarter move
                temporary.add(newCube)                                  # Save the derived cube to be manipulated next round
                V.add(newCube)                                          # Store the cube as a vertex
                E.update(((newCube, cube),(cube, newCube)))             # Store edges both ways as this graph is undirected
                
            # If any orientation of the problem instances is found in the set of vertices, 
            # generate and return the distance classes along with the specific orientation of the problem instance found
            for c in pCubes:
                if c in V:
                    print("Found instance after {:,} permutations\n".format(len(V)))
                    return ((distanceClasses(V, E, solvedCube)), c)

        # Transfer over the next set of vertices to generate new vertices from, and reset/empty the temporary set
        toRotate = temporary
        temporary = set()
        print("Total permutations so far... {:,}".format(len(V))) 


#██████╗░██████╗░██╗███╗░░██╗████████╗  ░██████╗░█████╗░██╗░░░░░██╗░░░██╗████████╗██╗░█████╗░███╗░░██╗
#██╔══██╗██╔══██╗██║████╗░██║╚══██╔══╝  ██╔════╝██╔══██╗██║░░░░░██║░░░██║╚══██╔══╝██║██╔══██╗████╗░██║
#██████╔╝██████╔╝██║██╔██╗██║░░░██║░░░  ╚█████╗░██║░░██║██║░░░░░██║░░░██║░░░██║░░░██║██║░░██║██╔██╗██║
#██╔═══╝░██╔══██╗██║██║╚████║░░░██║░░░  ░╚═══██╗██║░░██║██║░░░░░██║░░░██║░░░██║░░░██║██║░░██║██║╚████║
#██║░░░░░██║░░██║██║██║░╚███║░░░██║░░░  ██████╔╝╚█████╔╝███████╗╚██████╔╝░░░██║░░░██║╚█████╔╝██║░╚███║
#╚═╝░░░░░╚═╝░░╚═╝╚═╝╚═╝░░╚══╝░░░╚═╝░░░  ╚═════╝░░╚════╝░╚══════╝░╚═════╝░░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚══╝

def printSolution(data):
    [print("Minimum number of steps to solve your cube are {0} steps!\n".format(data[0].index(distance))) for distance in data[0] if data[1] in distance]

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
#           STUDENT NUMBER: N????????                                   +-------+
#                                               Finally, follow the order in the diagram above and note down the colour
#                                               of the 24 stickers and you should end up with something like this: 
#
#                                                                   WWBBGWOORRGWYBRROOYBYGYG
