import numpy as np
import matplotlib.pyplot as plt
import time
start_time = time.time()

n = 10000
_x0 = 0 # Initial condition
_x1 = 1 # Initial condition
h = (_x1 - _x0) / n # Step size
_x = np.linspace(_x0,_x1,n)

d    = 2
ac0 = -1

b =  100* np.exp(-10*_x)*h**2
_b = np.copy(b)



_c    = np.zeros(n) - 1
_c[-1] = 0 # Initial condition




_c[0] = _c[0]/d
_b[0] = b[0]/d
for i in range(1,n):
    _c[i] = (     ac0  /  ( d - (ac0*_c[i-1])  )     )
    _b[i] = ( (b[i] -(ac0*_b[i-1] ) )   / (d- (ac0*_c[i-1]))   ) #d[i] - (_b[i-1] * a[i-1] )  )




N = 9
for i in range(1,n):
    _b[N-i] = _b[N-i] - (_c[N-i]*_b[N-i+1] )


print("--- %s seconds ---" % (time.time() - start_time))

u = 1-(1-np.exp(-10))*_x - np.exp(-10*_x)
plt.plot(_x,u, label = "Analytical")
plt.plot(_x, _b, label = "Approximation")
plt.legend()
plt.grid()
plt.xlabel("Distance ; Meter",size=15)
plt.ylabel("Potential ; Volt",size=15)
plt.title("Potential from charge\nFast special method ",size=15)
plt.show()

Error = np.log(  abs( (_b-u)/u )  )
print(np.max(Error[1:]))
