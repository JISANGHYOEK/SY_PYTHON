#윤년 구하기
year = int(input("Enter year: "))

print(year%4==0 and year%100!=0 or year%400==0)