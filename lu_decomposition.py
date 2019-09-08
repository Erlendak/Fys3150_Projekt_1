import numpy as np
import scipy.linalg as sa
import matplotlib.pyplot as plt
import time
class LUDecomposition():
    """¨
    Approximationm for the potential from a charge,
    using a system of differential equation and LU decomposition and a
    backwards substitution to calculate the potential from the charge to
    1 meter away from the charge.
    """
    def __init__(self, n):
        if (n<3):
            raise ValueError('''n is lesser than 3 and algorithm does
            not support smaller than 3''')
        self.n = n
        _x0 = 0 # Initial condition
        _x1 = 1 # Initial condition
        h = (_x1 - _x0) / n # Step size
        self.x = np.linspace(_x0,_x1,n)
        b =  100* np.exp(-10*self.x)*h**2
        _b = np.copy(b)
        d    = np.diag( np.zeros(n-2) + 2 ) # Diagonal elements
        c    = np.diag((np.zeros(n-3) - 1 ), 1)# Upperdiagonal elements
        a    = np.diag( (np.zeros(n-3) - 1) , -1) # Lowerdiagonal elements
        A = a + d + c # Tridiagonal matrix
        start_time = time.time()
        _lu = sa.lu(A)
        _lu = sa.lu_factor(A)
        v = sa.lu_solve(_lu, b[1:-1])
        v = np.insert(v,0,0 )
        self.v = np.append(v,0 )
        self.t = (time.time() - start_time)
        self.u = 1-(1-np.exp(-10))*self.x - np.exp(-10*self.x)

    def plot(self):
        plt.plot(self.x, self.v , label = "Numerisk tilnærming" , marker = '+')

        plt.plot(self.x , self.u , label = "Analytisk")
        plt.legend()
        plt.grid()
        plt.xlabel("Avstand ; Meter",size=15)
        plt.ylabel("Potentsial ; Volt",size=15)
        plt.title("Potentsial fra ladningen\n'LU decomposition'",size=15)
        plt.show()

    def error(self):
        error =np.max( np.log(  abs( (self.v[1:]-self.u[1:])/self.u[1:] )  ))
        return(error)

    def _error(self):
        error= np.max(abs(abs(self.v) - abs(self.u)))
        return(error)

    def time(self):
        return(self.t)


if __name__ == '__main__':
    n = int(input("How many steps in the approximation: n = ") )
    test = LUDecomposition(n)
    test.plot()
    print("--- %s Sekunder ---" % (test.time()))
    print(test.error())
    print(test._error())
