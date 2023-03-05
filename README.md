![year](https://img.shields.io/badge/2021-lightgrey?style=plastic)
![creators](https://img.shields.io/badge/Johnny%20Madigan-yellow?style=plastic)
![python](https://img.shields.io/badge/Python-9cf?style=plastic&logo=python)

# **CUBE SOLVER**
A graph theory project on finding the minimum number of moves to solve a Rubik's Pocket cube (2x2x2).

It is well known that people compete to solve Rubik's cubes in the shortest amount of time, but what about the least number of moves?

This Python script:
1. Takes the state of your scrambled cube (encoded)
2. Generates a Cayley Graph
3. Uses distance classes and BFS to find the shortest path to the solved state
4. Prints the minimum number of moves and the moves themselves

Please see my report for more details.

![project animation](/img/demonstration.gif)

# **How to solve a demo cube**
Copy one of the encoded cubes below:

```python
"WSDAWKLDM33ML3MDSLKCMDLE"  # x  illegal cube
"WWWWGGGGRRRRBBBBOOOOYYYY"  # 0  steps - already solved
"WWBBGWGWRRRRYBYBOOOOGGYY"  # 1  step
"wwbbgwgwrrrrybyBOOOOGGYY"  # 1  step again (case-insensitive)
"WWROGGOWYWRGBRYRBOBBGOYY"  # 6  steps
"WYYYGGOBOORYBRRWGORWWBBG"  # 9  steps
"WRYGGGOBOYRYRWBRGOBWWOBY"  # 10 steps - harder cube, only found after generating half a million permutations
```

Assign to the *'instance'* variable in *main.py*
```python
instance = "WWROGGOWYWRGBRYRBOBBGOYY"
```
Run: `python3 main.py`

# **How to solve your cube**
A Rubik's Pocket cube has 6 faces and 24 stickers (4 per face).

To solve, each face must be the same colour, the colours are:

![colours](/img/colours.png)

Follow the order of the diagram and note the colour of each sticker.

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

You should end up with something like this:

```python
"WYYYGGOBOORYBRRWGORWWBBG"
```
Assign to the *'instance'* variable in *main.py*
```python
instance = "WYYYGGOBOORYBRRWGORWWBBG"
```
Run: `python3 main.py`

# **Use docstrings**
CopyPaste the following commands into *main.py* to get details on what each function does.

```python
print("SOLUTION:" + project.solution.__doc__)
print("PRINT SOLUTION:" + project.printSolution.__doc__)
print("BREADTH-FIRST SEARCH:" + project.breadthFirst.__doc__)
```

# **Call Graph**
![pyan3 generated call graph](/img/cube-solver-pyan3-call-graph.png)
