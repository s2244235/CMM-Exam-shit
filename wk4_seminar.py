import matplotlib.pyplot as plt
import numpy as np

# Newton Raphson Methopd
def new_raph(f, df, x_0, N):
    x_n = x_0 - f(x_0)/df(x_0)
    i = 1
    for i in range(0, N):
        x = x_n - f(x_n)/df(x_n)
        x_n = x
    return x_n
          
# Secant
def secant(f,a,b,N):

    if f(a)*f(b) >= 0:
        print("Secant method fails.")
        return None
    a_n = a
    b_n = b
    for n in range(1,N+1):
        m_n = a_n - f(a_n)*(b_n - a_n)/(f(b_n) - f(a_n))
        f_m_n = f(m_n)
        if f(a_n)*f_m_n < 0:
            a_n = a_n
            b_n = m_n
        elif f(b_n)*f_m_n < 0:
            a_n = m_n
            b_n = b_n
    return a_n - f(a_n)*(b_n - a_n)/(f(b_n) - f(a_n))

# Variables                                                                        
N = 100
x_0 = 7
a = 0
b = 7
        
# Define equations
f = lambda x: x**2 + 4*x - 12
df = lambda x: 2*x + 4

# Define arrays to store varible
N_array_NR = np.zeros(N)
sol_array_NR = np.zeros(N)

N_array_S = np.zeros(N)
sol_array_S = np.zeros(N)

for i in range (0, N):
    sol = new_raph(f, df, x_0, i)
    N_array_NR[i] = i
    sol_array_NR[i] = sol
    
    sol = secant(f, a, b, i)
    N_array_S[i] = i
    sol_array_S[i] = sol

# Plotters    
plt.figure()
plt.plot(N_array_NR, sol_array_NR)
plt.plot(N_array_S, sol_array_S)