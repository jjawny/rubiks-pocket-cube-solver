![year](https://img.shields.io/badge/Year-2021-lightgrey?style=plastic)
![author](https://img.shields.io/badge/Author-Johnny%20Madigan-yellow?style=plastic)
![python version](https://img.shields.io/badge/Python-informational?style=plastic&logo=python)

- [About](#about)
- [Usage](#usage)
- [How to run via the terminal](#how-to-run-via-the-terminal)
- [How to run via *Visual Studio Code*](#how-to-run-via-visual-studio-code)
- [Call Graph](#call-graph)
- [Dependencies](#dependencies)

# **About**
### **A GRAPH THEORY PROJECT**
A Graph Theory project, demonstrating my skills in using math/logic to solve real-world problems. The chosen problem is that Rubik's cubes are often solved in the shortest amount of time, not the least amount of moves. This Python script first generates a Cayley Graph, then uses distance classes and a Breadth-First Search algorithm to find the shortest path between any scrambled cube and the solved state. First, the cube is encoded in **Python**, the problem is translated to mathematical language, then finally functions handle the large amount of data in a clever yet sophisticated way to solve the problem.

Please see my report for more details.

![project animation](/img/ezgif-demonstration.gif)

# **Usage**
### **GUIDE TO USING READY-MADE CUBES**
CopyPaste one of the encoded cubes below into the *'instance'* variable in *main.py* to solve using the program.

```python
"WSDAWKLDM33ML3MDSLKCMDLE"  # x  illegal cube
"WWWWGGGGRRRRBBBBOOOOYYYY"  # 0  steps - already solved
"WWBBGWGWRRRRYBYBOOOOGGYY"  # 1  step
"wwbbgwgwrrrrybyBOOOOGGYY"  # 1  step again (case-insensitive)
"WWROGGOWYWRGBRYRBOBBGOYY"  # 6  steps
"WYYYGGOBOORYBRRWGORWWBBG"  # 9  steps
"WRYGGGOBOYRYRWBRGOBWWOBY"  # 10 steps - harder cube, only found after generating half a million permutations
```
```python
instance = "WWROGGOWYWRGBRYRBOBBGOYY"
```

### **GUIDE TO USING YOUR OWN CUBES**
Rubik's Pocket Cube has 6 faces and 24 stickers (4 per face). When solved each face is a single colour, the colours are...

![colours](/img/colours.png)

Choose any face from your cube and draw a diagram out like this:

```
        ┌───┬───┐
        │ 1 │ 2 │
        ├───┼───┤
        │ 3 │ 4 │
┌───┬───┼───┼───┼───┬───┬───┬───┐
│ 5 │ 6 │ 9 │10 │ 13│14 │ 17│18 │
├───┼───┼───┼───┼───┼───┼───┼───┤
│ 7 │ 8 │ 11│12 │ 15│16 │ 19│20 │
└───┴───┼───┼───┼───┴───┴───┴───┘
        │ 21│22 │
        ├───┼───┤
        │ 23│24 │
        └───┴───┘
```

Finally, follow the order in the diagram and note down the colour of the 24 stickers and you should end up with something like this:

```python
"WYYYGGOBOORYBRRWGORWWBBG"
```
### **GUIDE TO USING DOCSTRINGS**
CopyPaste the following commands into *main.py* to get details on what each function does.

```python
print("SOLUTION:" + project.solution.__doc__)
print("PRINT SOLUTION:" + project.printSolution.__doc__)
print("BREADTH-FIRST SEARCH:" + project.breadthFirst.__doc__)
```

# **How to run via the Terminal**
- Run with
   ```sh
   python3 main.py
   ```

# **How to run via *Visual Studio Code***
- Download *VScode*: https://code.visualstudio.com
- Follow the *Getting Started with Python* guide: https://code.visualstudio.com/docs/python/python-tutorial
- Launch *VScode*
- Select *Python* Interpreter version 2.7 or 3.8 or 3.9
- Open main.py in *VScode* and click run

![run button](/img/run-button.png)

# **Call Graph**

![pyan3 generated call graph](/img/cube-solver-pyan3-call-graph.png)

# **Dependencies**
**Python** Interpreter versions 2.7, 3.8, and 3.9 have been proven to compile as of writing this.
