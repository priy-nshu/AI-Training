func =[lambda arg=x:arg *10 for x in range(1,5)] 

for i in func:
    print(i())

calc =lambda x,y:(x+y,x*y)
res =calc(5,10)
print(res)

a=[1,2,3,4]
double =map(lambda x:x*2,a) #map() applies the lambda function to each element of the list 'a' and returns a map object. Used for itereable DS
print(double," ",type(double))               #gives the memory address of the map object
print(list(double))

from functools import reduce
a=[1,2,3,4]
mul=reduce(lambda x,y:x*y,a) #reduce() applies the lambda function cumulatively to the items of the list 'a', from left to right, reducing the list to a single value.
print("Reduced multiplication 4!:", mul)

c=[1,2,3,4,5,6]
even=filter(lambda x:x%2==0,c) #filter() constructs an iterator from elements of the list 'c' for which the lambda function returns true.
print(even," ",type(even)) #gives the memory address of the filter object
print(list(even))

def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries -= 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

#ask_ok('Do you really want to quit?')
#ask_ok('OK to overwrite the file?', 2)
ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')