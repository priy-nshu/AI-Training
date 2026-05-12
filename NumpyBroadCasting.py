import numpy as np

a=np.array([[1,2,3],[4,5,6]])
x=10
print(a+x)
b=np.array([[1,3,7],[7,9,11]])
res=a+b
print(res)

a=np.array([12,24,5,21,34,67,41,10])
b=np.array(['adult','minor'])
res=np.where(a>18,b[0],b[1])
print(res)

a=np.array([[12,24],[5,21],[34,67],[41,10]])
b=np.array([10,20])
res=a*b
print(res,type(res))

items=([0.8,2.9,3.9],
       [52.4,23.6,36.5])
b=np.array([3,3,8])
res=items * b
print(res)
sum=np.sum(res,axis=1)
print(sum)

img=np.array([[100,200,300],
             [90,10,140],
             [80,100,120]])
m=img.mean(axis=0)
s=img.std(axis=0)
res=(img/m)/s
print(res)

