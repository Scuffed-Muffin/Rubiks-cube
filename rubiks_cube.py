import numpy as np
import tkinter as tk
import random

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
     cube1[[1,4,3,2],0,:] = cube[[4,3,2,1],0,:]
  return cube1
#Governs both the U and U' movement, U' movement occurs when direction = 1, U movment occurs when direction = -1

def D(cube,direction):
  cube1 = cube.copy()
  cube1[5]= np.rot90(cube[5], k = direction)
  if direction == 1:
    cube1[[4,3,2,1],2,:] = cube[[1,4,3,2],2,:]
  elif direction == -1:
     cube1[[1,4,3,2],2,:] = cube[[4,3,2,1],2,:]
  return cube1
#Governs both the D and D' movement, D' movement occurs when direction = 1, D movment occurs when direction = -1

def M(cube,direction):
  cube1 = cube.copy()
  if direction == 1:
    cube1[[4,3,2,1],3,:] = cube[[1,4,3,2],3,:]
  elif direction == -1:
     cube1[[1,4,3,2],3,:] = cube[[4,3,2,1],3,:]
  return cube1
#For simplicity I made a new notation for a legal move which rotates the middle row horizontally, it has the same properties as U and U'.
#I wont use this in the 2D GUI as it is not an official notation, but it will be used once I establish a 3D GUI

def L(cube,direction):
  cube1 = cube.copy()
  cube1[2]= np.rot90(cube[2], k = direction)
  if direction == 1:
    cube1[[0,5,1,3],:,0] = cube[[5,3,0,1],:,0]
  elif direction == -1:
     cube1[[5,3,0,1],:,0] = cube[[0,5,1,3],:,0]
  return cube1
#Governs both the L and L' movement, L' movement occurs when direction = 1, L movment occurs when direction = -1

def R(cube,direction):
  cube1 = cube.copy()
  cube1[4]= np.rot90(cube[4], k = direction)
  if direction == 1:
    cube1[[5,3,0,1],:,2] = cube[[0,5,1,3],:,2]
  elif direction == -1:
     cube1[[0,5,1,3],:,2] = cube[[5,3,0,1],:,2]
  return cube1
#Governs both the R and R' movement, R' movement occurs when direction = 1, R movment occurs when direction = -1

def C(cube,direction):
  cube1 = cube.copy()
  if direction == 1:
    cube1[[5,3,0,1],:,1] = cube[[0,5,1,3],:,1]
  elif direction == -1:
     cube1[[0,5,1,3],:,1] = cube[[5,3,0,1],:,1]
  return cube1
#For simplicity I made a new notation for a legal move which rotates the middle row vertically, it has the same properties as L and L'.
#I wont use this in the 2D GUI as it is not an official notation, but it will be used once I establish a 3D GUI

def F(cube,direction):
  cube1 = cube.copy()
  cube1[1]= np.rot90(cube[1], k = direction)
  if direction == 1:
    for i in range(2):
      cube1[0,2,i] = cube[2,(2-i),2]
      cube1[2,i,2] = cube[3,0,(2-i)]
      cube1[3,0,i] = cube[4,(2-i),0]
      cube1[4,i,0] = cube[0,2,(2-i)]
  elif direction == -1:
    cube1[2,:,2] = cube[0,2,:]
    cube1[3,0,:] = cube[2,:,2]
    cube1[4,:,0] = cube[3,0,:]
    cube1[0,2,:] = cube[4,:,0]
  return cube1
#Governs both the F and F' movement, F' movement occurs when direction = 1, F movment occurs when direction = -1

def B(cube,direction):
  cube1 = cube.copy()
  cube1[5]= np.rot90(cube[5], k = direction)
  if direction == 1:
    cube1[0,0,:] = cube[2,:,0]
    cube1[2,:,0] = cube[3,2,:]
    cube1[3,2,:] = cube[4,:,2]
    cube1[4,:,2] = cube[0,0,:]
  elif direction == -1:
    cube1[2,:,0] = cube[0,0,:]
    cube1[3,2,:] = cube[2,:,0]
    cube1[4,:,2] = cube[3,2,:]
    cube1[0,0,:] = cube[4,:,2]
  return cube1
