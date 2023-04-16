age, temp = input("나이와 체온을 입력하세요: ").split()
age, temp = int(age), float(temp)

if age<=2:
    if 36.4 <= temp <= 38.0:
        result = '정상 체온'
    else:
        result = '비정상 체온'
elif age <=10:
    if 36.1 <= temp <= 37.8:
        result = '정상 체온'
    else:
        result = '비정상 체온'
elif age <=64:
    if 35.9 <= temp <= 37.6:
        result = '정상 체온'
    else:
        result = '비정상 체온'
else:
    if 35.8 <= temp <= 37.5:
        result = '정상 체온'
    else:
        result = '비정상 체온'

print(f"{age}세, {temp}도는 {result}입니다.")