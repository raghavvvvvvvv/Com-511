

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
