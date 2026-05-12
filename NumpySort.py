import numpy as np

arr=np.array([3,1,2,3,4,])
sorted_arr=np.sort(arr)
print(sorted_arr," ",arr)

arr=np.array([3,1,2,4,5])
arr.sort()
print(arr)

a=np.array([[1,4],[3,1]])
print(a)
print(f'Sort along last axis:\n{np.sort(a)}')

print(f'Flat Sort: {np.sort(a,axis=None)}')
print(f'Sorted along first axis:\n{np.sort(a,axis=0)}')

arr=np.array([[10,2,5]
              ,[1,8,3]])

sorted_arr=np.sort(arr,axis=1)
print(sorted_arr)

dtype=[('name','S10'),('height',float),('age',int)]
values=[('Arthur',1.8,41),('Lancelot',1.9,38),('Galahad',1.7,38)]
a=np.array(values,dtype=dtype)
a=np.sort(a,order='height')

for k in a:
    print(k)

def arg_sort():
    x=np.array([3,1,2])
    print('Our Array is:',x)
    y=np.argsort(x)
    print("Applying arg sort to x",y)
    print("Reconstruct Original array in sorted order:",x[y])
    for i in y:
        print(x[i],end=' ')

arg_sort()

def Re_Shape():
    a=np.array([1,2,3,4,5,6,7,8])
    r=a.reshape(2,2,2)
    print(r)
    reshaped=a.reshape(-1)
    print(reshaped)

    arr=np.array([1,2,3,4,5])
    try:
        reshaped=arr.reshape((2,3))
    except ValueError as e:
        print("Error occured in Reshaping:",e)

def Re_Size():
    arr=np.array([1,2,3,4,5,6])
    arr.resize((3,4))
    print(arr)
    arr.resize((2,2))
    print(arr)
    print()
##############
Re_Shape()
Re_Size()