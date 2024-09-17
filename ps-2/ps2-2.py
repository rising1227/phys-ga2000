import numpy as np

def find_mininum_number_32():
    a = np.float32(1.0)
    incr = np.float32(1.0)
    while(1):
        if a + incr != np.float32(1.0):
            incr = np.float32(incr/2)
            print(incr)
        else:
            print("minimum number for float32 is {number}".format(number=incr))
            break
            
def find_mininum_number_64():
    a = np.float64(1.0)
    incr = np.float64(1.0)
    while(1):
        if a + incr != np.float64(1.0):
            incr = incr/2
        else:
            print("minimum number for float64 is {number}".format(number=incr))
            break

find_mininum_number_32()
find_mininum_number_64()


print("minimum number for float32 to represent without overflow and underflow is {number}".format(number=np.finfo(np.float32).tiny))
print("maximum number for float32 to represent without overflow and underflow is {number}".format(number=np.finfo(np.float32).max))
print("minimum number for float64 to represent without overflow and underflow is {number}".format(number=np.finfo(np.float64).tiny))
print("maximum number for float64 to represent without overflow and underflow is {number}".format(number=np.finfo(np.float64).max))