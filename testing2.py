#████████╗███████╗░██████╗████████╗  ██████╗░░█████╗░████████╗░█████╗░
#╚══██╔══╝██╔════╝██╔════╝╚══██╔══╝  ██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗
#░░░██║░░░█████╗░░╚█████╗░░░░██║░░░  ██║░░██║███████║░░░██║░░░███████║
#░░░██║░░░██╔══╝░░░╚═══██╗░░░██║░░░  ██║░░██║██╔══██║░░░██║░░░██╔══██║
#░░░██║░░░███████╗██████╔╝░░░██║░░░  ██████╔╝██║░░██║░░░██║░░░██║░░██║
#░░░╚═╝░░░╚══════╝╚═════╝░░░░╚═╝░░░  ╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝

#testData = ["GRY", "BRY", "GOY", "GOW", "BOW", "BOY", "BRW", "GRW"] # expecting 1 steps (applied 1 legal move)
#testData = ["GRY", "BRY", "OGY", "OGW", "OBW", "OBY", "BRW", "GRW"] # expecting 1 steps (same as above except not in alphabetical order)
#testData = ["BRW", "GOW", "GRY", "GOY", "BOW", "BOY", "GRW", "BRY"] # expecting 2 steps (applied 2 legal moves)
#testData = ["brW", "GOw", "grY", "GOY", "bow", "BOY", "GRW", "bry"] # expecting 2 steps (same as above but not uppercase)
#testData = ["BOW", "BRW", "GRY", "GOY", "BRY", "BOY", "GOW", "GRW"] # expecting 6 steps (randomly put corners together)
##testData = ["OBW", "BRY", "OGW", "BRW", "GRW", "GRY", "OBY", "OGY"] # expecting 11 steps (test data from section 6 of assignment pdf)

# ██████  ███████ ███████
# ██   ██ ██      ██
# ██   ██ █████   ███████
# ██   ██ ██           ██
# ██████  ██      ███████

############
# Undirected versions
# edges are symmetric, so arbitrarily using the out version of above.

# vertices connected by an edge from u.
def N_out(V, E, u):
    return { v for v in V if (u,v) in E }

def N(V, E, u):
   return N_out(V, E, u)

def depthFirst(V, E, u, goal):
    T = {u}             # set of vertices already seen
    return depthFirstR(V, E, u, goal, T)
    
def depthFirstR(V, E, u, goal, T):
    #print('processing ', u)                # process vertex u
    
    if len(T) == len(V): return T # already seen all?
    Nu = N(V, E, u) - T     # Neighbours not already seen
    print(len(Nu))
    T.update(Nu)            # Update set of vertices seen
    print(len(T))
    temp = set()
    while goal not in T:
        print("working")
        for v in Nu:
            if len(T) >= len(V): print("seen all"); break # already seen all?
            y = (N(V, E, v) - T)
            for i in y:
                temp.add(i)     # Neighbours not already seen 
            if goal in y:
                for i in y:
                    temp.add(i)     # Neighbours not already seen 
                print("earlyyyy")
                print(goal)
                #temp.add(goal)
                goalsNeighbours = (N(V, E, goal) - T)
                goalsNeighbours.add(goal)
                goalsNeighbours.add(v)
                T = T.union(goalsNeighbours)
                #T = T.union(temp)
                T = T.union(Nu)
                if goal in temp:
                    print ("yes its here")
                print("found early should stop here")    
                return T                

        T = T.union(Nu)
        Nu = temp
        temp = set()
    print("returned")
    return T


#██████╗░██╗░██████╗████████╗░█████╗░███╗░░██╗░█████╗░███████╗  ░█████╗░██╗░░░░░░█████╗░░██████╗░██████╗███████╗░██████╗
#██╔══██╗██║██╔════╝╚══██╔══╝██╔══██╗████╗░██║██╔══██╗██╔════╝  ██╔══██╗██║░░░░░██╔══██╗██╔════╝██╔════╝██╔════╝██╔════╝
#██║░░██║██║╚█████╗░░░░██║░░░███████║██╔██╗██║██║░░╚═╝█████╗░░  ██║░░╚═╝██║░░░░░███████║╚█████╗░╚█████╗░█████╗░░╚█████╗░
#██║░░██║██║░╚═══██╗░░░██║░░░██╔══██║██║╚████║██║░░██╗██╔══╝░░  ██║░░██╗██║░░░░░██╔══██║░╚═══██╗░╚═══██╗██╔══╝░░░╚═══██╗
#██████╔╝██║██████╔╝░░░██║░░░██║░░██║██║░╚███║╚█████╔╝███████╗  ╚█████╔╝███████╗██║░░██║██████╔╝██████╔╝███████╗██████╔╝
#╚═════╝░╚═╝╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚══╝░╚════╝░╚══════╝  ░╚════╝░╚══════╝╚═╝░░╚═╝╚═════╝░╚═════╝░╚══════╝╚═════╝░

