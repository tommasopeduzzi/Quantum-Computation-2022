import numpy as np

s0 = np.matrix([[1,0],[0,1]])
s1 = np.matrix([[0,1],[1,0]])
s2 = np.matrix([[0,-1j],[1j,0]])
s3 = np.matrix([[1,0],[0,-1]])
npresulot = np.tensordot(np.tensordot(s1,s0, axes=0),s0, axes= 0).flatten()[i:i+8]
print([ npresulot[i:i+8] for i in range(8)])
