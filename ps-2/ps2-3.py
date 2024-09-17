import time
import numpy as np

start_time = time.time()

# method 1 with for loop
M = 0
L = 200
List = np.arange(-L,L+1)
for i in List:
    for j in List:
        for k in List:
            if i == 0 and j == 0 and k ==0:
                continue
            M = M + (-1)**(np.abs(i+j+k))/np.sqrt(i**2+j**2+k**2)
print("--- method 1 with for loop cost %s seconds ---" % (time.time() - start_time))
print("M number of L = {lvalue} system is: {mvalue}".format(lvalue=L, mvalue=M))

method 2 without for loop(direct matrice calculation)

start_time2 = time.time()

M = 0
L = 200
A = np.zeros([2*L+1,2*L+1,2*L+1])
x = np.arange(-L,L+1)**2
res = np.sqrt(x.reshape([1,1,2*L+1]) + x.reshape([1,2*L+1,1]) + x.reshape([2*L+1,1,1]))
res2 = 1-((np.arange(-L,L+1).reshape([1,1,2*L+1]) + np.arange(-L,L+1).reshape([1,2*L+1,1]) + np.arange(-L,L+1).reshape([2*L+1,1,1])) %2)*2
M = res * res2
M[L,L,L] = 100000000
M = 1/M


print("--- method 2 with numpy matrice calculation cost %s seconds ---" % (time.time() - start_time2))
print("M number of L = {lvalue} system is: {mvalue}".format(lvalue=L, mvalue=M.sum()))