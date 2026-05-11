from collections import Counter

def basics():
    print("Basic")
    t1=12345,54321, 'hello!'
    print(t1[0])
    print(t1)

    tup2 =t1,(1,2,3,4,5)
    print(tup2)

    tup3=([1,2,3],[3,2,1,5])
    print(tup3)

def PackUnpack():
    print("Pack and Unpack")
    a,b,c=11,12,13
    tup=(a,b,c,(),)
    print(len(tup),all(tup),tup)

    t1=12345,54321, 'hello!'
    print(t1[0])
    print(t1)

    x,y,z=t1
    print(x,y,z)

def EmptyOrSingle():
    empty=()
    print(empty)

    singleton='hello',
    print('Length of singleton:', len(singleton),singleton)

def MoreTuples():
    print("More on Tuples")
    new_tuple =tuple([1,2,3,4,5,6,7,8,9])
    print(new_tuple)

    print(new_tuple[0],new_tuple[2])
    print("Jumping:",new_tuple[1:4:5])
    # Because of immutability, we cannot change the value of a tuple element. However, we can concatenate tuples to create a new tuple.
    print(new_tuple.count(2),new_tuple.index(3))

def SomeMore():
    tup=(10,5,20,34,-23,-0)

    print("Value at index tup[-1]:",tup[-1])
    print("Value at index tup[-2]:",tup[-2] )
    print("Value at index tup[-3]:",tup[-3] )

    for x in tup:
        print(x,end=' ')
    print()

    tup1=(0,1,2,3)
    tup2=('python','C++')
    tup3=(tup1,tup2)        #Concatenating tuples
    print(tup3)
    tup3 +=tup2

    for x in tup3:
        if(len(x)>1 and type(x ) is not str):
            for y in x:
                print(y,end=' ')
            print()
        else:
            print(x)
    print(Counter(tup3))

def RepeatSlice():
    tup=('python','C++')
    print(tup,type(tup))
    tup=(0,1,2,3)

    print(tup[1:])
    print(tup[::-1])
    print(tup[:-1])
    print(tup[-1:])
    print(tup[2:4])

    a=[0,1,2]
    tup=tuple(a)
    print(tup,type(tup),len(tup))

def MultiLevelNest():
    tup=('gfg',)
    n=5

    for i in range(n):
        tup=(tup,)
        print(tup)
def EnumerableTuple():
    a=['Python','C++','Java']
    for i,v in enumerate(a):
        print(i,v)
    
    a=['A','B','C','D']
    r=list(enumerate(a))
    print(r,type(r))

    d={'a':1,'b':2,'c':3}
    for i, (k,v) in enumerate(d.items()):
        print(i,k,v)
    
def SortedLTD():
    mylist=[2,5,9,1,5,7]
    print("Sorted")
    res=sorted(mylist)
    print(res)
    res=tuple(sorted(mylist,reverse=True))
    print(res)

    #Sort a Dictionary

    a=[{"name":'Alice', 'age':30},
        {"name":'Bob', 'age':25},
        {"name":'Charlie', 'age':35}]
    b=sorted(a,key=lambda x:x['name'])
    print(b)

######################################################################
# basics()
# PackUnpack()
# EmptyOrSingle()
# MoreTuples()
# SomeMore()
# RepeatSlice()
MultiLevelNest()
EnumerableTuple()
SortedLTD()