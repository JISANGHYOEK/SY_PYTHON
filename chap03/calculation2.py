str_1, str_2 = input("두 개의 숫자를 입력하세요 : ").split()
oper = input("연산자를 입력하세요: ")

result = eval(str_1 + oper + str_2)
print(f"계산결과 : {str_1} {oper} {str_2} = {result}")