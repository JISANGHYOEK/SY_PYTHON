x, y = map(int,input("x, y: ").split())

if x==y:
    print(f"{x} = {y}")
elif x > y:
    print(f"{x} > {y}")
else:
    print(f"{x} < {y}")