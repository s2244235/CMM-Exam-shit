# Import Modules
import numpy as np
import matplotlib.pyplot as plt
import math as math

# Function to solve 
# dy/dx = y(1-y)
def model(x, y):
    dydx = y * (1 - y)
    return dydx

# Initial conditions
x_0 = 0
y_0 = 0.0179862

# Solution Interval
x_final = 10

# Step sizes
h = 0.01

# Euler Method
# number of steps
N = math.ceil(x_final/h)

# Arrays to store solution
x_eul = np.zeros(N + 1)
y_eul = np.zeros(N + 1)

# First elementr of array with initial conditions
x_eul[0] = x_0
y_eul[0] = y_0

# Populate the x array
for i in range(N):
    x_eul[i+1] = x_eul[i] + h
    
# Euler Method
for i in range(N):
    # gradient differential
    grad = model(x_eul[i],y_eul[i])
    # Apply method
    y_eul[i+1] = y_eul[i] + h * grad

    
# ------------------------------------------------------
# super refined sampling of the exact solution c*e^(-x)
# n_exact linearly spaced numbers# only needed for plotting reference solution
# Definition of array to store the exact solution
n_exact = 1000
x_exact = np.linspace(0,x_final,n_exact+1)
y_exact = np.zeros(n_exact+1)

# exact values of the solution
for i in range(n_exact+1):
    y_exact[i] = math.exp(x_exact[i]-4)/(math.exp(x_exact[i]-4) + 1)
    

# ------------------------------------------------------
# print results on screen
print ('Solution: step x y-eul y-exact error%')
#for i in range(N+1):
    # plot results in the loop
plt.figure()
plt.plot(x_eul, y_eul , 'b.-', label='Eul')
plt.plot(x_exact, y_exact , 'r-', label='Exact')
plt.xlabel('x')
plt.ylabel('y(x)')
st1 = 'Solution for h = '+str(h) 
plt.legend(title=st1)
st2 = 'Solution_h_'+str(h)+'.pdf'
plt.savefig(st2)









