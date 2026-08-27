import numpy as np
import tkinter as tk

cube = np.zeros((6,3,3), dtype= int)
for face in range(6):
    cube[face] = face
#Creates a 3x3x6 matrix that acts as the cube.
#The numbers 0-5 represent different colours on the cube
#For example, 0 = white, 1 = red, 2 = orange, 3 = yellow, 4 = green, 5 = blue.
solved_cube = cube.copy()
#Creates a template for a solved cube, we can use this as a win condition in the future

colour_list = ["orange","white","green","red","blue","yellow"]

#=====================================================================
#Functions that define cube movments
def U(cube,direction):
  cube1 = cube.copy()
  cube1[0]= np.rot90(cube[0], k = direction)
  if direction == 1:
    cube1[[4,3,2,1],0,:] = cube[[1,4,3,2],0,:]
  elif direction == -1:
     cube1[[1,2,3,4],0,:] = cube[[4,3,2,1],0,:]
  return cube1
#Governs both the U and U' movement, U' movement occurs when direction = 1, U movment occurs when direction = -1

def D(cube,direction):
  cube1 = cube.copy()
  cube1[5]= np.rot90(cube[5], k = direction)
  if direction == 1:
    cube1[[4,3,2,1],2,:] = cube[[1,2,3,4],2,:]
  elif direction == -1:
     cube1[[1,2,3,4],2,:] = cube[[4,3,2,1],2,:]
  return cube1
#Governs both the D and D' movement, D' movement occurs when direction = 1, D movment occurs when direction = -1

def M(cube,direction):
  cube1 = cube.copy()
  if direction == 1:
    cube1[[4,3,2,1],3,:] = cube[[1,2,3,4],3,:]
  elif direction == -1:
     cube1[[1,2,3,4],3,:] = cube[[4,3,2,1],3,:]
  return cube1
#For simplicity I made a new notation for a legal move which rotates the middle row horizontally, it has the same properties as U and U'.

def L(cube,direction):
  cube1 = cube.copy()
  cube1[2]= np.rot90(cube[2], k = direction)
  if direction == 1:
    cube1[1,[4,5,1,0],:] = cube[1,[0,4,5,1],:]
  elif direction == -1:
     cube1[1,[0,4,5,1],:] = cube[1,[4,5,1,0],:]
  return cube1
#Governs both the L and L' movement, L' movement occurs when direction = 1, L movment occurs when direction = -1

def R(cube,direction):
  cube1 = cube.copy()
  cube1[4]= np.rot90(cube[4], k = direction)
  if direction == 1:
    cube1[3,[4,5,1,0],:] = cube[3,[0,4,5,1],:]
  elif direction == -1:
     cube1[3,[0,4,5,1],:] = cube[3,[4,5,1,0],:]
  return cube1
#Governs both the R and R' movement, R' movement occurs when direction = 1, R movment occurs when direction = -1

def C(cube,direction):
  cube1 = cube.copy()
  if direction == 1:
    cube1[2,[4,5,1,0],:] = cube[2,[0,4,5,1],:]
  elif direction == -1:
     cube1[2,[0,4,5,1],:] = cube[2,[4,5,1,0],:]
  return cube1
#For simplicity I made a new notation for a legal move which rotates the middle row vertically, it has the same properties as L and L'.

def F(cube,direction):
  cube1 = cube.copy()
  cube1[2]= np.rot90(cube[2], k = direction)
  if direction == 1:
    cube1[1,[4,5,1,0],:] = cube[1,[0,4,5,1],:]
  elif direction == -1:
     cube1[1,[0,4,5,1],:] = cube[1,[4,5,1,0],:]
  return cube1
#Governs both the L and L' movement, L' movement occurs when direction = 1, L movment occurs when direction = -1

def B(cube,direction):
  cube1 = cube.copy()
  cube1[4]= np.rot90(cube[4], k = direction)
  if direction == 1:
    cube1[3,[4,5,1,0],:] = cube[3,[0,4,5,1],:]
  elif direction == -1:
     cube1[3,[0,4,5,1],:] = cube[3,[4,5,1,0],:]
  return cube1
#Governs both the R and R' movement, R' movement occurs when direction = 1, R movment occurs when direction = -1

def N(cube,direction):
  cube1 = cube.copy()
  if direction == 1:
    cube1[2,[4,5,1,0],:] = cube[2,[0,4,5,1],:]
  elif direction == -1:
     cube1[2,[0,4,5,1],:] = cube[2,[4,5,1,0],:]
  return cube1
#For simplicity I made a new notation for a legal move which rotates the middle row vertically, it has the same properties as L and L'.
#================================================================
#Commands associated with buttons on the GUI
def do_U():
  cube[:] = U(cube, 1)
  CreateCube()





#===========================================================================
#2D graphical interface

import tkinter as tk

window = tk.Tk()
canvas = tk.Canvas(window, width=600, height=600)
canvas.pack()


def CreateFace(face,Start_x,Start_y):
    for i in range(0,3):
        for j in range(0,3):
            Square_Colour = cube[face,j,i]
            Colour = colour_list[Square_Colour]
            canvas.create_rectangle(Start_x+(i*25), Start_y+(j*25), Start_x+((i+1)*25), Start_y+((j+1)*25), fill=Colour,outline="black")

def CreateCube():
  canvas.delete("all")
  CreateFace(0, 300, 100)
  CreateFace(1, 300, 175) 
  CreateFace(3, 300, 250)  
  CreateFace(5, 300, 325)  
  CreateFace(2, 225, 175)  
  CreateFace(4, 375, 175)  

#===========================================================================
#Buttons on the GUI
button = tk.Button(
    window,
    text="U",
    command=do_U
)

button.pack()


CreateCube()
window.mainloop()

