import numpy as np
import matplotlib.pyplot as plt
import time
class ThomasAlorithm():
    """¨
    Approximationm for the potential from a charge,
    using a system of differential equation and a augmented matrix
    to calculate the potential, using the thomas algorithm and a
    backwards substitution.
    """
    def __init__(self, n):
        self.n = n
        _x0 = 0 # Initial condition
        _x1 = 1 # Initial condition
        h = (_x1 - _x0) / n # Step size
        _x = np.linspace(_x0,_x1,n)
        self.x = _x
        b =  100* np.exp(-10*_x)*h**2
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
            _b[i] = ( (b[i] -(a[i-2]*_b[i-1] ) )   / (d[i]- (a[i-2]*_c[i-2]))   ) #d[i] - (_b[i-1] * a[i-1] )  )

        N = n-1

        for i in range(1,n-1):
            _b[N-i] = _b[N-i] - (_c[(N-1)-i]*_b[(N+1)-i] )
        self.t = (time.time() - start_time)
        self.v = _b
        self.u = 1-(1-np.exp(-10))*_x - np.exp(-10*_x)
        #return(self.t)

    def plot(self):
        plt.plot(self.x, self.v , label = "Approximation" , marker = '+')

        plt.plot(self.x , self.u , label = "Analytical")
        plt.legend()
        plt.grid()
        plt.xlabel("Distance ; Meter",size=15)
        plt.ylabel("Potential ; Volt",size=15)
        plt.title("Potential from charge\nFast special method ",size=15)
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
    test = ThomasAlorithm(n)
    test.plot()
    print("--- %s seconds ---" % (test.time()))
    print(test.error())
    print(test._error())
