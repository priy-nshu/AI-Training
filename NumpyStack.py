import numpy as np 

def my_stack():
    a=np.array([1,2,3])
    b=np.array([4,5,6])
    res=np.stack((a,b),axis=-1)
    print(res)

    m=np.array([[[1,2],[3,4]],
                 [[5,6],[7,8]]])
    
    n=np.array([[[10,20],[30,40]],
                 [[50,60],[70,80]]])
    
    arr=np.empty((2,2,2,2))
    print(np.stack((m,n),axis=0,out=arr))
    print(arr)

    print(arr.shape)

#############################################
my_stack()