def distanceClasses(V, E, u):
    V0 = V              # V_0 = V
    D = [ {u} ]         # D[0] = D_0 = {u}
    return distanceClassesR(V0, E, D)

def distanceClassesR(V, E, D):
    Vnew = V - D[-1]            # V_{j} = V_{j-1} / D_{j-1}
    if len(Vnew) == 0: return D # Already considered all elements?
    Dnew = D + [ NS_out(Vnew, E, D[-1]) ]  # D_{j} = N_{V_j}(D_{j-1})
    return distanceClassesR(Vnew, E, Dnew)

    # vertices connected by an edge from S.
def NS_out(V, E, S):
    return { v for v in V for u in S if (u,v) in E }


#░██████╗░█████╗░██╗░░░░░██╗░░░██╗████████╗██╗░█████╗░███╗░░██╗
#██╔════╝██╔══██╗██║░░░░░██║░░░██║╚══██╔══╝██║██╔══██╗████╗░██║
#╚█████╗░██║░░██║██║░░░░░██║░░░██║░░░██║░░░██║██║░░██║██╔██╗██║
#░╚═══██╗██║░░██║██║░░░░░██║░░░██║░░░██║░░░██║██║░░██║██║╚████║
#██████╔╝╚█████╔╝███████╗╚██████╔╝░░░██║░░░██║╚█████╔╝██║░╚███║
#╚═════╝░░╚════╝░╚══════╝░╚═════╝░░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚══╝

#turn UP 90 anti               U'
#turn RIGHT 90 anti          R'
#turn UP  90x2            U U
#turn FRONT 90x2          F F
#turn TOP 90 clockwise       U
#turn FRONT 90 anti           F'
#turn RIGHT 90 anti            R'
#turn FRONT 90 clockwise        F
#turn TOP 90 anti                U'    1  2  5 3   0      2 2 0 0 5 1

#WWWWGGGGRRRRBBBBOOOOYYYY solved            1 unique permutation
#WWBBGWGWRRRRYBYBOOOOGGYY 1 rotation        7 unique permutations
#WWBBGWOORRGWYBRROOYBYGYG 2 rotations      34 unique permutations
#WYBOGWOORWGBBRYRGOGBYRYW 3     "         154 unique permutations
#WYBOGWGBRWYRBRGBGOOORWYY 4     "         688 unique permutations yes
#WYBWGRGWYRRWBROBGOOOGBYY 5     "        2944 unique permutations
#WYBWGROOYRGWBRRWGOOBYGYB 6     "      11,913 unique permutations
#WYBWGROBYROOBRGWGORWYYBG 7            44,971 unique permutations
#WYBRGYOYOYORBRWWGORWGBBG 8           159,120 unique permutations
#WYYYGGOBOORYBRRWGORWWBBG 9           519,628 unique permutations
#WRYGGGOBOYRYRWBRGOBWWOBY 10        1,450,216 unique permutations
#WRRBGGOYYYOROWWRGOBWGBBY 11        2,801,068 unique permutations
#                         12        3,583,604 unique permutations
#                         13        3,673,884 unique permutations
#                         14        3,674,160 unique permutations
#WRBRGWBORWBGGGYOYOYRWOYB testData from project sec 6 but manual
#check if same perm but just rotated before adding to V
#import sys
#sys.setrecursionlimit(5000)
testData = "WYBRGYOYOYORBRWWGORWGBBG" #max achieved 9

