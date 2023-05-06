person = ["김이준", 20, "남성"]
print(person)

print(person[0])
print(person[1])
print(person[2])
print("-----------------------------------------------")

person.append("A형")
person.append("서울")
print(person)
print(person[4])
print(person[-1])
print("-----------------------------------------------")

print(person)
print(person[0:2]) #마지막 인덱스 +1 해주기
print(person[:2]) 
print(person[3:5])
print(person[-2:]) #0은 음수가 아니므로 이런 경우에는 끝깞을 생략
print("--------------------------------")

print(person)
person.insert(2, 180) #원하는 위치에 값을 넣기
print(person)
