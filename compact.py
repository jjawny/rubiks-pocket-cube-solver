def solution(problemCube):    
    solvedCube = "GRWGRYGOYGOWBOWBOYBRYBRW"; legalCorners = ["GRW", "GRY", "GOY", "GOW", "BOW", "BOY", "BRY", "BRW"]; legalMoves = [[3,0,1,2,4,5,6,7], [1,2,3,0,4,5,6,7], [1,6,2,3,4,5,7,0], [7,0,2,3,4,5,1,6], [0,6,1,3,4,2,5,7], [0,2,5,3,4,6,1,7]]; afterSorted = [item for sublist in [[("".join(sorted(corner.upper()))) for legalCorner in legalCorners if legalCorner == ("".join(sorted(corner.upper())))]for corner in problemCube] for item in sublist]
    if len(afterSorted) < 8: print("Invalid problem cube, please make sure you use the right corners in your string"); return [{}]
    sortedProblemCube = "".join(afterSorted); problemCubes = [sortedProblemCube[-3*view:] + sortedProblemCube[:-3*view] for view in range(6)]; found = False; toRotate = {solvedCube}; temporary = set(); V = set(); E = set()
    while not found:
        solution = [((distanceClasses(V, E, solvedCube)), cube) for cube in problemCubes if cube in V]
        if solution: return solution[0]
        print("searching...")
        for cube in toRotate:
            for move in range(6): splitCorners = [cube[i:i+3] for i in range(0, len(cube), 3)]; newCube = ''.join([splitCorners[i] for i in legalMoves[move]]); temporary.add(newCube); V.add(newCube); E.add((newCube, cube)); E.add((cube, newCube))
        V = V.union(toRotate); toRotate = temporary; temporary = set()




#11 lines c:



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

def printSolution(data):
    [print("Cube already solved!") if data[0].index(distance) == 0 else print("Minimum number of steps to solve your cube are {0} steps!".format(data[0].index(distance))) for distance in data[0] if data[1] in distance]



#testData = ["GRW", "GRY", "GOY", "GOW", "BOW", "BOY", "BRY", "BRW"] # expecting 0 steps (cube already solved)

testData = ["OBW", "BRY", "OGW", "BRW", "GRW", "GRY", "OBY", "OGY"] # expecting 5 steps (test data from section 6 of assignment pdf)
printSolution(solution(testData))
