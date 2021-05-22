#████████╗███████╗░██████╗████████╗  ██████╗░░█████╗░████████╗░█████╗░
#╚══██╔══╝██╔════╝██╔════╝╚══██╔══╝  ██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗
#░░░██║░░░█████╗░░╚█████╗░░░░██║░░░  ██║░░██║███████║░░░██║░░░███████║
#░░░██║░░░██╔══╝░░░╚═══██╗░░░██║░░░  ██║░░██║██╔══██║░░░██║░░░██╔══██║
#░░░██║░░░███████╗██████╔╝░░░██║░░░  ██████╔╝██║░░██║░░░██║░░░██║░░██║
#░░░╚═╝░░░╚══════╝╚═════╝░░░░╚═╝░░░  ╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝

#testData = ["GRW", "GRY", "GOY", "GOW", "BOW", "BOY", "BRY", "zzz"] # expecting warning msg (no such corner "zzz")
#testData = ["GRW", "GRY", "GOY", "GOW", "BOW", "BOY", "BRY", "BRW"] # expecting 0 steps (cube already solved)



#testData = ["BRY", "GRW", "BOW", "GOW", "BRW", "GOY", "BOY", "GRY"]  #rotated 11x expecting 11 steps
#              BOY   GRY     BRY     GRW     BOW     GOW     BRW     GOY 
#testData = ["GOW","BRY", "GRY", "BOY", "BOW", "BRW", "GOY", "GRW"] closest so far 7 moves of CAB230 data
#testData = ["GRY", "BRW", "GOY", "GOW", "BOW", "BOY", "GRW", "BRY"] #most accurate still 7 but kept corner 4 fixed and every corner relevant to it (GOW is at position 4 just like solved cube, aka pivot point)
#testData = ["WGR", "RGY", "OYB", "YGO", "BOW", "BRY", "GOW", "BWR"] # going off at looking at the coloured cube then manually mapping out...



#testData = "GB    'W'    RY   'G'   OG   'R'     BRWWOGBWOYBYOYR"
#testData = WW    'W'    WG   'G'   GG   'R'     RRRBBBBOOOOYYYY

#testData = ["GRY", "BRY", "GOY", "GOW", "BOW", "BOY", "BRW", "GRW"] # expecting 1 steps (applied 1 legal move)
#testData = ["GRY", "BRY", "OGY", "OGW", "OBW", "OBY", "BRW", "GRW"] # expecting 1 steps (same as above except not in alphabetical order)
#testData = ["BRW", "GOW", "GRY", "GOY", "BOW", "BOY", "GRW", "BRY"] # expecting 2 steps (applied 2 legal moves)
#testData = ["brW", "GOw", "grY", "GOY", "bow", "BOY", "GRW", "bry"] # expecting 2 steps (same as above but not uppercase)
#testData = ["BOW", "BRW", "GRY", "GOY", "BRY", "BOY", "GOW", "GRW"] # expecting 6 steps (randomly put corners together)
##testData = ["OBW", "BRY", "OGW", "BRW", "GRW", "GRY", "OBY", "OGY"] # expecting 11 steps (test data from section 6 of assignment pdf)
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

            #GBWRYGOGRBRWWOGBYBWOYOYR
#testData = "GBWRYGOGRBRWWOGBWOYBYOYR" #correct test data from lec and oriented correctly
#testData = "WWWWGGGGRRRRBBBBOOOOYYYY" #solved 
#testData = "WRRBGGOYYYOROWWRGOBWGBBY" #rotated manually
#testData = "WWBBGWGWRRRRYBYBOOOOGGYY" #rotated U'








#testData = "YGOGOBWYYYRORRWBWGRBBGOW" #same as above but not oriented correctly #  GBWRYGOGRBRWWOGBYBWOYOYR IT WORKS

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

#WYBWGRGWYRRWBROBGOOOGBYY 5 rotations    3746 unique permutations
#WYBWGROOYRGWBRRWGOOBYGYB 6 rotations  17,646 unique permutations
#WYBWGROBYROOBRGWGORWYYBG 7            82,150 unique permutations
#WYBRGYOYOYORBRWWGORWGBBG 8           379,426 unique permutations
#WYYYGGOBOORYBRRWGORWWBBG 9         1,739,310 unique permutations
#WRYGGGOBOYRYRWBRBOGWWOBY 10        7,892,305 unique permutations
#WRRBGGOYYYOROWWRBOGWGBBY 11        ...
#check if same perm but just rotated before adding to V
testData = "WRYGGGOBOYRYRWBRBOGWWOBY"

