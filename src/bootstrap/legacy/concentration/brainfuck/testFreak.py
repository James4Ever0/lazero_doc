from unicode_tensor import chrTens, recv

s="give no fuck"
c=chrTens(s)
d=recv(c)
print(c)
print(d,c.shape[0])