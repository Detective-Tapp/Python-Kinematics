import vpython as vp
import numpy as np
import time

i=0
global abc
abc = bool(0)
a1=5 #link length
a2=5 #link length
a3=5 #link length

def calc(T1, T2, T3):
    
    #T1 = 0 # Theta 1  base      x/z?
    #T2 = 0 # Theta 2  arm       y/z?
    #T3 = 0  # Theta 3 grabber   y/z?
    
    T1 = (T1/180.0)*np.pi #radians
    T2 = (T2/180.0)*np.pi #radians
    T3 = (T3/180.0)*np.pi #radians
    
    # Rotation matrix
    R0_1 = [[np.cos(T1),    0,              np.sin(T1)],
            [np.sin(T1),    0,              -np.cos(T1)],
            [0,             1,              0]]
    
    R1_2 = [[np.cos(T2),             -np.sin(T2),              0],
            [np.sin(T2),             np.cos(T2),              0],
            [0,             0,              1]]
    
    R2_3 = [[np.cos(T3),    -np.sin(T3),    0],
            [np.sin(T3),    np.cos(T3),     0],
            [0,             0,              1]]
    
    # displacement vectonk
    d0_1 = [[0],
        [0],
        [a1]]
    
    d1_2 = [[a2*np.cos(T2)],
        [a2*np.sin(T2)],
        [0]]
    
    d2_3 = [[a3*np.cos(T3)],
        [a3*np.sin(T3)],
        [0]]
    
    # Homogenous matrix
    H0_1 = [[np.cos(T1), 0, np.sin(T1),  0],
        [np.sin(T1), 0, -np.cos(T1), 0],
        [0, 1, 0,                   a1],
        [0, 0, 0,                    1]]
    
    H1_2 = [[np.cos(T2), -np.sin(T2), 0, a2*np.cos(T2)],
        [np.sin(T2), np.cos(T2), 0, a2*np.sin(T2)], 
        [0, 0, 1, 0],
        [0, 0, 0, 1]]
    
    H2_3 = [[np.cos(T3), -np.sin(T3), 0, a3*np.cos(T3)],
        [np.sin(T3), np.cos(T3), 0, a3*np.sin(T3)],
        [0, 0, 1, 0],
        [0, 0, 0, 1]]
    
    # combined homohenous matrix
    H0_3 = np.dot(H0_1, np.dot(H1_2, H2_3))
    
    # calculate the 2d angles in degrees.
    Theta1 = np.arccos(H0_1[0][0])/np.pi*180.0
    Theta2 = np.arccos(H1_2[0][0])/np.pi*180.0
    Theta3 = np.arccos(H2_3[0][0])/np.pi*180.0
    
    print(np.matrix(H0_3))
    
    print(np.matrix(R0_1))
    print(np.matrix(R1_2))
    print(np.matrix(R2_3))
    
    pos1 = vp.vector(H0_1[3][0], H0_1[3][1], H0_1[3][2])
    pos2 = vp.vector(H1_2[3][0], H1_2[3][1], H1_2[3][2])
    pos3 = vp.vector(H2_3[3][0], H2_3[3][1], H2_3[3][2])
    
    #pos2 += vp.vector(0,5,0)
    #pos3 += pos2
    #pos3 += vp.vector(0,0,5)
    
    #rot1 = vp.vector(R0_1[2][0], R0_1[2][1], R0_1[2][2])
    #rot2 = vp.vector(R1_2[2][0], R1_2[2][1], R1_2[2][2])
    #rot3 = vp.vector(R2_3[2][0], R2_3[2][1], R2_3[2][2])
    
    rot1 = vp.vector(1,1,1)
    rot2 = vp.vector(1,1,1)
    rot3 = vp.vector(1,1,1)
    
    #rot1 *= R0_1
    #rot2 *= R1_2
    #rot3 *= R2_3
    
    # Multiply rot matrix with the rotVectors.
    r1 = vp.vector(R0_1[0][0] + R0_1[1][0] + R0_1[2][0], R0_1[0][1] + R0_1[1][1] + R0_1[2][1], R0_1[0][2] + R0_1[1][2] + R0_1[2][2])
    r2 = vp.vector(R1_2[0][0] + R1_2[1][0] + R1_2[2][0], R1_2[0][1] + R1_2[1][1] + R1_2[2][1], R1_2[0][2] + R1_2[1][2] + R1_2[2][2])
    r3 = vp.vector(R2_3[0][0] + R2_3[1][0] + R2_3[2][0], R2_3[0][1] + R2_3[1][1] + R2_3[2][1], R2_3[0][2] + R2_3[1][2] + R2_3[2][2])
    
    # Normalize the rotvectors.
    vp.vector.norm(r1); r1 *= 3
    vp.vector.norm(r2); r2 *= 3 
    vp.vector.norm(r3); r3 *= 3 
    
    # Set the length of the rotvectors to 5.
    
    #rot2 += rot1
    #rot3 += rot1
    
    # cylinder ctor = (posVec3, axisVec3, upVec3, length, radius, size, colorRGB 0-1, shininess, emissive, texture, canvas)
    #base =    vp.cylinder(pos=pos1, axis=vp.vector(1,0,0), length=5, radius=1, color=vp.vector(0,0,1))
    #arm  =    vp.cylinder(pos=pos2, axis=vp.vector(0,1,0), length=5, radius=1, color=vp.vector(1,0,0))
    #grabber = vp.cylinder(pos=pos3, axis=vp.vector(0,0,1), length=5, radius=1, color=vp.vector(0,1,0))

    if i <= 1:
        global base;     base    = vp.cylinder(pos=pos1, axis=r1, length=5, radius=1, color=vp.vector(1,0,0))
        global arm;      arm     = vp.cylinder(pos=r1, axis=r2, length=5, radius=1, color=vp.vector(0,1,0))
        global grabber;  grabber = vp.cylinder(pos=r2 + r1, axis=r3, length=5, radius=1, color=vp.vector(0,0,1))
    
    base.pos = pos1; base.axis = r1
    arm.pos = r1; arm.axis = r2
    grabber.pos = r2 + r1; grabber.axis = r3
    
# Todo: Add sliders to aid in debugging arm and to control arm. Figure out bone/joints. find correct base axis for all arms.

# normalize rotation vector, then set pos of arm 2 to rotVec of pos1. And so on.
while i < 3600000:
    i += 1
    T1 = i # Theta 1  base      x/z?
    T2 = i # Theta 2  arm       y/z?
    T3 = i/2  # Theta 3 grabber   y/z?
    if i >= 360: 
        i = 3
    calc(1,T2,1)