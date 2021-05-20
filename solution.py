def solve(problemCube):
    solvedCube = "GGGGRRRRBBBBOOOOWWWWYYYY"
    legalMoves = [
        [0,19,2,18,4,5,6,7,21,9,20,11,12,13,14,15,16,17,8,10,1,3,22,23],
        [0,20,2,21,4,5,6,7,18,9,19,11,12,13,14,15,16,17,3,1,10,8,22,23],
        [12,13,2,3,0,1,6,7,4,5,10,11,8,9,14,15,16,17,18,19,20,21,22,23],
        [4,5,2,3,8,9,6,7,12,13,10,11,0,1,14,15,16,17,18,19,20,21,22,23],
        [0,1,2,3,4,17,6,19,8,9,10,11,23,13,21,15,16,14,18,12,20,5,22,7],
        [0,1,2,3,4,21,6,23,8,9,10,11,19,13,17,15,16,5,18,7,20,14,22,12]]

    V = set() #cubes
    E = set() #edges between cubes
    toRotate = {solvedCube} #temporary holding, starts off with the solvedCube
    temporary = set()

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
                newCube = ''.join([cube[i] for i in legalMoves[move]])
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




#problemCube = "GWGWRRRRYBYBOOOOWWBBGGYY" #after 2 turns
problemCube = "OOGWGWRRRRYBYBOOWWBBGGYY" #after 1 turns
#problemCube = "OOGWGRWRRRYBYOBOWWBGBGYY" #after ? turns
solve(problemCube)



#sooooo it works if i rotate the cube to get the problem cube
#but not if i just place a bunch of random letter (sticking to the rules: colours (W,G,R,B,O,Y) and only 4 of each)
#it aint working