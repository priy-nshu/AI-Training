import numpy as np

def prebasics():
    a=np.array([[1,2,3],[4,6,5]])
    print("Shape:",a.shape,type(a.ndim))
    a=np.random.random((2,3))
    print(a)
    print(a.max())
    print(a.data)
    a=np.logspace(0,10,5)
    print(a)

def basics():
    # x=np.arange(6)
    # x=x.reshape((2,3))

    zeros=np.zeros((5,),dtype=np.int_)
    print(zeros)
    s=(2,2)
    s_onesarr=np.ones(s,dtype=np.float64)
    print(s_onesarr)

    # zerosarr=np.zeros_like(x)
    # print (zerosarr)

def binary_ops():
    a1=np.array([1,2,3])
    a2=np.array([4,5,6])
    a3=np.array([1,2,34,5,6,7])

    print(np.add(a1,a2))
    print(np.subtract(a1,a2))
    print(np.multiply(a1,a2))
    print(np.divide(a1,a2))

    # print((np.add(a1,a3)))
    # print((np.subtract(a1,a3)))
    # print(np.multiply(a1,a3))
    # print(np.divide(a1,a3))

def ThreeDOps():
    a3 = np.array([[[1, 2], [3, 4],        # 3D array
                    [5, 6], [7, 8]]])
    a4 = np.array([[[1, 2], [3, 4],        # 3D array
                    [5, 6], [7, 8]]])

    a5 = a6 = a7 = a3

    print(a3 + a4)    # add
    a3 += a4
    print(a3)
    print()

    print(a5 - a4)    # subtract
    a5 -= a4
    print(a5)
    print()

    print(a6 * a4)    # multiply
    a6 *= a4
    print(a6)
    print()

    a7=a7.astype(float)
    a7 /= a4  # divide
    print(a7)

def BitWise():
    # (0101 in binary)
    print()
    a = 5

    # (1010 in binary, which is -6 in decimal with two's complement)
    result = ~a
    print("The result obtained is:", result)

    print('Binary equivalents of 13 and 17:')
    a, b = 13, 17
    print(bin(a), bin(b))
    print('\n')

    # Print bitwise AND of 13 and 17
    print('Bitwise AND of 13 and 17:')
    print(np.bitwise_and(a, b))
    print(np.bitwise_or(a, b))
    print(np.bitwise_xor(a, b))

def ShiftBits():
    # Shift the bits of the integer 5 to the left by 1 position
    result = np.left_shift(5, 1)
    print(result)

    arr1 = np.array([[49, 6, 61],
                     [82, 69, 29]])

    arr2 = np.array([[40, 60, 61],
                     [81, 55, 32]])

    print(np.left_shift(arr1, 5))
    print(np.right_shift(arr1, 2))

    a1 = np.array([3, 5])
    print("Bit",np.bitwise_left_shift(a1, 2))
    print(np.left_shift(a1, 2))
    print(np.bitwise_right_shift(a1, 2))
    print(np.right_shift(a1, 2))



prebasics()
basics()
binary_ops()
ThreeDOps()
BitWise()
ShiftBits()