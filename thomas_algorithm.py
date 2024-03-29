import numpy as np
import matplotlib.pyplot as plt
import time
class ThomasAlgorithm():
    """¨
    Approximationm for the potential from a charge,
    using a system of differential equation and a augmented matrix
    to calculate the potential, using the thomas algorithm and a
    backwards substitution.
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

        d    = np.zeros(n) + 2 # Diagonal elements

        c    = np.zeros(n-2) - 1 # Upperdiagonal elements
        _c   = np.copy(c)

        a    =  np.zeros(n-2) - 1 # Lowerdiagonal elements
        start_time = time.time()

        _b[0] = 0 # Initial condition
        _c[0] = _c[0]/d[0]
        _b[1] = b[1]/d[1]
        for i in range(2,n-1):
            _c[i-1] = (     c[i-1]  /  ( d[i-1] - (a[i-2]*_c[i-2])  )     )
            _b[i] = ( (b[i] -(a[i-2]*_b[i-1] ) )   / (d[i]- (a[i-2]*_c[i-2])) )
        for i in range(1,n-1):
            _b[(n-1) - i] = _b[(n-1)-i] - (_c[(n-2)-i]*_b[n-i] )
        self.t = (time.time() - start_time)
        self.v = _b
        self.u = 1-(1-np.exp(-10))*self.x - np.exp(-10*self.x)

    def plot(self):
        plt.plot(self.x, self.v , label = "Numerisk tilnærming" , marker = '+')

        plt.plot(self.x , self.u , label = "Analytisk")
        plt.legend()
        plt.grid()
        plt.xlabel("Avstand ; Meter",size=15)
        plt.ylabel("Potensial ; Volt",size=15)
        plt.title("Potensialet fra ladningen\nThomas algoritmen",size=15)
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
    test = ThomasAlgorithm(n)
    test.plot()
    print("--- %s Sekunder ---" % (test.time()))
    print(test.error())
    print(test._error())
