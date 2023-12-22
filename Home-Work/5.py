# square
def square(n):
    list = []
    for i in range (1, n+1):
        s = i ** 2
        list.append(s )
    return list
n = int(input("enter "))
print(square(n ))
