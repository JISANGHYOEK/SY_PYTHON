birth_month = int(input("당신이 태어난 달을 입력하세요: "))
birth_day = int(input("당신이 태어난 일을 입력하세요: "))
step_1 = (birth_month * 4 + 2) * 25
step_2 = step_1 + birth_day - 50
print(step_2)

