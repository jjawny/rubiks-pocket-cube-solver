#████████╗███████╗░██████╗████████╗  ██████╗░░█████╗░████████╗░█████╗░
#╚══██╔══╝██╔════╝██╔════╝╚══██╔══╝  ██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗
#░░░██║░░░█████╗░░╚█████╗░░░░██║░░░  ██║░░██║███████║░░░██║░░░███████║
#░░░██║░░░██╔══╝░░░╚═══██╗░░░██║░░░  ██║░░██║██╔══██║░░░██║░░░██╔══██║
#░░░██║░░░███████╗██████╔╝░░░██║░░░  ██████╔╝██║░░██║░░░██║░░░██║░░██║
#░░░╚═╝░░░╚══════╝╚═════╝░░░░╚═╝░░░  ╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝

#testData = ["GRW", "GRY", "GOY", "GOW", "BOW", "BOY", "BRY", "zzz"] # expecting warning msg (no such corner "zzz")
#testData = ["GRW", "GRY", "GOY", "GOW", "BOW", "BOY", "BRY", "BRW"] # expecting 0 steps (cube already solved)
testData = ["GOY", "BRY", "BRW", "BOY", "BOW", "GRW", "GRY", "GOW"]  #rotated 11x expecting 11 steps

#testData = ["GRY", "BRY", "GOY", "GOW", "BOW", "BOY", "BRW", "GRW"] # expecting 1 steps (applied 1 legal move)
#testData = ["GRY", "BRY", "OGY", "OGW", "OBW", "OBY", "BRW", "GRW"] # expecting 1 steps (same as above except not in alphabetical order)
#testData = ["BRW", "GOW", "GRY", "GOY", "BOW", "BOY", "GRW", "BRY"] # expecting 2 steps (applied 2 legal moves)
#testData = ["brW", "GOw", "grY", "GOY", "bow", "BOY", "GRW", "bry"] # expecting 2 steps (same as above but not uppercase)
#testData = ["BOW", "BRW", "GRY", "GOY", "BRY", "BOY", "GOW", "GRW"] # expecting 6 steps (randomly put corners together)
##testData = ["OBW", "BRY", "OGW", "BRW", "GRW", "GRY", "OBY", "OGY"] # expecting 9 steps (test data from section 6 of assignment pdf)
#TODO testData above is completed in 5 steps... why :c
#turn UP 90 anti               U'
#turn RIGHT 90 anti          R'
#turn UP  90x2            U U
#turn FRONT 90x2          F F
#turn TOP 90 clockwise       U
#turn FRONT 90 anti           F'
#turn RIGHT 90 anti            R'
#turn FRONT 90 clockwise        F
#turn TOP 90 anti                U'

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
        print("Invalid problem cube, please make sure you use the allowed corners in your list")
        return [{}]

    # get a list of the same problem cube but from different POVs (when looking at the 8 corners) keeps them in sequence which is crucial
    sortedProblemCube = "".join(afterSorted)
    problemCubes = [sortedProblemCube[-3*view:] + sortedProblemCube[:-3*view] for view in range(8)]
    
    #testing only
    #splitCorners = [sortedProblemCube[i:i+3] for i in range(0, len(sortedProblemCube), 3)]
    #newCube = '", "'.join([splitCorners[i] for i in legalMoves[3]])
    #print(newCube)

    # add mirrored problem cubes
    for cube in problemCubes[:]:
        problemCubes.append(cube[::-1])

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
                return ((distanceClasses(V, E, solvedCube)), cube)

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

def printSolution(data):
    #problemCube = distances.pop() # remove the problem cube
    for distance in data[0]:
        if data[1] in distance:
            index = data[0].index(distance)
            if index == 0: 
                print("Cube already solved!")
            else:
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
