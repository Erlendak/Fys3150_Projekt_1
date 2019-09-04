import numpy as np
import matplotlib.pyplot as plt
n = 10000
_x0 = 0 # Initial condition
_x1 = 1 # Initial condition
h = (_x1 - _x0) / n # Step size
_x = np.linspace(_x0,_x1,n)


b =  100* np.exp(-10*_x)*h**2
_b = np.copy(b)

d    = np.zeros(n) + 2
_d   = np.copy(d)
d0  = 2

c    = np.zeros(n) - 1
c[-1] = 0 # Initial condition
_c   = np.copy(c)
ac0 = -1


a    =  np.zeros(n) - 1
a[0] = 0 # Initial conditon



_c[0] = _c[0]/_d[0]
_b[0] = b[0]/d[0]
for i in range(1,n):
    _c[i] = (     ac0  /  ( d0 - (ac0*_c[i-1])  )     )
    _b[i] = ( (b[i] -(ac0*_b[i-1] ) )   / (d0- (ac0*_c[i-1]))   ) #_d[i] - (_b[i-1] * a[i-1] )  )


_b_ = np.copy(_b)

N = 9

for i in range(1,n):
    _b_[N-i] = _b_[N-i] - (_c[N-i]*_b_[N-i+1] )
plt.plot(_x, _b_, label = "Approximation")
#plt.plot(_x,( 1-(1-np.exp(-10))*_x - np.exp(-10*_x) ), label = "Analytical")
#plt.plot(_x,( 100*np.exp(-10*_x) ), label = "test")
plt.legend()
plt.show()
