print("Enter an array of Integers:")
array=list(map(int,input().split()))

k=int(input("enter the target value:"))

found=False
length=0
for i in range(len(array)):
    sum=0
    for j in range(i,len(array)):
        sum= sum+array[j]
        if sum == k :
            found = True
            length =max(length,j-i+1)
        
if not found:
    print("0") 
else:
    print(length)   
#####################################################
print("Enter an array of Integers:")
array=list(map(int,input().split()))
found=False

for i in range(len(array)):
    for j in range(i,len(array)):
        if array[i]==array[j]:
            print("repeated at:",j+1)
            found=True
            break
    if found:
        break
###############################################

print("Enter an array of positive Integers:")
array=list(map(int,input().split()))

k=int(input("enter the window :"))

for i in range(len(array)-k+1):
    sum=0
    for j in range(i,i+k):
        sum +=array[j] 
    print(f"Sum of window of {k}",sum)