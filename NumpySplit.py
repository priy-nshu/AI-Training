import numpy as np

def simple_split():
    arr=np.array([1,2,3,4,5,6])
    (a1,a2,a3)=np.array_split(arr,3)
    print(a1)

def unequal_split():
    arr=np.array([[1,2,3],[4,5,6]])
    res=np.array_split(arr,4)
    print(res)
    res=np.split(arr,2,axis=0)
    print(res)

def equal_split():
    arr=np.array([[1,2,3],[4,5,6]])
    res=np.split(arr,2,axis=0)
    print(res)
    res=np.split(arr,2,axis=1)
    print(res)

def v_split():
    arr=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
    print(arr.shape)
    res=np.vsplit(arr,4)
    print(res)

def h_split():
    arr=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
    print(arr.shape)
    res=np.hsplit(arr,4)
    print(res)

#######################################
simple_split()
unequal_split()
equal_split
v_split()
h_split()