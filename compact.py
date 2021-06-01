def solution(instance):    
    solvedCube = "WWWWGGGGRRRRBBBBOOOOYYYY"; instance = instance.upper(); pCubes = set(); legalMoves = [[0,1,7,5,4,20,6,21,10,8,11,9,2,13,3,15,16,17,18,19,14,12,22,23], [0,1,12,14,4,3,6,2,9,11,8,10,21,13,20,15,16,17,18,19,5,7,22,23], [0,1,2,3,4,5,18,19,8,9,6,7,12,13,10,11,16,17,14,15,22,20,23,21], [0,1,2,3,4,5,10,11,8,9,14,15,12,13,18,19,16,17,6,7,21,23,20,22], [0,9,2,11,4,5,6,7,8,21,10,23,14,12,15,13,3,17,1,19,20,18,22,16], [0,18,2,16,4,5,6,7,8,1,10,3,13,15,12,14,23,17,21,19,20,9,22,11]]; six = [[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23], [12,13,14,15,9,11,8,10,21,23,20,22,18,16,19,17,1,0,3,2,7,6,5,4], [8,9,10,11,5,7,4,6,20,21,22,23,14,12,15,13,3,2,1,0,19,18,17,16], [20,21,22,23,7,6,5,4,19,18,17,16,15,14,13,12,9,8,11,10,0,1,2,3], [4,5,6,7,17,19,16,18,22,20,23,21,10,8,11,9,2,0,3,1,15,14,13,12], [16,17,18,19,13,15,12,14,23,22,21,20,6,4,7,5,0,1,2,3,11,10,9,8]]; four = [[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23], [2,0,3,1,8,9,10,11,12,13,14,15,16,17,18,19,4,5,6,7,21,23,20,22], [3,2,1,0,12,13,14,15,16,17,18,19,4,5,6,7,8,9,10,11,23,22,21,20], [1,3,0,2,16,17,18,19,4,5,6,7,8,9,10,11,12,13,14,15,22,20,23,21]]
    if not sorted(solvedCube) == sorted(instance): print("Invalid scrambled cube, please make sure you have 4 of each colours"); return ({}, None)
    if solvedCube == instance: return ([{solvedCube}], solvedCube)
    for rot in range(0,len(six)):newOrientation = ''.join([instance[i] for i in six[rot]]); [pCubes.add(''.join([newOrientation[i] for i in four[spin]])) for spin in range(0, len(four))]
    toRotate = {solvedCube}; temporary = set(); E = set(); V = set(); print("\nsearching...\n")
    while not pCubes.intersection(V):
        for cube in toRotate:
            for move in range(0,len(legalMoves)): newCube = ''.join([cube[i] for i in legalMoves[move]]); temporary.add(newCube); V.add(newCube); E.update(((newCube, cube),(cube, newCube)))
            for c in pCubes: 
                if c in V: print("Found instance after {:,} permutations\n".format(len(V))); return ((distanceClasses(V, E, solvedCube)), c)
        toRotate = temporary; temporary = set(); print("Total permutations so far... {:,}".format(len(V)))


#                                                    12 lines c:






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
#                                                                       +-------+
#                                               Finally, follow the order in the diagram above and note down the colour
#                                               of the 24 stickers and you should end up with something like this: 
#
#                                                                   WWBBGWOORRGWYBRROOYBYGYG
