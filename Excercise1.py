prime_Limit =int(input("Please enter the limit for prime numbers: "))
for n in range(2, prime_Limit):
    for x in range(2, n//2 + 1):
        if n % x == 0:
            continue
    else:
        print(n, 'is a prime number')


OverOrUnder=int(input("Please enter a multi-digit number: "))
for x in range(2, OverOrUnder//2 + 1):
    if x ** 2 == OverOrUnder:
        print(OverOrUnder, 'is a perfect square of', x)
        break
    elif x ** 2 > OverOrUnder :
        diff=min(x ** 2 - OverOrUnder, OverOrUnder - (x-1) ** 2)
        break
if diff < (x ** 2 - OverOrUnder):
    print(OverOrUnder, 'should be subtracted by', diff)
else:
    print(OverOrUnder, 'should be added by', diff)

count = 0
for x in range(1, 1000):
    perfect_number = sum(i for i in range(1, x) if x % i == 0)
    if perfect_number == x:
        count += 1
        print(x, 'is a perfect number')
    if count == 4:
        break