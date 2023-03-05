![year](https://img.shields.io/badge/2021-lightgrey?style=plastic)
![creators](https://img.shields.io/badge/Johnny%20Madigan-yellow?style=plastic)
![python](https://img.shields.io/badge/Python-9cf?style=plastic&logo=python)

# **CUBE SOLVER**

A graph theory project on finding the minimum number of moves to solve a Rubik's Pocket cube (2x2x2).

It is well known that people compete to solve Rubik's cubes in the shortest amount of time, but what about the least number of moves?

This Python script:

1. Takes the state of your scrambled cube (encoded)
2. Generates a Cayley Graph
3. Uses BFS to find the shortest path to the solved state
4. Prints the minimum number of moves and the moves themselves

Please see my report for more details.

There is also a compact version of the script, just for fun ¯\\\_(ツ)\_/¯

![demo](/img/demo.gif)

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

Run with `python3 app.py` or VS Code and paste the cube when prompted and press enter!

# **How to solve your own cube**

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

Run with `python3 app.py` or VS Code and paste the cube when prompted and press enter!
