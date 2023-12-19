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