def solution(problemCube):    
    solvedCube = "WWWWGGGGRRRRBBBBOOOOYYYY"

    legalMoves = [
        [0,1,7,5,4,20,6,21,10,8,11,9,2,13,3,15,16,17,18,19,14,12,22,23], # U    up clockwise
        [0,1,12,14,4,3,6,2,9,11,8,10,21,13,20,15,16,17,18,19,5,7,22,23], # U'   up anti-clockwise
        [0,1,2,3,4,5,18,19,8,9,6,7,12,13,10,11,16,17,14,15,22,20,23,21], # F    front clockwise
        [0,1,2,3,4,5,10,11,8,9,14,15,12,13,18,19,16,17,6,7,21,23,20,22], # F'   front anti-clockwise
        [0,9,2,11,4,5,6,7,8,21,10,23,14,12,15,13,3,17,1,19,20,18,22,16], # R    right clockwise
        [0,18,2,16,4,5,6,7,8,1,10,3,13,15,12,14,23,17,21,19,20,9,22,11]] # R'   right anti-clockwise

    six = [
        [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23], # Red face on top
        [12,13,14,15,9,11,8,10,21,23,20,22,18,16,19,17,1,0,3,2,7,6,5,4], # ? on top
        [8,9,10,11,5,7,4,6,20,21,22,23,14,12,15,13,3,2,1,0,19,18,17,16], #
        [20,21,22,23,7,6,5,4,19,18,17,16,15,14,13,12,9,8,11,10,0,1,2,3], #
        [4,5,6,7,17,19,16,18,22,20,23,21,10,8,11,9,2,0,3,1,15,14,13,12], #
        [16,17,18,19,13,15,12,14,23,22,21,20,6,4,7,5,0,1,2,3,11,10,9,8]] #

    four = [
        [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23], # Spin left 90 degrees
        [2,0,3,1,8,9,10,11,12,13,14,15,16,17,18,19,4,5,6,7,21,23,20,22], # Spin left 180 degrees
        [3,2,1,0,12,13,14,15,16,17,18,19,4,5,6,7,8,9,10,11,23,22,21,20], # Spin left 270 degrees
        [1,3,0,2,16,17,18,19,4,5,6,7,8,9,10,11,12,13,14,15,22,20,23,21]] # Spin left 360 degrees

    if not sorted(solvedCube) == sorted(problemCube): # check early to see if the cube is scrambled properly
        print("Invalid scrambled cube, please make sure you have 4 of each colours")
        return [{}]

    if solvedCube == problemCube: # solve here rather than processing at all to save memory
        print("Cube already solved!")
        return [{}]

    # get all 24 rotations of the problem cube in 3D space in 3D space so we can ignore position
    pCubes = set()
    for rot in range(0,len(six)):
        anewCube = ''.join([problemCube[i] for i in six[rot]])
        for spin in range(0, len(four)):
            pCubes.add(''.join([anewCube[i] for i in four[spin]]))

    toRotate = {solvedCube} # next set of parent cubes to rotate (starts off with the solved cube)
    temporary = set()       # temporary holding for next set of cubes to be rotated next after current rotations are done
    V = set()               # vertices are cubes
    E = set()               # edges are parent-child relationships (parent cube and it's 6 children cubes, 1 after each legal move rotation)

    print("searching...")
    while pCubes.isdisjoint(V):
        print("Total permutations so far... {0}".format(len(V)))
        for cube in toRotate:
            for move in range(0,len(legalMoves)):
                newCube = ''.join([cube[i] for i in legalMoves[move]])

                # add vertex (permutation) & edges (related cubes)
                V.add(newCube)
                E.update(((newCube, cube),(cube, newCube)))
                temporary.add(newCube)

                # check if the problem cube is found here so we
                # can stop creating unnecessary permutations ASAP
                # as this can go up to 3.6 million permutations...
                if newCube in pCubes:
                #found = ''.join(c for c in pCubes if c in V)
                #if found:
                    print("found it!")
                    yeet = depthFirst(V, E, newCube, solvedCube)
                    newE = set()
                    for e in E:
                        if e[0] in yeet:
                            if e[1] in yeet:
                                newE.add(e)
                    print("old V length")
                    print(len(V))
                    print("new V length")
                    print(len(yeet))
                    print("Old E length")
                    print(len(E))
                    print("new E length")
                    print(len(newE))

                    if newCube in yeet:
                        print ("yes its heressds")
                    for pair in newE:
                        if newCube in pair:
                            print("also in edges")

                    print("Total permutations... {0}\nCreating solution model...".format(len(V)))
                    return ((distanceClasses(yeet, newE, solvedCube)), newCube)
        # reset
        V = V.union(toRotate)
        toRotate = temporary
        temporary = set()




