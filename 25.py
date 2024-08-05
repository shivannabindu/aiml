import numpy as n 
 
s=50 
print("Scalar : ",s) 
 
m=n.array([[0, 2],[2, 3]]) 
v=n.array([[0, 2]]) 
print("\nMatrix:\n",m) 
print("\nVector:\n",v) 
 
print("\nTensor:") 
g=n.gradient(m) 
print("\nGradient:\n",g) 
 
w,v = n.linalg.eig(m) 
mat_norm = n.linalg.norm(m) 
print("\nEigen values:\n",w) 
print("\nEigen vectors:\n",v) 
print("\nMatrix norm:", mat_norm) 