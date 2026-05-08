matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
def Nested_ListComprehension():
    print ([[row[i] for row in matrix]for i in range(3)])
    transpose=[]
    for i in range(3):
        transpose.append([row[i] for row in matrix])
    print("transpose:", transpose)
    print("zip:", list(zip(*matrix)))

Nested_ListComprehension()