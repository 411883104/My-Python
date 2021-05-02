#函数format
a=5
print("{0:.8f}".format(float(a)))
print("{0:.6f}".format(3.1415926))

print("{0:<15.5f}".format(float(a)))#左对齐
print("{0:>15.5f}".format(float(a)))#右对齐
print("{0:^15.5f}".format(float(a)))#中对齐