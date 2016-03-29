import numpy as np

class Cube():
    #yellow is top, green is front

    #cube = [green,red,blue,orange,white,yellow]
    #save values
    cube = np.array([])
    F, R, B, L, U, D = 0, 1, 2, 3, 4, 5

    #edges = [[0,0], [1,0], [2,0], [3,0], [4,0], [5,0], [6,0], [7,0], [8,0], [9,0], [10,0], [11,0]]
    #if edges[10] = [5,0], then piece 10 is in place 5 with correct orientation
    #order of edges:
    #   DF = 0, DR = 1, DB = 2, DL = 3
    #   FR = 4, BR = 5, BL = 6, FL = 7
    #   UF = 8, UR = 9, UB = 10, UL = 11
    def __init__(self):
        self.cube = self.solvedState()

    '''def __init__(self, fFace, rFace, bFace, lFace, uFace, dFace):
        cube = [fFace, rFace, bFace, lFace, uFace, dFace]

        # A Face is stored like so: (stored by proper face)
        #  [R, F, U]
        #  [L, D, B
        #  [R, F, U]
        # Numerical Positions:
        # [1, 2, 3]
        # [4, 5, 6]
        # [7, 8, 9]'''

    def solvedState(self):
        tempF = np.array([self.F,self.F,self.F,self.F,self.F,self.F,self.F,self.F,self.F])
        tempR = np.array([self.R,self.R,self.R,self.R,self.R,self.R,self.R,self.R,self.R])
        tempB = np.array([self.B,self.B,self.B,self.B,self.B,self.B,self.B,self.B,self.B])
        tempL = np.array([self.L,self.L,self.L,self.L,self.L,self.L,self.L,self.L,self.L])
        tempU = np.array([self.U,self.U,self.U,self.U,self.U,self.U,self.U,self.U,self.U])
        tempD = np.array([self.D,self.D,self.D,self.D,self.D,self.D,self.D,self.D,self.D])

        '''tempF = [[self.F,self.F,self.F],[self.F,self.F,self.F],[self.F,self.F,self.F]]
        tempR = [[self.R,self.R,self.R],[self.R,self.R,self.R],[self.R,self.R,self.R]]
        tempB = [[self.B,self.B,self.B],[self.B,self.B,self.B],[self.B,self.B,self.B]]
        tempL = [[self.L,self.L,self.L],[self.L,self.L,self.L],[self.L,self.L,self.L]]
        tempU = [[self.U,self.U,self.U],[self.U,self.U,self.U],[self.U,self.U,self.U]]
        tempD = [[self.D,self.D,self.D],[self.D,self.D,self.D],[self.D,self.D,self.D]]'''

        return np.array([tempF, tempR, tempB, tempL, tempU, tempD])

    def moveU(self):
        temp = self.cube
        tempF = self.cube[self.F]
        tempR = self.cube[self.R]
        tempB = self.cube[self.B]
        tempL = self.cube[self.L]
        tempU = self.cube[self.U]
        tempD = self.cube[self.D]

        print str(tempF[0])
        self.cube[self.U] = np.array([tempU[6], tempU[3], tempU[0], tempU[7], tempU[4], tempU[1], tempU[8], tempU[5], tempU[2]])
        self.cube[self.F] = np.array([tempR[0], tempR[1], tempR[2], tempF[3], tempF[4], tempF[5], tempF[6], tempF[7], tempF[8]])
        self.cube[self.R] = np.array([tempB[0], tempB[1], tempB[2], tempR[3], tempR[4], tempR[5], tempR[6], tempR[7], tempR[8]])
        self.cube[self.B] = np.array([tempL[0], tempL[1], tempL[2], tempB[3], tempB[4], tempB[5], tempB[6], tempB[7], tempB[8]])
        self.cube[self.L] = np.array([tempF[0], tempF[1], tempF[2], tempL[3], tempL[4], tempL[5], tempL[6], tempL[7], tempL[8]])
        print str(tempF[0])

        '''#Corners of U
        self.cube[self.U, 0] = temp[self.U, 6]
        self.cube[self.U, 2] = temp[self.U, 0]
        self.cube[self.U, 8] = temp[self.U, 2]
        self.cube[self.U, 6] = temp[self.U, 8]
        #Edges of U
        self.cube[self.U, 1] = temp[self.U, 3]
        self.cube[self.U, 5] = temp[self.U, 1]
        self.cube[self.U, 7] = temp[self.U, 5]
        self.cube[self.U, 3] = temp[self.U, 7]
        #Front face
        self.cube[self.F, 0] = temp[self.R, 0]
        self.cube[self.F, 1] = temp[self.R, 1]
        self.cube[self.F, 2] = temp[self.R, 2]
        #Right face
        self.cube[self.R, 0] = temp[self.B, 0]
        self.cube[self.R, 1] = temp[self.B, 1]
        self.cube[self.R, 2] = temp[self.B, 2]
        #Back face
        self.cube[self.B, 0] = temp[self.L, 0]
        self.cube[self.B, 1] = temp[self.L, 1]
        self.cube[self.B, 2] = temp[self.L, 2]
        #Left face
        self.cube[self.L, 0] = temp[self.F, 0]
        self.cube[self.L, 1] = temp[self.F, 1]
        self.cube[self.L, 2] = temp[self.F, 2]'''

    def moveU2(self):
        temp = self.cube
        self.cube[self.U][1] = temp[self.U][9]
        self.cube[self.U][3] = temp[self.U][7]
        self.cube[self.U][9] = temp[self.U][1]
        self.cube[self.U][7] = temp[self.U][3]
        #Edges of U
        self.cube[self.U][2] = temp[self.U][8]
        self.cube[self.U][6] = temp[self.U][4]
        self.cube[self.U][8] = temp[self.U][2]
        self.cube[self.U][4] = temp[self.U][6]
        #Front face
        self.cube[self.F][1] = temp[self.B][1]
        self.cube[self.F][2] = temp[self.B][2]
        self.cube[self.F][3] = temp[self.B][3]
        #Right face
        self.cube[self.R][1] = temp[self.L][1]
        self.cube[self.R][2] = temp[self.L][2]
        self.cube[self.R][3] = temp[self.L][3]
        #Back face
        self.cube[self.B][1] = temp[self.F][1]
        self.cube[self.B][2] = temp[self.F][2]
        self.cube[self.B][3] = temp[self.F][3]
        #Left face
        self.cube[self.L][1] = temp[self.R][1]
        self.cube[self.L][2] = temp[self.R][2]
        self.cube[self.L][3] = temp[self.R][3]

    def moveUPrime(self):
        temp = self.cube
        #Corners of U
        self.cube[self.U][1] = temp[self.U][3]
        self.cube[self.U][3] = temp[self.U][9]
        self.cube[self.U][9] = temp[self.U][7]
        self.cube[self.U][7] = temp[self.U][1]
        #Edges of U
        self.cube[self.U][2] = temp[self.U][4]
        self.cube[self.U][6] = temp[self.U][2]
        self.cube[self.U][8] = temp[self.U][6]
        self.cube[self.U][4] = temp[self.U][8]
        #Front face
        self.cube[self.F][1] = temp[self.L][1]
        self.cube[self.F][2] = temp[self.L][2]
        self.cube[self.F][3] = temp[self.L][3]
        #Right face
        self.cube[self.R][1] = temp[self.F][1]
        self.cube[self.R][2] = temp[self.F][2]
        self.cube[self.R][3] = temp[self.F][3]
        #Back face
        self.cube[self.B][1] = temp[self.R][1]
        self.cube[self.B][2] = temp[self.R][2]
        self.cube[self.B][3] = temp[self.R][3]
        #Left face
        self.cube[self.L][1] = temp[self.B][1]
        self.cube[self.L][2] = temp[self.B][2]
        self.cube[self.L][3] = temp[self.B][3]


newCube = Cube()

newCube.moveU()
#newCube.cube

print str(newCube.cube)