def solution(problemCube):    
    solvedCube = "WWWWGGGGRRRRBBBBOOOOYYYY"
    #solvedCube = "ABCDEFGHIJKLMNOPQRSTUVWX"


    if not sorted(solvedCube) == sorted(problemCube):
        print("Invalid scrambled cube, please make sure you have 4 of each colours")
        return [{}]

    # orient cube so we dont have to worry about rotations
    rotations = [
        [1,3,0,2,16,17,18,19,4,5,6,7,8,9,10,11,12,13,14,15,22,20,23,21], # RIGHT
        [2,0,3,1,8,9,10,11,12,13,14,15,16,17,18,19,4,5,6,7,21,23,20,22], # LEFT
        [8,9,10,11,5,7,4,6,20,21,22,23,14,12,15,13,3,2,1,0,19,18,17,16], # UP
        [18,19,16,17,6,4,7,5,0,1,2,3,13,15,12,14,23,22,21,20,8,9,10,11]] # DOWN

    toRotate = {problemCube}
    nextSet = set()
    rotatedproperly = False
    finalProblemCube = ""
    #while not rotatedproperly:
    #    print("rotating")
    #    for cube in toRotate:
    #        if cube[2] == 'C' and cube[5] == 'F' and cube[8] == 'I':
    #            finalProblemCube = cube
    #            rotatedproperly = True
    #            break
    #        else:
    #            for rot in range(0,4):
    #                newCube = ''.join([cube[i] for i in rotations[rot]])
    #                nextSet.add(newCube)
    #    toRotate = nextSet
    #    nextSet = set()

    # legal moves
    legalMoves = [
        [0,1,7,5,4,20,6,21,10,8,11,9,2,13,3,15,16,17,18,19,14,12,22,23], # U    up clockwise
        [0,1,12,14,4,3,6,2,9,11,8,10,21,13,20,15,16,17,18,19,5,7,22,23], # U'   up anti-clockwise
        [0,1,2,3,4,5,18,19,8,9,6,7,12,13,10,11,16,17,14,15,22,20,23,21], # F    front clockwise
        [0,1,2,3,4,5,10,11,8,9,14,15,12,13,18,19,16,17,6,7,21,23,20,22], # F'   front anti-clockwise
        [0,9,2,11,4,5,6,7,8,21,10,23,14,12,15,13,3,17,1,19,20,18,22,16], # R    right clockwise
        [0,18,2,16,4,5,6,7,8,1,10,3,13,15,12,14,21,17,23,19,20,9,22,11]] # R'   right anti-clockwise

    toRotate = {solvedCube} # next set of parent cubes to rotate (starts off with the solved cube)
    temporary = set()       # temporary holding for next set of cubes to be rotated next after current rotations are done
    V = set()               # vertices are cubes
    E = set()               # edges are parent-child relationships (parent cube and it's 6 children cubes, 1 after each legal move rotation)
    

#turn UP 90 anti               U'
#turn RIGHT 90 anti          R'
#turn UP  90x2            U U
#turn FRONT 90x2          F F
#turn TOP 90 clockwise       U
#turn FRONT 90 anti           F'
#turn RIGHT 90 anti            R'
#turn FRONT 90 clockwise        F
#turn TOP 90 anti                U'    1  2  5 3   0   2 2 0 0 5 1

    finalProblemCube = problemCube
    while finalProblemCube not in V:
        print("searching...")
        for cube in toRotate:
            for move in range(0,6):
                newCube = ''.join([cube[i] for i in legalMoves[move]])
                V.add(newCube)
                E.add((newCube, cube))
                E.add((cube, newCube))
                temporary.add(newCube)

        # reset
        V = V.union(toRotate)
        toRotate = temporary
        temporary = set()

    print("found it")
    print(finalProblemCube)
    print(len(V))
    return [{}]
    return ((distanceClasses(V, E, solvedCube)), finalProblemCube)



#██████╗░██████╗░██╗███╗░░██╗████████╗  ░██████╗░█████╗░██╗░░░░░██╗░░░██╗████████╗██╗░█████╗░███╗░░██╗
#██╔══██╗██╔══██╗██║████╗░██║╚══██╔══╝  ██╔════╝██╔══██╗██║░░░░░██║░░░██║╚══██╔══╝██║██╔══██╗████╗░██║
#██████╔╝██████╔╝██║██╔██╗██║░░░██║░░░  ╚█████╗░██║░░██║██║░░░░░██║░░░██║░░░██║░░░██║██║░░██║██╔██╗██║
#██╔═══╝░██╔══██╗██║██║╚████║░░░██║░░░  ░╚═══██╗██║░░██║██║░░░░░██║░░░██║░░░██║░░░██║██║░░██║██║╚████║
#██║░░░░░██║░░██║██║██║░╚███║░░░██║░░░  ██████╔╝╚█████╔╝███████╗╚██████╔╝░░░██║░░░██║╚█████╔╝██║░╚███║
#╚═╝░░░░░╚═╝░░╚═╝╚═╝╚═╝░░╚══╝░░░╚═╝░░░  ╚═════╝░░╚════╝░╚══════╝░╚═════╝░░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚══╝

def printSolution(data):
    print("made it to print solution")
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
