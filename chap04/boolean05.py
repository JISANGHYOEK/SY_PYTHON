x,y = map(int,input("enter x y: ").split())

print(x>0 and y>0, "1사분면")
print(x<0 and y>0, "2사분면")
print(x<0 and y<0, "3사분면")
print(x>0 and y<0, "4사분면")
