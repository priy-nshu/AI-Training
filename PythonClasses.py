class Dog:
    kind = 'canine'

    def __init__(self, name , age):
        self.name = name
        self.age = age

    def description(self):
        return f'{self.name} is {self.age} years old.'
    def speak(self, sound):
        return f'{self.name} says {sound}'

my_dog = Dog('Buddy', 5)
ur_dog = Dog('Max', 3)

print(my_dog.name)
print(my_dog.kind)
print(my_dog.age)

print(my_dog.description())
print(ur_dog.description())
print(my_dog.speak('Woof'))
print(ur_dog.speak('Bark'))

#------------------------------------------------

class Dog:
    trick = []
    def __init__(self, name,trick):#if trick is constructor then its unique for each object, else its shared by all the instances of the class
        self.name = name
        self.trick = trick

    def add_trick(self, trick):
        self.trick.append(trick)

d1 = Dog('Fido','roll over')
d2 = Dog('Buddy','play dead')

print(d1.trick) 
print(d2.trick) 