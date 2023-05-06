a = (1, 3, 5, 7, 9)
print(a)
print(type(a))

b= tuple(i for i in range(10) if i % 2 != 0)
print(b)
print(type(b))

print(max(b) + min(b))
print(sum(b))
print("------------------------------------")

c = list(b) #반대도 가능 c = tuple(b)
print(c)
print(type(c))