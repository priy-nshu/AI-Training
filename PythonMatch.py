from dataclasses import dataclass 
from random import randint

@dataclass # Similar to a Struct in other languages, provides an easy way to create classes that are primarily used to store data
class Point:
    x: int
    y: int

def describe_point(point):
    match point:
        case Point(x=0,y=0):
            return "Origin"
        case Point(x=0,y=y):
            return f"On the Y-axis at {y}"
        case Point(x=x,y=0):
            return f"On the X-axis at {x}"
        case Point():
            return "Somewhere else"
        case _:
            return "Not a point"
        
def num_check(x):
    match x:
        case 10|20|30:
            print(f"Matched: {x}")
        case 15 if x % 3 == 0:
            print(f"Matched: {x} but is not even")
        case 19:
            print(f"Matched: {x} but is not even")
        case _:
            print("No match found")

def person(person):
    match person:
        case {"name": name, "age": age} if age >= 18:
            return f"Name: {name}, Age: {age}."
        case {"name": name}:
            return f"Name: {name}"
        case _:
            return "Invalid person data."

def process(data):
    match data:
        case[x,y]:
            print(f'Two-element list: {x}, {y}')
        case[x,y,z]:
            print(f'Three-element list: {x}, {y}, {z}')
        case _:
            print("Unknown data format")


point1 = Point(0, 0)
point2 = Point(0, 5)
point3 = Point(5, 0)
point4 = Point(3, 4)

print(describe_point(point1)) 
print(describe_point(point2))  
print(describe_point(point3)) 
print(describe_point(point4))
print()


for _ in range(randint(2, 5)):
    num_check(randint(1, 30)) 

print()
print(person({"name": "Alice", "age": 30}))
print(person({"name": "Bob"}))
print(person({"city": "New York"}))

print()
process([1, 2])
process([1, 2, 3])
process([1, 2, 3, 4])