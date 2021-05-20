#████████╗███████╗░██████╗████████╗  ██████╗░░█████╗░████████╗░█████╗░
#╚══██╔══╝██╔════╝██╔════╝╚══██╔══╝  ██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗
#░░░██║░░░█████╗░░╚█████╗░░░░██║░░░  ██║░░██║███████║░░░██║░░░███████║
#░░░██║░░░██╔══╝░░░╚═══██╗░░░██║░░░  ██║░░██║██╔══██║░░░██║░░░██╔══██║
#░░░██║░░░███████╗██████╔╝░░░██║░░░  ██████╔╝██║░░██║░░░██║░░░██║░░██║
#░░░╚═╝░░░╚══════╝╚═════╝░░░░╚═╝░░░  ╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝

#testData = "GRWGRYGOYGOWBOWBOYBRYzrw" # expecting warning msg (no such corner ZRW)
#testData = "GRWGRYGOYGOWBOWBOYBRYBRW" # expecting 0 steps (cube already solved)
#testData = "GRYBRYGOYGOWBOWBOYBRWGRW" # expecting 1 steps (applied 1 legal move)
#testData = "GRYBRYOGYOGWOBWOBYBRWGRW" # expecting 1 steps (same as above except not in alphabetical order)
#testData = "BRWGOWGRYGOYBOWBOYGRWBRY" # expecting 2 steps (applied 2 legal moves)
#testData = "brWGOwgrYGOYbowBOYGRWbry" # expecting 2 steps (same as above but not uppercase)
#testData = "BOWBRWGRYGOYBRYBOYGOWGRW" # expecting 6 steps (randomly put corners together)
testData = "OBWBRYOGWBRWGRWGRYOBYOGY" # expecting 5 steps (test data from section 6 of assignment pdf)

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
    solvedCube = "GRWGRYGOYGOWBOWBOYBRYBRW" # starting cube (each corner's colours are in alphabetical order)

    # check if the problem cube argument is a valid scrambled (or solved) cube
    problemCube = problemCube.upper()
    splitProblemCube = [problemCube[i:i+3] for i in range(0, len(problemCube), 3)] # split string into groups of 3 (corners)

    legalCorners = ["GRW", "GRY", "GOY", "GOW", "BOW", "BOY", "BRY", "BRW"]
    afterSorted = list()
    
    for corner in splitProblemCube:
        for legalCorner in legalCorners:
            sortedCorner = "".join(sorted(corner))
            if sortedCorner == legalCorner:
                afterSorted.append(sortedCorner)
    
    if len(afterSorted) < 8: # if not all corners are found, display warning msg
        print("Invalid problem cube, please make sure you use the right corners in your string")
        return [{}]

    sortedProblemCube = "".join(afterSorted)

    # get the same problem cube but from different POVs (when looking at the 8 corners) keeps them in sequence which is crucial
    problemCubes = [sortedProblemCube[-3*view:] + sortedProblemCube[:-3*view] for view in range(6)]
    
    #OLD for the above
    #problemCubes = list()
    #for view in range(6):
    #    problemCubes.append(sortedProblemCube[-3*view:] + sortedProblemCube[:-3*view])

    legalMoves = [
        [3,0,1,2,4,5,6,7],  # F  = face clockwise
        [1,2,3,0,4,5,6,7],  # F' = face anti-clockwise
        [1,6,2,3,4,5,7,0],  # U  = up clockwise
        [7,0,2,3,4,5,1,6],  # U' = up anti-clockwise
        [0,6,1,3,4,2,5,7],  # R  = right clockwise
        [0,2,5,3,4,6,1,7]]  # R' = right anti-clockwise

    V = set()               # vertices are cubes
    E = set()               # edges are parent-child relationships (parent cube and it's 6 children cubes, 1 after each legal move rotation)
    toRotate = {solvedCube} # next set of parent cubes to rotate (starts off with the solved cube)
    temporary = set()       # temporary holding for next set of cubes to be rotated next after current rotations are done
    found = False           # flag for when the given problem cube is found
    foundProblemCube = None # store the found problem cube as it's the one we will use to get the number of steps

    while not found:
        for cube in problemCubes:
            if cube in V:
                foundProblemCube = cube
                found = True
                break

        print("searching...")  # let the user know the program is running as it can take some time...
        for cube in toRotate:
            for move in range(6): # for 6 legal moves
                splitCorners = [cube[i:i+3] for i in range(0, len(cube), 3)] # ensures corners are moved in groups of 3 (also makes legalMoves 8x smaller)
                newCube = ''.join([splitCorners[i] for i in legalMoves[move]]) # apply move & create new permitation
                
                V.add(newCube) # save new permitation as a vertex (does not add duplicates)
                temporary.add(newCube) # temporarily save new permitation to be rotated next time
                E.add((newCube, cube)) # save relationship edge
                E.add((cube, newCube)) # save reverse edge as graph is un-directed (also to avoid maximum recursion depth error)

        V = V.union(toRotate) # save all parent cubes as vertices
        toRotate = temporary
        temporary = set()

    distances = distanceClasses(V, E, solvedCube) # get the set of distances
    distances.insert(len(distances),foundProblemCube) # save the problem cube in the data structure, will be popped in printSolution()
    return(distances)

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
#              | \     (BOW)  _."|              (W) red
#              |  '.   _.+.,."   |              (R) yellow
#              |   _\-",-' ",    |              (Y) white
#              |_-" "+'      ",  |              (G) green
#        (GOW)+{   (GRY)       ".|              (B) blue
#               \    |          ,+(BOY)         (O) orange
#                ".  |      ,-'                   
#                  \ |   ,-'                    The allowed corners are in the diagram to the left based on how a
#                   \|,-'                       real pocket cube is coloured. Combine these into a single string
#                    +                          to make a cube like this... "GRYOBYOBWBRYBRWGRWOGWOGY". As long as 
#                  (GOY)                        you never split these combinations apart, it means your scrambled 
#                                               cube can exist in real-life and therefore the program can solve it
#    DESIGNED & PROGRAMMED BY JOHNNY MADIGAN    to let you know the minimum number of steps you'd need.




# TESTING ONLY TO BE REMOVED BEFORE SUBMITTING
# to rotate the cube must be done in solve function
#
# splitCorners = [solvedCube[i:i+3] for i in range(0, len(solvedCube), 3)]
# print(splitCorners)
# print(''.join([splitCorners[i] for i in legalMoves[2]]))