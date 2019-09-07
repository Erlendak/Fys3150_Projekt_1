import numpy as np
import scipy.linalg as sa
import matplotlib.pyplot as plt
import time

n = int(input("How many steps in the approximation: n = ") )
_x0 = 0 # Initial condition
_x1 = 1 # Initial condition
h = (_x1 - _x0) / n # Step size
_x = np.linspace(_x0,_x1,n)


b =  100* np.exp(-10*_x)*h**2
_b = np.copy(b)
#b[1] = 0
d    = np.diag( np.zeros(n-2) + 2 ) # Diagonal elements
c    = np.diag((np.zeros(n-3) - 1 ), 1)# Upperdiagonal elements
a    = np.diag( (np.zeros(n-3) - 1) , -1) # Lowerdiagonal elements
A = a + d + c # Tridiagonal matrix
#print(A)
_lu = sa.lu(A)
_lu = sa.lu_factor(A)
v = sa.lu_solve(_lu, b[1:-1])
#print(solutition)
#print(sp.__version__)

#print(_lu)

#start_time = time.time()



#print("--- %s seconds ---" % (time.time() - start_time))
v = np.insert(v,0,0 )
v = np.append(v,0 )
plt.plot(_x,v , label = "Approximation" , marker = '+')

u = 1-(1-np.exp(-10))*_x - np.exp(-10*_x)
plt.plot(_x,u, label = "Analytical" , marker = '+')
plt.legend()
plt.grid()
plt.xlabel("Distance ; Meter",size=15)
plt.ylabel("Potential ; Volt",size=15)
plt.title("Potential from charge\nFast special method ",size=15)
plt.show()

Error = np.log(  abs( (v[1:]-u[1:])/u[1:] )  )
print(np.max(Error))
print(np.max( abs(abs(v) - abs(u) )))
