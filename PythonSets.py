def SetBasics():
    basket={'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
    print(basket) # show that duplicates have been removed

    print('orange' in basket) # fast membership testing
    print('crabgrass' in basket)

    a=set('abracadabra')
    b=set('alacazam')
    print(a,b)
    print(a - b) # letters in a but not in b
    print(a | b) # letters in a or b or both
    print(a & b) # letters in both a and b
    print(a ^ b) # letters in a or b but not both
    IterableSet=set('Hello')
    print(IterableSet)
    NotIerableSet={'Hello'}
    print("NOT",NotIerableSet)
    print(type(IterableSet),type(NotIerableSet))

def MoreBasics():
    employees ={"Alice","Charlie"}
    employees.add("Jane")
    print(employees)

    employees.add("Laura")
    employees.remove("Charlie")
    print(employees)

    employees.discard("Allen")

    employee =employees.pop()
    print(employee)

    employees.clear()
    print(len(employees))

def SetComprehension():
    a={x for x in 'abacadabra' if x not in 'abc'}
    print(a)

    usernames=['Alice','Bob','ALICE','bob','charlie','Charlie',"JOHN"]
    CompSet={name.lower().strip() for name in usernames}
    print(CompSet)

def MoreList():
    rgb_color={(51,255,87),
               (51,87,255),
               (241,196,15),
               (231,76,60)}
    print(rgb_color)

    set1=set({"Smith","McArthur","Wilson","Ram","Smith"})
    print(set1)

    set1={21,'Hi!',3.141,None,'Python'}
    print(set1)

def SetUnion():
    pet_animals ={"dog",'cat','hamster','parrot'}
    farm_animals={'cow','pig','chicken','dog','cat'}
    farmSet= pet_animals.union(farm_animals)
    print(farmSet)

def SetInter():
    john_f={'linda','matthew','carlos'}
    jane_f={'alice','bob','laura'}
    myfriend=john_f.intersection(jane_f)
    print(myfriend)

    #Multiple sets can be intersected

    a={1,2,3,4}
    b={2,3,4,5}
    c={3,4,5,6}
    d={4,5,6,7}

    print(a & b & c & d)
    print(a.intersection(b,c,d))

def SetDiff():
    reg_users={'alice','bob','charlie','diana'}
    checked_inUsers={'alice','charlie'}

    print(reg_users-checked_inUsers)
    print(checked_inUsers-reg_users)

    a={1,2,3,30}
    b={20,30,40,50}
    c={300,400,500,600}

    print("SetDiff")
    print(a-b-c)
    print(a.difference(b,c))

def SymDiff():
     reg_users={'alice','bob','charlie','diana'}
     checked_inUsers={'alice','charlie'}

     print(reg_users^checked_inUsers)
     print(reg_users.symmetric_difference(checked_inUsers))

     a={1,2,3,30}
     b={20,30,40,50}
     c={300,400,500,600}

     print(a^b^c)
     print(a.symmetric_difference(b).symmetric_difference(c))

def setComp():
    required_ingredients ={'cheese','eggs','milk'}
    available_ingredients={'cheese','eggs','milk','sugar','salt'}

    print(required_ingredients <= available_ingredients)
    print(required_ingredients.issubset(available_ingredients))

    a={1,2,3,4,5}
    print('a is a subset of itset:',a<=a)
    print('a is a proper subset of itself',a<a)
    print('a is a superset of a ',a>=a)
    print('a ia a proper superset of a',a>a)

    regular_plan={'Tutorials','Quizzes'}
    premiun_plan={'Tutorials','Video Courses','Quizzes','Books'}

    print("super set:",premiun_plan>regular_plan)

def verify_purchase(age, selection, restricted_products):
    # Convert lists to sets so we can use set operations
    selection = set(selection)
    restricted_products = set(restricted_products)

    if age < 21 and not selection.isdisjoint(restricted_products):
        print("Purchase denied: selection includes age-restricted products")
    else:
        print("Product approved")


def MoreSetOps():
    cities = {"Vancouver", "Berlin", "London", "Warsaw", "Vienna"}

    # Alphabetical sorting
    for city in sorted(cities):
        print(city)

    print()

    cities = {
        ("Vancouver", 6715000),
        ("Berlin", 3800000),
        ("London", 8980000),
        ("Warsaw", 1790000),
        ("Vienna", 1900000),
    }

    # Sort by population (ascending)
    for city in sorted(cities, key=lambda city: city[1]):
        print(city)

    print()

    # Sort by population (descending)
    for city in sorted(cities, key=lambda city: city[1], reverse=True):
        print(city)


    # Function calls
    verify_purchase(
        age=18,
        selection=["milk", "bread", "beer"],
        restricted_products=["alcohol", "beer", "cigarettes"]
    )




########################################################################
SetBasics()
MoreBasics()
SetComprehension()
MoreList()
SetUnion()
SetInter()
SetDiff()
SymDiff()
setComp()
MoreSetOps