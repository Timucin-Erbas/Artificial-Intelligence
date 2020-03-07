#-------------------------------------------------------------------------------------------------------------------------------------
#  Author: Timucin Erbas
#  Date:   March 7, 2020
#-------------------------------------------------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------------------------------------------------
#  Summary:
#  This is a linear regression program that works for any number of X values.
#-------------------------------------------------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------------------------------------------------
#  HOW TO USE:
#  1. In the console where it says "ALL X VALUES, THEN Y VALUE: ", put in all X values SPACE SEPERATED  and at the end put the Y value
#     STILL SPACE SEPERATED
#  2. When you put in all of the data, type "DONE" in the console.
#  3. The program will ask the number of iterations needed. Type in the number.
#  4. Then it will ask the learning rate, type it in.
#  5. Wait while the program trains itself"
#  6. When the program asks "X VALUES: ", type in the input numbers SPACE SEPERATED
#  7. The program will predict the output.
#-------------------------------------------------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------------------------------------------------
#  Import Necessary Packages
#-------------------------------------------------------------------------------------------------------------------------------------

import numpy as np

#-------------------------------------------------------------------------------------------------------------------------------------
#  Take in the inputs from user
#-------------------------------------------------------------------------------------------------------------------------------------

x = []
y = []

while True:
        inp = input("ALL X VALUES, THEN Y VALUE: ")
        if inp == "DONE":
                iter = int(input("ITERATIONS: "))
                alpha = int(input("LEARNING RATE (%): "))
                break

        split = inp.split()
        y.append(int(split[-1]))
        current = []
        for i in range(0,len(split)-1,1):
                current.append(split[i])
        x.append(current)

xnums = []
ynums = []
for i in range(0,len(x),1):
        for j in range(0,len(x[i]),1):
                xnums.append(int(x[i][j]))

for i in range(0,len(y),1):
        ynums.append(int(y[i]))

#-----------------------------------------------------------------------------------------------------------------------------
#  Normalize inputs since there might be outliers in the data.
#-----------------------------------------------------------------------------------------------------------------------------

xdiv = max(xnums) - min(xnums)
ydiv = max(ynums) - min(ynums)

for i in range(0,len(x),1):
        for j in range(0,len(x[i]),1):
                x[i][j] = int(x[i][j])/xdiv

for i in range(0,len(y),1):
        y[i] = int(y[i])/ydiv
        

#-----------------------------------------------------------------------------------------------------------------------------
#  Start gradient descent
#-----------------------------------------------------------------------------------------------------------------------------

DW = []
W = []
b = 0
for i in range(0,len(x[0]),1):
        W.append(1)
for it in range(0,iter,1):
        for i in range(0,len(W),1):
                DW.append(0)
        db = 0
        dz = 0
        for i in range(0,len(x),1):
                a = np.dot(W,x[i]) + b
                dz = a - y[i]
                D = (y[i] - a)*(y[i] - a)
                for w in range(0,len(x[1]),1):
                        DW[w] += x[i][w]*dz
                db += dz
        D /= len(x)
        for d in range(0,len(DW),1):
                DW[d] /= len(x)
        db /= len(x)
        for w in range(0,len(W),1):
                W[w] -= (alpha/100)*(DW[w])
        b -= (alpha/100)*(db)

#----------------------------------------------------------------------------------------------------------------------------
#  After the program has been trained enough, it is ready to take in some input and predict the output.
#----------------------------------------------------------------------------------------------------------------------------

while True:
        q = input("X VALUES: ")
        xs = q.split()
        for x in range(0,len(xs),1):
                xs[x] = int(xs[x])/xdiv
        pred = np.dot(W, xs) + b
        print("PREDICTION: " + str(pred*ydiv))

#----------------------------------------------------------------------------------------------------------------------------
#  END OF PROGRAM
#----------------------------------------------------------------------------------------------------------------------------

