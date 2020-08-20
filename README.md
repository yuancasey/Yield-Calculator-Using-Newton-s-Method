# Yield-Calculator-Using-Newton-s-Method
This program calculates the yield of a bond by using the discounted future values to compute yield.

Newton’s method is a method to approximate solutions to an equation f(x) = 0 very quickly. It works by starting with a (more-or-less random) guess x0 for a solution, and then coming up with better and better approximations x1, x2, x3, etc., using the following process:
x1 = x0 − f(x0)/f′(x0) x2 = x1 − f(x1)/f′(x1) x3 = x2 − f(x2)/f′(x2)
and so on and so forth, with xn+1 = xn − f(xn)/f′(xn) in general. x1 will usually be close to a solution, and x2 will be closer, and x3 closer still, etc.

The program will ask the user to enter in B, c1, c2, c3, T1, T2, T3, and will then solve the equation f(x) = 0, where
f(x)=c1e−xT1 +c2e−xT2 +c3e−xT3 −B. (1) (To be very specific: x is the only variable on the right side of the above equation.) The program will use an initial guess
of x0 = 0.1, and then do 100 iterations of Newton’s method and report the value of x100.
