width = int(input("너비: "))
height = int(input("높이: "))
figure = input("삼각형 or 사각형: ")

if figure == "삼각형":
    area = width * height / 2
elif figure == "사각형":
    area = width * height
else:
    area = 0

if area != 0:
    print(f"{figure}의 면적은 {area} 입니다.")
else:
    print("다시 입력하세요: ")