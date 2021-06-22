#                                   .x88888x.            x*8888x.:*8888: -"888;
#                                  :8**888888X.  :>     X   48888X/`8888H/`8888H
#                                  f    `888888x./     X8x.  8888X  8888X  8888X;
#                                 '       `*88888~     X8888 X8888  88888  88888;
#                                  \.    .  `?)X.      '*888!X8888  X8888  X8888;
#                                   `~=-^   X88> ~       `?8 `8888  X888X  X888X
#                                          X8888  ~      ~"  '888"  X888   X888
#                                          488888           !888;  !888;  !888;
#                                  .xx.     88888X         888!   888!   888!
#                                 '*8888.   '88888>       88"    88"    88"
#                                   88888    '8888>        "~     "~     "~
#                                   `8888>    `888                           
#                                    "8888     8%     johnny.madigan@icloud.com
#                                     `"888x:-"    https://johnnymadigan.github.io/

import project

# UNCOMMENT BELOW FOR DOCSTRINGS
#print("What does 'solution()' do?\n" + project.solution.__doc__)
#print("What does 'breadthFirst()' do?\n" + project.breadthFirst.__doc__)
#print("What does 'printSolution()' do?\n" + project.printSolution.__doc__)

# COPY & PASTE ENCODED CUBES INTO THE "instance" VARIABLE
#WSDAWKLDM33ML3MDSLKCMDLE  x  illegal cube
#WWWWGGGGRRRRBBBBOOOOYYYY  0  steps already solved
#WWBBGWGWRRRRYBYBOOOOGGYY  1  step cube
#wwbbgwgwrrrrybyBOOOOGGYY  1  step cube again (case-insensitive)
#OBBBWWRORRBYYYOGOGWGWGYR  6  step cube
#WYYYGGOBOORYBRRWGORWWBBG  9  step cube
#WRYGGGOBOYRYRWBRGOBWWOBY  10 step cube (harder cube, only found after generating half a million permutations)

instance = "OBBBWWRORRBYYYOGOGWGWGYR"
solution = project.solution(instance)

project.printSolution(solution)

#                                                               GUIDE TO USING YOUR OWN CUBE
#                                                        
#                     _.-",                     Rubik's Pocket Cube has 6 faces and 24 stickers (4 per face). 
#                _.-"\     '.                   When solved each face is a single colour, the colours are...
#              {"     \    .-",                
#              |\      \_."    '.               (W) white, (R) red, (Y) yellow, (G) green, (B) blue, (O) orange
#              | \ _.-" '\     _.|              
#              |  |\      \ _."  |              Choose any face from your cube and draw a diagram out like this:
#              |\ | \    _.\     |                                      +-------+
#              | \|  +,-"  |  _.-|                                      |  1 2  |
#              {  |\ |    _|-"   |                                      |  3 4  |
#               \ | \|_.-" |   _,'                              +-------+-------+-------+-------+
#                \|  |     |,-'                                 |  5 6  |  9 10 | 13 14 | 17 18 |
#                 '\ |   ,-'                                    |  7 8  | 11 12 | 15 16 | 19 20 |
#                   \|,-'                                       +-------+-------+-------+-------+
#                                                                       | 21 22 |
#          DEVELOPED by JOHNNY MADIGAN                                  | 23 24 |
#          a Graph Theory project for                                   +-------+
#          CAB203 Discrete Structures           Finally, follow the order in the diagram and note down the colour
#                                               of the 24 stickers and you should end up with something like this: 
#
#                                                                  "OBBBWWRORRBYYYOGOGWGWGYR"
