import random

num_1, num_2 = random.randint(1,10), random.randint(1,10)
result = int(input(f"{num_1} * {num_2} = "))

if result == num_1 * num_2:
    print("정답입니다.")
else:
    print("정답이 아닙니다.")