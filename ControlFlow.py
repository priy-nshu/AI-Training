def SimpleFlow():
    marks = 45
    res = "Pass" if marks >= 40 else "Fail"   # ternary operation
    print(f"Result: {res}")  # f is like $ in C#

    x = int(input("Please enter an integer: "))
    print(x)
    if x < 0:
        x = 0
        print('Negative changed to zero')
    elif x == 0:
        print('Zero')
    elif x == 1:
        print('Single')
    else:
        print('More')

def ForWithElse():
    for n in range(2, 10):
        for x in range(2, n):
            if n % x == 0:
                print(n, 'equals', x, '*', n//x)
                break
        else:
            print(n, 'is a prime number')

def MoreFor():
    users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

    for user, status in users.copy().items():
        if status == 'inactive':
            del users[user]

    print(users)

    active_users = {}
    for user, status in users.items():
        if status == 'active':
            active_users[user] = status

    print(active_users)

def WhileWithElse():
    import random ,time

    max_retries = 5
    attemps = 0
    while attemps < max_retries:
        attemps += 1
        print(f"Attempt {attemps} :Connecting to server...")

        time.sleep(0.3) 
         # Simulate connection delay
        if random.choice([False,False,False,True]):
            print("Success!")
            break
        print("Failed, retrying...")
    else:
        print("All attempts failed.")

#SimpleFlow()
#ForWithElse()
#MoreFor()
WhileWithElse()