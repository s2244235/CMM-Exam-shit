import numpy as np

def secant(y,a,b,e,N):
    if y(a)*y(b) >= 0:
        print("Secant method fails.")
        return None
    a_n = a
    b_n = b
    E_r = 1
    for n in range(0,N):
        m_n = a_n - y(a_n)*(b_n - a_n)/(y(b_n) - y(a_n))
        y_m_n = y(m_n)
        if e < abs(E_r) and y(a_n)*y_m_n < 0:
            a_n = a_n
            b_n = m_n
            E_r = y(m_n)
        elif e < abs(E_r) and y(b_n)*y_m_n < 0:
            a_n = m_n
            b_n = b_n
            E_r = y(m_n)
        elif e > abs(E_r):
            print("Found a solution at x =", m_n)
            return m_n
        else:
            print("Secant method fails.")
            return None
    return a_n - y(a_n)*(b_n - a_n)/(y(b_n) - y(a_n))  
y = lambda beta: np.cosh(beta) * np.cos(beta) + 1
root_1 = secant(y,0,4,0.0001,10)  
root_2 = secant(y,4,6,0.0001,10)  
roots = np.array([root_1, root_2])

# define variables
E = 200
I = 3.255E-11
m = 7850
L = 0.9

f = np.sqrt((root_2**4 * E * I)/(m * L**3))/(2 * np.pi)

print(f)

print(root_1, root_2)