#██████╗░██████╗░██╗███╗░░██╗████████╗  ░██████╗░█████╗░██╗░░░░░██╗░░░██╗████████╗██╗░█████╗░███╗░░██╗
#██╔══██╗██╔══██╗██║████╗░██║╚══██╔══╝  ██╔════╝██╔══██╗██║░░░░░██║░░░██║╚══██╔══╝██║██╔══██╗████╗░██║
#██████╔╝██████╔╝██║██╔██╗██║░░░██║░░░  ╚█████╗░██║░░██║██║░░░░░██║░░░██║░░░██║░░░██║██║░░██║██╔██╗██║
#██╔═══╝░██╔══██╗██║██║╚████║░░░██║░░░  ░╚═══██╗██║░░██║██║░░░░░██║░░░██║░░░██║░░░██║██║░░██║██║╚████║
#██║░░░░░██║░░██║██║██║░╚███║░░░██║░░░  ██████╔╝╚█████╔╝███████╗╚██████╔╝░░░██║░░░██║╚█████╔╝██║░╚███║
#╚═╝░░░░░╚═╝░░╚═╝╚═╝╚═╝░░╚══╝░░░╚═╝░░░  ╚═════╝░░╚════╝░╚══════╝░╚═════╝░░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚══╝

def printSolution(data):
    #[print("Cube already solved!") if data[0].index(distance) == 0 else print("Minimum number of steps to solve your cube are {0} steps!".format(data[0].index(distance))) for distance in data[0] if data[1] in distance]
    for distance in data[0]:
        if data[1] in distance:
            index = data[0].index(distance)
            print("Minimum number of steps to solve your cube are {0} steps!".format(index))

printSolution(solution(testData))


#                      (BRW)                    {{{{{{{{GUIDE TO SCRAMBLING YOUR OWN CUBE}}}}}}}}
#                        +                         
#                     _.-"-,                    A Pocket Cube (2x2x2), is made of 8 corner pieces that are all unique
#                _.-""   |  ',                  in the way that each corner has a different combination of 3 colours.
#        (GRW)+:"        |    ',                The colours...
#              |\        |      '.+(BRY)
#              | \     (BOW)  _."|              (W) white
#              |  '.   _.+.,."   |              (R) red
#              |   _\-",-' ",    |              (Y) yellow
#              |_-" "+'      ",  |              (G) green
#        (GOW)+{   (GRY)       ".|              (B) blue
#               \    |          ,+(BOY)         (O) orange
#                ".  |      ,-'                 
#                  \ |   ,-'                    The allowed corners are in the diagram to the left based on how a real-life Pocket cube
#                   \|,-'                       is coloured. Arrange these 8 corners in any order to scramble your own cube like this...
#                    +                          
#                  (GOY)                        ["GRW", "GRY", "GOY", "GOW", "BOW", "BOY", "BRY", "BRW"]  
#                                               
#      {{{DESIGNED by JOHNNY MADIGAN}}}         As long as you use these 8 corners (no duplicates) the function will know it's a real
#                                               cube and start solving it so it can let you know the minimum number of moves it took.
#
#____________________________________________________________________________________________________________________________________________
#
#                                               If you have a Pocket Cube in real-life and want to import it here, please follow these steps:
#
#                                               1. Choose any side of your cube in real-life and starting from the bottom-left corner, go 
#                                                  clockwise and note the colours of each corner. For example...
# 
#                                                       Starting from bottom-left "GRW" go up to top-left "GRY" then  
#                                                       go right to top-right "GOY" and finally go down to bottom-right "GOW"
#
#                                               2. Now spin your cube around so you're looking at the opposite face (horizontally 180 degrees)
#                                                  and repeat, remember to start from the bottom-left corner and go clockwise!
#
#                                               3. That's it! don't worry about case and the order you wrote the colour's letters down as the 
#                                                  function is smart enough to recognise the unique corner. For example...
#
#                                                       "BOY" is equivalent to "YOB", "bOy", "ByO" and so on... 
#                                                       (the function knows this corner is unique with Blue, Orange and Yellow)
#
#
#
#                                                   TODO (I might make a scrambler function in the future but for now it's out-of-scope for the assignment)
