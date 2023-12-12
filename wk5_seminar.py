# importing modules
import numpy as np
import matplotlib.pyplot as plt

x = np.array([0.    ,     0.06666667, 0.13333333, 0.2   ,     0.26666667, 0.33333333,
     0.4   ,     0.46666667, 0.53333333, 0.6   ,     0.66666667, 0.73333333,
     0.8   ,     0.86666667, 0.93333333, 1.    ,    ])

y = np.array([2.17312991, 2.19988829, 2.33988149, 2.33940595, 2.41968027, 2.99955891,
     3.04855788, 3.86631749, 3.66009775, 4.42305111, 4.22747852, 4.11717969,
     3.87539822, 4.53121841, 5.52211102, 5.30792203])
n = len(x)
# Gradient function
m = ((n * np.sum(np.multiply(x,y))) - (np.multiply(np.sum(x), np.sum(y))))/((n * np.sum(np.square(x))) - (np.sum(x))**2)

# y intercept function
y_bar = np.sum(y)/n
x_bar = np.sum(x)/n
c = y_bar - (m * x_bar)

x_array = np.linspace(0, 1, 100)

f = x_array * m + c

print("y =", m, "x +", c)

plt.scatter(x,y)
plt.plot(x_array, f)