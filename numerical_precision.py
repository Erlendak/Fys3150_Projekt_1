from thomas_algorithm import *
from fast_special_thomas_algorithm import *
from lu_decomposition import *
n = 6

N = []
for i in range(1,n):
    N.append(10**i)

t_ta = []
e_ta = []

for i in range(n-1):
    approximation = ThomasAlgorithm(N[i])
    t_ta.append(approximation.time())
    e_ta.append(approximation.error())
    del approximation

t_fsta = []
e_fsta = []
for i in range(n-1):
    approximation = FastSpecialThomasAlgorithm(N[i])
    t_fsta.append(approximation.time())
    e_fsta.append(approximation.error())
    del approximation

t_lud = []
e_lud = []
for i in range(n-1):
    approximation = FastSpecialThomasAlgorithm(N[i])
    t_lud.append(approximation.time())
    e_lud.append(approximation.error())
    del approximation

plt.plot(N , t_fsta , label = "Fast Special Thomas Algorithm")
plt.plot(N , t_ta , label = "Thomas Algorithm")
plt.plot(N , t_lud , label = "LU Decomposition")
plt.legend()
plt.grid()
plt.xlabel("n ; ",size=15)
plt.xscale("log")
plt.yscale("log")
plt.ylabel("Tid ; Sekunder",size=15)
plt.title("Sammenligning av algorithmene\nTidsforbruk per n",size=15)
plt.show()

plt.plot(N , e_fsta , label = "Fast Special Thomas Algorithm")
plt.plot(N , e_ta , label = "Thomas Algorithm")
plt.plot(N , e_lud , label = "LU Decomposition")
plt.legend()
plt.grid()
plt.xlabel("n ; ",size=15)
plt.xscale("log")
plt.yscale("log")
plt.ylabel("Tid ; Sekunder",size=15)
plt.title("Sammenligning av algorithmene\nNumerisk feil per n",size=15)
plt.show()
