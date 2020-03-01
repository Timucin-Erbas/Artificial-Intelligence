#-------------------------------------------------------------------------------
#  Author:  Timucin Erbas
#  Date  :  March 1st, 2020
#
#  Summary: This is a program that does linear regression to predict the
#  equation of the linear line that your data represents. First, the program
#  assigns values to the slope of the line, and the y-intercept.
#  Of course, these values are probaly not even close to what the equation
#  is supposed to be, so the program inches its values
#  (slope(w) and y-intecept(b)) closer and closer to the values using
#  gradient descent.
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
#  How To Use:
#  First, the program will ask you for data in th console saying "X Y: "
#  Enter your data as your X-Value a space, then your Y-Value.
#  When you are done, write DONE
#  Then enter the learning rate, and the number of times you want to run the
#  gradient descent algorithm.
#  The program will run and will give you an input slot saying "X: ".
#  In that part, write an X-Value, and the program will predict the
#  corresponding Y-Value
#  When done, write "DONE"
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
#  Import necessary packages for the program, and get input from the user
#  to train the linear regression program (x values (X), y values (Y))
#-------------------------------------------------------------------------------

import numpy as np
import random

X = []
Y = []

while True:
        inpset = input("X Y: ")
        if inpset == "DONE":
                it = int(input("Iterations: "))
                le = int(input("Learning Rate (%): "))
                break

        split = inpset.split()
        X.append(int(split[0]))
        Y.append(int(split[1]))

#-------------------------------------------------------------------------------
#  Have to normalize the data considering that the gradient descent algorithm
#  will not work if one of the points in the data is far off from the other
#  ones
#-------------------------------------------------------------------------------

m = len(X)
xdiv = max(X) - min(X)
ydiv = max(Y) - min(Y)

for i in range(0,len(X),1):
        X[i] = X[i]/xdiv
        Y[i] = Y[i]/ydiv

#-------------------------------------------------------------------------------
#  Initialize the slope(w) and y-intercept(b)
#-------------------------------------------------------------------------------

w = 1.0
b = 0.0
alpha=le/100

#-------------------------------------------------------------------------------
#  Start the gradient descent part of the program
#-------------------------------------------------------------------------------

for iter in range(0,it,1):
        dw = 0
        db = 0
        dz = 0
        J = 0
        for i in range(0,m,1):
                a = w*X[i] + b
                J += (Y[i] - a)*(Y[i] - a)
                dz = a - Y[i]
                dw += X[i]*dz
                db += dz
        db /= m
        dw /= m
        J /= m
        w -= alpha * dw
        b -= alpha * db

#--------------------------------------------------------------------------------
#  After the slope(w) and the y-intercept(b) are close enough, I finish
#  the gradient descent process. Now the user can give the program an X value,
#  and the program will predict it based on the data it was given in the
#  beginning. While doing this, it is important that the program de-normaizes
#  the outut by doing the inverse operation while being normalized.
#--------------------------------------------------------------------------------

while True:
        xinp = int(input("X: "))
        if xinp != "DONE":
                predx = xinp/xdiv
                predy = ydiv * (predx*w + b)
                print("Y: " + str(predy))
        else:
                print("----------------------------")
                break

#--------------------------------------------------------------------------------
# END OF PROGRAM
#--------------------------------------------------------------------------------



