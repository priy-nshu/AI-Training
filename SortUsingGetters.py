from operator import itemgetter,attrgetter

class Student:
    def __init__(self,name,grade,age):
        self.name =name
        self.grade=grade
        self.age=age
    
    def __repr__(self):
        return repr((self.name,self.grade,self.age))
        
student_objects=[
        Student('john','A',15),
        Student('jane','B',12),
        Student('dave','A',10)
    ]        

student_tuples=student_objects

print(sorted(student_objects,key=lambda student:student.age))
#sorted(student_objects,key=itemgetter(2))
print(sorted(student_objects,key=attrgetter('age')))
print(sorted(student_objects,key=attrgetter('grade','age')))

s=sorted(student_objects,key=attrgetter('age'))
print(sorted(s,key=attrgetter('grade'),reverse=True))

def multisort(xs,specs):
    for key,reverse in reversed(specs):
        xs.sort(key=attrgetter(key),reverse=reverse)
    return xs

sorted1=multisort(list(student_tuples),(('grade',True),('age',False)))
print(sorted1)

from math import isnan
from itertools import filterfalse

data=[3,3,float('nan'),1.1,2,2]
sorted(filterfalse(isnan,data))

data=['twelve','11',10]
sorted(map(str,data))

data=[3.3,None,1.1,2.2]
sorted(x for x in data if x is not None)