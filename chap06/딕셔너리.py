person = {"name": "김이준",
         "age": 20,
         "gender": "남성"}

print(person)
print(person["age"])

print("-----------------")

person["혈액형"] = "B"
person["거주지"] = "서울"
print(person)

print("-----------------")

blood = { "ABO": "B",
         "Rh": "+"}
person["혈액형"] = blood
print(person)
print(person["혈액형"]["Rh"])

print("-----------------")

for i in person:
    print(i)

print("----------------")
for i in person:
    print(person[i])