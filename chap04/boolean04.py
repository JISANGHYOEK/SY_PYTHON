#나연이의 정보
name = '이나연'
age = 20
height = 170
weight = 50
gender = '여성'
location = '서울'
user_id = 'nayeoni@abc.d.y'
user_pw = '1234'
test_1 = 57
test_2 = 65

print(gender == '여성')
print(name[0] == '김')
print(location == '서울' and height >= 160)
print(19 <= age <= 34)

bmi = weight / (height / 100) ** 2
print(bmi >= 23.0 and bmi <= 24.9)
print((test_1 + test_2)/2 < 60)
print(test_1 >= 60 or test_2 >= 60)

print(user_id.find('@') > 0)
print()

input_id = input("id: ")
input_pw = input("pw: ")
print(user_id == input_id and user_pw == input_pw)
