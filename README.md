# Astar-Algorithm
A* algorithm implementation on 2*2 puzzle.(Project For an AI course) 

# What is an A* algorithm?
A * algorithm is a searching algorithm that searches for the shortest path between the initial and the final state. It is used in various applications, such as maps and games.

# The goal of the puzzle
it is about a 2D list that contains 4 colors and the goal is to have these colors in the same order as the goal list the available move is: up -> to swap the two upper tiles down -> to swap the bottom two tiles left -> to swap the left two tiles right -> to swap the right two tiles and the heuristic is based on the misplaced tiles.

# How it works?
Imagine a square grid that possesses many obstacles, scattered randomly. The initial and the final cell is provided. The aim is to reach the final cell in the shortest amount of time.


## Explanation
A* algorithm has 3 parameters:
<br/>
g : the cost of moving from the initial cell to the current cell. Basically, it is the sum of all the cells that have been visited since leaving the first cell.
<br/>
h : also known as the heuristic value, it is the estimated cost of moving from the current cell to the final cell. The actual cost cannot be calculated until the final cell is reached. Hence, h is the estimated cost. We must make sure that there is never an over estimation of the cost.
<br/>
f : it is the sum of g and h. So, f = g + h
<br/>
The way that the algorithm makes its decisions is by taking the f-value into account. The algorithm selects the smallest f-valued cell and moves to that cell. This process continues until the algorithm reaches its goal cell.
<br/>

------------------------------------------------------------------------------
for more details please check this link : https://colab.research.google.com/drive/1Cz_UQi-mjIGdx-5DFcLc01lIjgqR0_dL?authuser=1#scrollTo=d157d06c
