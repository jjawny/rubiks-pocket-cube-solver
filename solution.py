#████████╗███████╗░██████╗████████╗  ██████╗░░█████╗░████████╗░█████╗░
#╚══██╔══╝██╔════╝██╔════╝╚══██╔══╝  ██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗
#░░░██║░░░█████╗░░╚█████╗░░░░██║░░░  ██║░░██║███████║░░░██║░░░███████║
#░░░██║░░░██╔══╝░░░╚═══██╗░░░██║░░░  ██║░░██║██╔══██║░░░██║░░░██╔══██║
#░░░██║░░░███████╗██████╔╝░░░██║░░░  ██████╔╝██║░░██║░░░██║░░░██║░░██║
#░░░╚═╝░░░╚══════╝╚═════╝░░░░╚═╝░░░  ╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝

#testData = ["GRW", "GRY", "GOY", "GOW", "BOW", "BOY", "BRY", "zzz"] # expecting warning msg (no such corner ZRW)
#testData = ["GRW", "GRY", "GOY", "GOW", "BOW", "BOY", "BRY", "BRW"] # expecting 0 steps (cube already solved)
#testData = ["GRY", "BRY", "GOY", "GOW", "BOW", "BOY", "BRW", "GRW"] # expecting 1 steps (applied 1 legal move)
#testData = ["GRY", "BRY", "OGY", "OGW", "OBW", "OBY", "BRW", "GRW"] # expecting 1 steps (same as above except not in alphabetical order)
#testData = ["BRW", "GOW", "GRY", "GOY", "BOW", "BOY", "GRW", "BRY"] # expecting 2 steps (applied 2 legal moves)
#testData = ["brW", "GOw", "grY", "GOY", "bow", "BOY", "GRW", "bry"] # expecting 2 steps (same as above but not uppercase)
#testData = ["BOW", "BRW", "GRY", "GOY", "BRY", "BOY", "GOW", "GRW"] # expecting 6 steps (randomly put corners together)
testData = ["OBW", "BRY", "OGW", "BRW", "GRW", "GRY", "OBY", "OGY"] # expecting 5 steps (test data from section 6 of assignment pdf)

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

def solution(problemCube):    
    solvedCube = "GRWGRYGOYGOWBOWBOYBRYBRW" # starting cube & starting vertex for distance classes

    legalCorners = ["GRW", "GRY", "GOY", "GOW", "BOW", "BOY", "BRY", "BRW"]
    legalMoves = [
        [3,0,1,2,4,5,6,7],  # F  = face clockwise
        [1,2,3,0,4,5,6,7],  # F' = face anti-clockwise
        [1,6,2,3,4,5,7,0],  # U  = up clockwise
        [7,0,2,3,4,5,1,6],  # U' = up anti-clockwise
        [0,6,1,3,4,2,5,7],  # R  = right clockwise
        [0,2,5,3,4,6,1,7]]  # R' = right anti-clockwise

    # sort the problem cube's corner's colours in alphabetical order & make them all uppercase for consistency
    # when sorting, we will only save the corners that are a member of the 8 legal corners (regardless of position)
    afterSorted = [[("".join(sorted(corner.upper()))) for legalCorner in legalCorners if legalCorner == ("".join(sorted(corner.upper())))]for corner in problemCube]
    afterSorted = [item for sublist in afterSorted for item in sublist] # flatten to remove nested lists

    # if not all 8 legal corners are found, the problem cube instance is invalid
    if len(afterSorted) < 8: 
        print("Invalid problem cube, please make sure you use the right corners in your string")
        return [{}]

    # get a list of the same problem cube but from different POVs (when looking at the 8 corners) keeps them in sequence which is crucial
    sortedProblemCube = "".join(afterSorted)
    problemCubes = [sortedProblemCube[-3*view:] + sortedProblemCube[:-3*view] for view in range(6)]

    found = False           # store the found problem cube (any 1 out of 8 of the POVs) also a flag
    toRotate = {solvedCube} # next set of parent cubes to rotate (starts off with the solved cube)
    temporary = set()       # temporary holding for next set of cubes to be rotated next after current rotations are done
    V = set()               # vertices are cubes
    E = set()               # edges are parent-child relationships (parent cube and it's 6 children cubes, 1 after each legal move rotation)

    while not found:
        for cube in problemCubes:
            # if problem cube is found, get the set of distance classes
            # save the problem cube in the distances data structure, will be popped in printSolution()
            if cube in V:
                distances = distanceClasses(V, E, solvedCube)
                distances.insert(len(distances),cube)
                return(distances)

        print("searching...")  # let the user know the program is running
        for cube in toRotate:
            # for the 6 legal moves, ensure the corners are moved in groups of threes (also makes legalMoves[] 8x smaller)
            # apply a legal move to create the new permitation
            for move in range(6): 
                splitCorners = [cube[i:i+3] for i in range(0, len(cube), 3)]
                newCube = ''.join([splitCorners[i] for i in legalMoves[move]])
                # add new vertex (cube), new edges (parent-child relationships), and save the cube temporarily to be rotated next time 
                V.add(newCube)
                E.add((newCube, cube))
                E.add((cube, newCube))
                temporary.add(newCube)

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

def printSolution(distances):
    problemCube = distances.pop() # remove the problem cube
    for d in distances:
        if problemCube in d:
            index = distances.index(d)
            if index == 0: 
                print("Cube already solved!")
            else:
                print("Minimum number of steps to solve your cube are {0} steps!".format(index))

printSolution(solution(testData))

#                      (BRW)                    GUIDE TO SCRAMBLING YOUR OWN CUBE: (I might make a scrambler function in the future)
#                        +                         
#                     _.-"-,                    A pocket cube (2x2x2) is made of 8 corner pieces that are all
#                _.-""   |  ',                  unique in the way that each corner has a different combination
#        (GRW)+:"        |    ',                of 3 colours (out of six). These colours are...
#              |\        |      '.+(BRY)
#              | \     (BOW)  _."|              (W) white
#              |  '.   _.+.,."   |              (R) red
#              |   _\-",-' ",    |              (Y) yellow
#              |_-" "+'      ",  |              (G) green
#        (GOW)+{   (GRY)       ".|              (B) blue
#               \    |          ,+(BOY)         (O) orange
#                ".  |      ,-'                   #TODO fix the input to [www, www, www, www]
#                  \ |   ,-'                    The allowed corners are in the diagram to the left based on how a
#                   \|,-'                       real pocket cube is coloured. Combine these into a single string
#                    +                          to make a cube like this... "GRYOBYOBWBRYBRWGRWOGWOGY". As long as 
#                  (GOY)                        you never split these combinations apart, it means your scrambled 
#                                               cube can exist in real-life and therefore the program can solve it
#    DESIGNED & PROGRAMMED BY JOHNNY MADIGAN    to let you know the minimum number of steps you'd need.
