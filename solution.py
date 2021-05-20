def solve(problemCube):
    #OLD unique 24 stickers = "ABCDEFGHIJKLMNOPQRSTUVWX"
    #OLD colours solvedCube = "GGGGRRRRBBBBOOOOWWWWYYYY"
    #OLD colours corners solvedCube = "GRWGRYOGYOGWOBWOBYBRYBRW"
    #solvedCube = "LFULFDBLDBLUBRUBRDRFDRFU"
    solvedCube = "GRWGRYOGYOGWOBWOBYBRYBRW"
    #8 corners solvedCube = "111222333444555666777888"

    legalMoves = [
        [3,0,1,2,4,5,6,7], #R
        [1,2,3,0,4,5,6,7], #R'
        [7,0,2,3,4,5,1,6], #U
        [1,6,2,3,4,5,7,0], #U'
        [0,2,5,3,4,6,1,7],
        [0,6,1,3,4,2,5,7]]

    V = set() #cubes
    E = set() #edges between cubes
    toRotate = {solvedCube} #temporary holding, starts off with the solvedCube
    temporary = set()

    #splitCorners = [problemCube[i:i+3] for i in range(0, len(problemCube), 3)]
    #print(''.join([splitCorners[i] for i in legalMoves[2]]))

    found = False
    while not found:
        if problemCube in V:
            found = True
            print("WE FOUND IT")
            print(V)
            print(problemCube)
            break

        print("looking for problem")
        for cube in toRotate:
            for move in range(0,6):
                splitCorners = [cube[i:i+3] for i in range(0, len(cube), 3)] #ensures corners are moved in groups of 3 also makes the algorithms above so much nicer
                newCube = ''.join([splitCorners[i] for i in legalMoves[move]])
                
                print(splitCorners)
                print(cube)
                print(newCube)

                V.add(newCube) #add new permitation (does not add duplicates)
                temporary.add(newCube) #add children cubes to temporary as we will rotate them in the next
                E.add((newCube, cube)) #add edge
                E.add((cube, newCube)) #to avoid maximum recursion depth as this graph is un-directed

        V = V.union(toRotate) #
        toRotate = temporary #replaces to rotate with the temporary ones
        temporary = set() #reset

    dist = (distanceClasses(V, E, solvedCube))

    for d in dist:
        if problemCube in d:
            index = dist.index(d)
            message = "Minimum amount of steps to solve your cube is {0}!"
            print(message.format(index))
            return index







# this code works for directed or undirected graphs.  For directed graphs, paths follow same direction as edges (i.e. starting at out edges from starting point)
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




#RULE your cube MUST be these groups stringed together:
# GRWGRYOGYOGWOBWOBYBRY
# 
# LFU = GRW in colours
# LFD = GRY
# BLD = OGY
# BLU = OGW
# BRU = OBW
# BRD = OBY
# RFD = BRY
# RFU = BRW
#problemCube = "BLULFULFDBLDBRUBRDRFDRFU" #after 1 turns
#problemCube = "RFU BLU LFD BLD BRU BRD LFU RFD" #after 2 turns

#problemCube = "OGWGRWGRYOGYOBWOBYBRYBRW" #after 1 turns
problemCube = "BRWOGWGRYOGYOBWOBYGRWBRY" #after 2 turns
solve(problemCube)



#sooooo even with unique stickers, the issue is anyone can input an illegal cube
#as in, i just realised that a 2x2x2 cube can be viewed as 8 corners, with 3 stickers that always move TOGETHER
#this means that for example, stickers 1,2,3 represent a corner and should always stay together "xxx123xxxxxxxxxxx" and "xxxxxxxxxxx123xxx" etc
#however users can easily input "x1xxx2xxxx3xxxx" which completely destroys the program
#this file therefore refactors the program's algorithms for illegal moves...