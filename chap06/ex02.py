person = ['김이준', 20, 180, '남성', 'B', '서울']
print(person)
person.remove("B") #pop은 배열 위치 값 삭제, remove는 동일한 값을 삭제
print(person)
blood = ["B", "+"]
person.insert(4, blood)
print(person)
print(person[4])
print(person[4][1])