# Dictionary
dict = {}
n = int(input())
for i in range(n):
    key = input()
    value  = input()
    dict[key] = value
for i in  dict.keys():
    print(i, end=" ")
for i in  dict.values():
    print(i, end=" ")





#bit count
n = int(input("Enter "))
count = 0 
while n :
    count+= n & 1
    n>>=1
print(count)






# unique values 
list = []
n = int(input())

for i in range (n):
    add = int (input())
    list.append(add)
unique = set (list)
print("unique values are :")
for i in unique :
    print(i)




# square
def square(n):
    list = []
    for i in range (1, n+1):
        s = i ** 2
        list.append(s )
    return list
n = int(input("enter "))
print(square(n ))

