import numpy as np
import matplotlib.pyplot as plt
import time

n = int(input("How many steps in the approximation: n = ") )
_x0 = 0 # Initial condition
_x1 = 1 # Initial condition
h = (_x1 - _x0) / n # Step size
_x = np.linspace(_x0,_x1,n)


b =  100* np.exp(-10*_x)*h**2
_b = np.copy(b)



d    = np.zeros(n) + 2
_d   = np.copy(d)

c    = np.zeros(n) - 1
c[-1] = 0 # Initial condition
_c   = np.copy(c)

a    =  np.zeros(n) - 1
a[0] = 0 # Initial conditon
a[1] = 0

start_time = time.time()

_c[1] = _c[1]/_d[1]
_b[1] = b[1]/d[1]
for i in range(2,n):
    _c[i] = (     c[i]  /  ( d[i] - (a[i]*_c[i-1])  )     )
    _b[i] = ( (b[i] -(a[i]*_b[i-1] ) )   / (d[i]- (a[i]*_c[i-1]))   ) #_d[i] - (_b[i-1] * a[i-1] )  )


v = np.copy(_b)

N = 9

for i in range(1,n):
    v[N-i] = v[N-i] - (_c[N-i]*v[N-i+1] )
print("--- %s seconds ---" % (time.time() - start_time))

plt.plot(_x, v, label = "Approximation" , marker = '+')

u = 1-(1-np.exp(-10))*_x - np.exp(-10*_x)
plt.plot(_x,u, label = "Analytical")
plt.legend()
plt.grid()
plt.xlabel("Distance ; Meter",size=15)
plt.ylabel("Potential ; Volt",size=15)
plt.title("Potential from charge\nFast special method ",size=15)
plt.show()

Error = np.log(  abs( (v[1:]-u[1:])/u[1:] )  )
print(np.max(Error))