#Governs both the B and B' movement, B' movement occurs when direction = 1, B movment occurs when direction = -1

def N(cube,direction):
  cube1 = cube.copy()
  if direction == 1:
    cube1[0,1,:] = cube[2,:,1]
    cube1[2,:,0] = cube[3,1,:]
    cube1[3,2,:] = cube[4,:,1]
    cube1[4,:,1] = cube[0,1,:]
  elif direction == -1:
    cube1[2,:,1] = cube[0,1,:]
    cube1[3,1,:] = cube[2,:,1]
    cube1[4,:,1] = cube[3,1,:]
    cube1[0,1,:] = cube[4,:,1]
  return cube1
#For simplicity I made a new notation for a legal move which rotates the middle row vertically, it has the same properties as L and L'.
#I wont use this in the 2D GUI as it is not an official notation, but it will be used once I establish a 3D GUI

#================================================================
action_list = [U,D,L,R,F,B]
#================================================================

#Commands associated with buttons on the GUI
def do_U():
  cube[:] = U(cube, -1)
  CreateCube()

def do_U_prime():
  cube[:] = U(cube, 1)
  CreateCube()

def do_D():
  cube[:] = D(cube, 1)
  CreateCube()

def do_D_prime():
  cube[:] = D(cube, -1)
  CreateCube()

def do_L():
  cube[:] = L(cube, 1)
  CreateCube()

def do_L_prime():
  cube[:] = L(cube, -1)
  CreateCube()

def do_R():
  cube[:] = R(cube, 1)
  CreateCube()

def do_R_prime():
  cube[:] = R(cube, -1)
  CreateCube()

def do_F():
  cube[:] = F(cube, 1)
  CreateCube()

def do_F_prime():
  cube[:] = F(cube, -1)
  CreateCube()

def do_B():
  cube[:] = B(cube, 1)
  CreateCube()

def do_B_prime():
  cube[:] = B(cube, -1)
  CreateCube()

def Scramble():
  for i in range(50):
    x = random.randint(0,5)
    action = action_list[x] 
    cube[:] = action(cube,1)
  CreateCube()
#===========================================================================
#2D graphical interface

window = tk.Tk()
canvas = tk.Canvas(window, width=700, height=700)
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
buttonU = tk.Button(
    window,
    text="U",
    command=do_U
)

buttonU.place(x=25, y=575)

buttonU_prime = tk.Button(
    window,
    text="U'",
    command=do_U_prime
)

buttonU_prime.place(x=25, y=600)

buttonD = tk.Button(
    window,
    text="D",
    command=do_D
)
buttonD.place(x=0, y=575)

buttonD_prime= tk.Button(
    window,
    text="D'",
    command=do_D_prime
)
buttonD_prime.place(x=0, y=600)

buttonL = tk.Button(
    window,
    text="L",
    command=do_L
)
buttonL.place(x=50, y=575)

buttonL_prime= tk.Button(
    window,
    text="L'",
    command=do_L_prime
)
buttonL_prime.place(x=50, y=600)


buttonR = tk.Button(
    window,
    text="R",
    command=do_R
)
buttonR.place(x=75, y=575)

buttonR_prime= tk.Button(
    window,
    text="R'",
    command=do_R_prime
)
buttonR_prime.place(x=75, y=600)

buttonF = tk.Button(
    window,
    text="F",
    command=do_F
)
buttonF.place(x=100, y=575)

buttonF_prime= tk.Button(
    window,
    text="F'",
    command=do_F_prime
)
buttonF_prime.place(x=100, y=600)

buttonB = tk.Button(
    window,
    text="B",
    command=do_B
)
buttonB.place(x=125, y=575)

buttonB_prime= tk.Button(
    window,
    text="B'",
    command=do_B_prime
)
buttonB_prime.place(x=125, y=600)

buttonScramble= tk.Button(
    window,
    text="Scramble",
    command=Scramble
)
buttonScramble.place(x=500, y=600)
#===================================
CreateCube()
window.mainloop()

