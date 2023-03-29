a, b = map(int,input("두 개의 숫자를 입력하세요: ").split())
c = input("연산할 기호를 입력하세요: ")
if(c=='+'):
    print(f"{a} {c} {b} = {a+b:,}")
elif(c=='-'):
    print(f"{a} {c} {b} = {a-b:,}")
elif(c=='/'):
    print(f"{a} {c} {b} = {a/b:,}")
elif(c=='*'):
    print(f"{a} {c} {b} = {a*b:,}")
else:
    print("잘못된 입력입니다.")