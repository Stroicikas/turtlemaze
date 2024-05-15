import turtle as t
import numpy as np
import random

def create_maze(dim):
    # this creates the grid with walls n shi
    maze = np.ones((dim*2+1, dim*2+1)) 

    # SP
    x, y = (5, 5)
    maze[2*x+1, 2*y+1] = 0

    # initialize stack with SP
    stack = [(x, y)]
    while len(stack) > 0:
        x, y = stack[-1]

        # defining possible dirrections
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] #basically this give random direction out of them 5
        random.shuffle(directions)

        for dx, dy in directions:
            nx, ny = x + dx, y + dy #new x, new y = x + direction x, y + direciont y pretty simple
            if nx >= 0 and ny >= 0 and nx < dim and ny < dim and maze[2*nx+1, 2*ny+1] == 1: #this just tells where to go i think?
                maze[2*nx+1, 2*ny+1] = 0 #math
                maze[2*x+1+dx, 2*y+1+dy] = 0 #more math
                stack.append((nx, ny)) #appends to the stack p ez right? its in the stack till all of the above conditions are true, if they aint true then it just pops it fr
                break
        else:
            stack.pop()

    maze[1, 0] = 0
    maze[-2, -1] = 0

    return maze
#all code under p much just makes the maze and tells the turtle where to go n shit like filling of circles how big circle
#and some other stuff.
maze = create_maze(10)
ypos = 100
t.penup()
t.setpos(-100, ypos)
t.speed(0)
for line in maze:
    for coord in line:
        if coord == 1:
            t.begin_fill()
            t.circle(5)
            t.end_fill()
            t.penup()
            t.forward(10)
            t.pendown()
        else:
            t.penup()
            t.forward(10)
            t.pendown()
    ypos -= 10
    t.penup()
    t.setpos(-100, ypos)
    t.pendown()

t.done()
"""
print(visited)

#visualiser
#random.shuffle(visited)

t.Screen().bgcolor("black")
t.hideturtle()
t.color("white")
t.speed(0)

for x in visited:
    x = [x[0] * 10, x[1] * 10]
    t.penup()
    t.setpos(x[0] - (GridSize * 5), x[1] - (GridSize * 5))
    t.pendown()
    t.begin_fill()
    t.circle(5)
    t.end_fill()

t.done()
"""