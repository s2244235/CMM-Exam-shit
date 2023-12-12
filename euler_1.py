# Import Modules
import numpy as np
import matplotlib.pyplot as plt
import math as math

# Function to solve 
# dy/dx = -y
def model(x, y):
    k = -1
    dydx = (k * y)
    return dydx

# Initial conditions
x_0 = 0
y_0 = 1

# Solution Interval
x_final = 1

# Step sizes
h = 0.2


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
    y_exact[i] = y_0 * math.exp(-x_exact[i])
    
# ------------------------------------------------------
# ------------------------------------------------------
# print results on screen
print ('Solution: step x y-eul y-exact error%')
for i in range(N+1):
    print(i,x_eul[i],y_eul[i], y_0 * math.exp(-x_eul[i]),(y_eul[i]- y_0 * math.exp(-x_eul[i]))/(y_0 * math.exp(-x_eul[i])) * 100)
    

# ------------------------------------------------------
# plot results
plt.plot(x_eul, y_eul , 'b.-',x_exact, y_exact , 'r-')
plt.xlabel('x')
plt.ylabel('y(x)')
plt.show()








