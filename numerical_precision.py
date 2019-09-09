from thomas_algorithm import *
from fast_special_thomas_algorithm import *
from lu_decomposition import *
import sys
N = np.array([10, 20 ,30, 50, 80, 100, 150, 250, 400, 600,
1e3 , 1500, 2e3, 4e3, 1e4, 1e5, 1e6, 1e7,1e8])
N = N.astype(int)
n = len(N)+1

t_ta = []
e_ta = []
p_ta = []

for i in range(n-1):
    approximation = ThomasAlgorithm(N[i])
    t_ta.append(approximation.time())
    e_ta.append(approximation.error())
    p_ta.append(approximation._error())
    del approximation
    sys.stdout.write("\r%d%%" % (0.34*((i+1)/(n-1)*100)) )
    sys.stdout.flush()

t_fsta = []
e_fsta = []
p_fsta = []
for i in range(n-1):
    approximation = FastSpecialThomasAlgorithm(N[i])
    t_fsta.append(approximation.time())
    e_fsta.append(approximation.error())
    p_fsta.append(approximation._error())
    del approximation
    sys.stdout.write("\r%d%%" % (34+(0.34*((i+1)/(n-1)*100)) ))
    sys.stdout.flush()

t_lud = []
e_lud = []
p_lud = []
for i in range(n-5):
    approximation = LUDecomposition(N[i])
    t_lud.append(approximation.time())
    e_lud.append(approximation.error())
    p_lud.append(approximation._error())
    del approximation
    sys.stdout.write("\r%d%%" % (66+(0.34*((i+1)/(n-1)*100))) )
    sys.stdout.flush()

H = 1/N

plt.plot(N , t_fsta , label = "Fast Special Thomas Algorithm")
plt.plot(N , t_ta , label = "Thomas Algorithm")
plt.plot(N[:-4] , t_lud , label = "LU Decomposition")
plt.legend()
plt.grid()
plt.xlabel("Antall itereringer ; ",size=15)
plt.xscale("log")
plt.yscale("log")
plt.ylabel("Tidsforbruk ; Sekunder",size=15)
plt.title("Tidsforbruk",size=15)
plt.show()

plt.plot(H , e_ta , label = "Thomas Algorithm", marker = 7)#'caretdown')
plt.plot(H , e_fsta , label = "Fast Special Thomas Algorithm", marker = 6)# 'caretop')
plt.plot(H[:-4] , e_lud , label = "LU Decomposition",marker = 0)
plt.legend()
plt.grid()
plt.xlabel("Stegstørrelse ; Meter",size=15)
plt.xscale("log")
plt.yscale("log")
plt.ylabel("Relativ numerisk feil ; ",size=15)
plt.title("Relativ numerisk feil\nper stegstørrelse",size=15)
plt.show()

plt.plot(H , p_ta , label = "Thomas Algorithm", marker = 7)#'caretdown')
plt.plot(H , p_fsta , label = "Fast Special Thomas Algorithm", marker = 6)# 'caretop')
plt.plot(H[:-4] , p_lud , label = "LU Decomposition",marker = 0)
plt.legend()
plt.grid()
plt.xlabel("Stegstørrelse ; Meter",size=15)
plt.xscale("log")
plt.yscale("log")
plt.ylabel("Potensial ; Volt",size=15)
plt.title("Nummerisk avvik\nper stegstørrelse",size=15)
plt.show()
