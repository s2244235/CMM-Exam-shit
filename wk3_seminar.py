def new_raph(f, df, x_0, e, N):
    x_n = x_0 - f(x_0)/df(x_0)
    E_r = 1
    i = 1
    for i in range(0, N):
        if e < E_r:
            x = x_n - f(x_n)/df(x_n)
            x_n = x
            E_r = f(x_n)
            print("step =", x_n)
        elif e > E_r:
            print("root =", x_n)
            break
    else:
        print("no solution in max iterations to desired accuracy")
f = lambda x: x**2 + 4*x -12
df = lambda x: 2*x + 4
new_raph(f, df, 200, 0.000001, 100)
        



def secant(f,a,b,e,N):
    if f(a)*f(b) >= 0:
        print("Secant method fails.")
        return None
    a_n = a
    b_n = b
    E_r = 1
    for n in range(0,N):
        m_n = a_n - f(a_n)*(b_n - a_n)/(f(b_n) - f(a_n))
        f_m_n = f(m_n)
        if e < abs(E_r) and f(a_n)*f_m_n < 0:
            a_n = a_n
            b_n = m_n
            E_r = f(m_n)
        elif e < abs(E_r) and f(b_n)*f_m_n < 0:
            a_n = m_n
            b_n = b_n
            E_r = f(m_n)
        elif e > abs(E_r):
            print("Found a solution at x =", m_n)
            return m_n
        else:
            print("Secant method fails.")
            return None
    return a_n - f(a_n)*(b_n - a_n)/(f(b_n) - f(a_n))  
f = lambda x: x**2 + 4*x - 12
secant(f,0,4,0.0001,10)  







