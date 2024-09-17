import numpy as np
import matplotlib.pyplot as plt
import struct


def get_bits(number):
    """For a NumPy quantity, return bit representation
    
    Inputs:
    ------
    number : NumPy value
        value to convert into list of bits
        
    Returns:
    -------
    bits : list
       list of 0 and 1 values, highest to lowest significance
    """
    bytes = number.tobytes()
    bits = []
    for byte in bytes:
        bits = bits + np.flip(np.unpackbits(np.uint8(byte)), np.uint8(0)).tolist()
    return list(reversed(bits))

value_big = np.float32(100.98763)
bitlist = get_bits(np.float32(value_big))
e10 = np.array([ ee * 2**(7-indx) for indx, ee in zip(range(8), bitlist[1:9])], dtype=np.int32).sum() - 127
print("Exponent of {value}: {exponent} --> {e10}".format(value=value_big, exponent=bitlist[1:9], e10=e10))
print("Mantissa of {value}: {mantissa}".format(value=value_big, mantissa=bitlist[9:]))
print("Difference between np.float32(100.98763) and 100.98763: {value}".format(value=value_big - np.float64(100.98763), mantissa=bitlist[9:]))

