#******************************************************************************
# yield.py
#******************************************************************************
# Name: Casey Yuan
#******************************************************************************
import math

x = float(0.1)
B = float(input("Value for B: "))
c1,c2,c3 = float(input("Value for c1: ")),float(input("Value for c2: ")),float(input("Value for c3: "))
T1,T2,T3 = float(input("Value for T1: ")),float(input("Value for T2: ")),float(input("Value for T3: "))
errorTolerance = float(input("Value for error tolerance: "))

def fx (): #function to calculate f(x)
  return float(c1*math.exp(-x*T1)+(c2*math.exp(-x*T2))+(c3*math.exp(-x*T3))-B)

def px (): #function to calculate derivative of f(x)
  return float(-T1*c1*math.exp(-x*T1)-T2*c2*math.exp(-x*T2)-T3*c3*math.exp(-x*T3))

print ("\nCalculating by running 100 iterations: ")

for y in range(0,100): #running 100 iterations, calculating up to x_99.
  x = float(x - (fx()/px())) #formula, but calling the two functions, since
  #x is being updated every iteration.

print (str(x))
if ((fx() < 0.0000001) and (fx()>-0.0000001)): #according to problem, this would
#be a good approximation.
  print ('Got a good approximate solution'+ '\n')

print ("Calculating by matching error tolerance (reset x to 0.1): ")
x = 0.1

while (abs(fx()) >= errorTolerance): #loop will run as long as error tolerance
#is greater than absolute value of function fx.
  x = float(x - (fx() / px ())) #updating x with x1, x2,... xn.

print(str(x) + '\n') #prints out value x using error tolerance.
