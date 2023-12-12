# Create an array x with 20 elements; all the elements must be zeros.
# Change the values of the elements in the array with random numbers in the range (0, 10).
# Print all the elements of the array on the console.
# Find the index of the elements that are larger than 5 and smaller than 6 and print them on the
# console

# import libraries
import numpy as np
import random

# create array of zeros with n elements
n = 20
x = np.zeros(n)

# print array to check it is correct
print(x)

# populate array with random numbers
random_min = 0
random_max = 10

for i in range(0,n):
    x[i] = random.uniform(random_min,
                          random_max)
    
# print array to check it is correct
print(x)

# find array positions for which
# the value is between a and b
a = 5
b = 6

for i in range(0,n):
    if x[i] > a and x[i] < b:
        print(i)
        
        
# Create an array x of equispaced coordinates in the range (0, 2π)
# Create an array y, where the elements of y are the sine of the elements of x. y = sin(x).
# Plot y vs x in a graph.

# import libraries
import numpy as np
import matplotlib.pyplot as plt

# create array x of coordinate in 0:2pi
n = 20
x = np.linspace(0, 2.0*np.pi, n)

# print array to check it is correct
print(x)

# create array y of sine values
y = np.sin(x)
plt.plot(x,y,'.')
plt.xlabel('x')
plt.ylabel('y=sin(x)')
plt.show()

##Pi Approximation using taylor series
# importing modules
import numpy as np
import matplotlib.pyplot as plt
N = 10
s = 0
pi_n = np.zeros(N)
nn = np.zeros(N)
error_true = np.zeros(N)
error_ext = np.zeros(N)
for i in range(1,N+1):
    pi_old = (s*6.0)**0.5
    s = s + 1.0/i**2.0
    pi_n[i-1] = (s*6.0)**0.5
    nn[i-1] = i
    error_true[i-1] = np.absolute(pi_n[i-1] - np.pi)
    error_ext[i-1] = np.absolute(pi_n[i-1] - pi_old)
    # print(i,pi_n[i-1], error_true[i-1], error_ext[i-1])
plt.figure()
plt.loglog(nn,error_true,'-b',
nn,error_ext,'.r')
plt.show()




