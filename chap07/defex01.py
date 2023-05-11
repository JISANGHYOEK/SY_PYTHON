def sum(x):
    sum = 0
    for i in range(1, x+1, 1):
        sum += i
    return sum

def sum2(x):
    sum = 0
    for i in range(2, x+1, 1):
        sum += i
    return sum

def sum3(x):
    sum = 0
    for i in range(1, x+1, 1):
        if(i%2==0): sum += i
    return sum

print(sum(10))
print(sum2(10))
print(sum3(10))
