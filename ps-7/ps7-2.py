import numpy as np

def f1(x):
    return (x-0.3)**2 * np.e**(x)

x1 = -2
x2 = 3
xmid = x1 + 0.382*(x2-x1)
w = 0.382

while(1):
    x3 = xmid - 0.5*( (xmid-x1)**2 * (f1(xmid) - f1(x2)) -(xmid-x2)**2 * (f1(xmid) - f1(x1)) )/((xmid-x1) * (f1(xmid) - f1(x2)) -(xmid-x2) * (f1(xmid) - f1(x1)))
    if min((f1(x1)-f1(x3)),(f1(x2)-f1(x3))) < 1e-10:
        print("the minimum of f1 is {asddf} at x3 = {asd}".format(asddf=f1(x3),asd=x3))
        break
    if x3 >= x2 or x3 <= x1:
        x3 = xmid + 0.382*(x2-xmid)
        if f1(x3) <= f1(xmid):
            x1 = xmid
            xmid = x3
        if f1(x3) > f1(xmid):
            x2 = x3
    if x3 < x2 and x3 > x1:
        if x3 >= xmid:
            if f1(x3) <= f1(xmid):
                x1 = xmid
                xmid = x3
            if f1(x3) > f1(xmid):
                x2 = x3
        if x3 < xmid:
            if f1(x3) <= f1(xmid):
                x2 = xmid
                xmid = x3
            if f1(x3) > f1(xmid):
                x1 = x3