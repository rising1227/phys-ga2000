import numpy as np
import sys

a = float(sys.argv[1])
b = float(sys.argv[2])
c = float(sys.argv[3])

print("the first root of the quadratic equation is:",(-b+np.sqrt(b**2-4*a*c))/(2*a))
print("the second root of the quadratic equation is:",(-b-np.sqrt(b**2-4*a*c))/(2*a))
