my_numbers =[0,1,1.414,1.618,2.718,3.142,42,49,1024,299792]
first_half =slice(0,5)
second_half = slice(5,10)

m1=my_numbers[first_half]
m2=my_numbers[second_half]

print(my_numbers[::])
print(my_numbers[:])

b=my_numbers[2:]
print(b)

c=my_numbers[:3]
print(c)

start,end=4,8
l1=my_numbers[start:end]
print(l1)

print("Negative slicing")
b=my_numbers[-2:]
print(b)

d=my_numbers[-4:-1]
print(d)    

e=my_numbers[-8:-1:2]
print(e)