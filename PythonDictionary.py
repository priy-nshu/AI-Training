a={"x":1,"y":2}
print(a)

d={"name":"Kat","age":31}

print(d["name"])
print(d.get("age"))

d["job"]="Engineer"
d["age"]=21
print(d)

staff=dict(first_name='Debra',last_name='Burks',phone=None,
           email='db@gmail.com',city='Bengaluru',
           state="KA",zip=53010)
print(staff)

knights={'gallahad':'the pure','robin':'the brave'}

for k,v in knights.items():
    print(k,v)

print(f'Key Collection: {knights.keys()}')
for k in knights.keys():
    print(k)

print(f'Value Collection: {knights.values()}')
for v in knights.values():
    print(v)

del d["name"]
print(d)

val=d.pop("age")
print(val)
print(d)

poped_item=d.popitem()
print(poped_item)

categories={
    'cat1':{1:'Children Bicycles'},
    'cat2':{2:'Comfort Bicycles'},
    'cat3':{3:'Cruiser Bicycles'}
}
print(categories)

def dict_comprehension():
    sq={x:x**2 for x in range(1,6)}
    print (sq)

    key=['a','b','c','d','e']
    values=[1,2,3,4,5]

    d={k:v for (k,v) in zip(key,values)}
    print(d)

    c={fruit:len(fruit) for fruit in ['apple','banana','cherry']}
    print(c)

    e={x:x**3 for x in range(10) if x**3 % 4==0}
    print(e)


##############################################################
dict_comprehension()