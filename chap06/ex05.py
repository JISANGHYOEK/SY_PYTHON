menus = ["김치찌개", "김밥", "떡국", "칼국수", "냉면", "떡볶이"]
prices= [6000, 3000, 5000, 5000, 6000, 3000]

print(menus)
print(prices)

menu = input("삭제할 음식 이름을 입력하세요: ")

if(menu in menus):
    price = prices[menus.index(menu)]
    print(f"{menu}, {price}원을 리스트에서 삭제합니다.")

    menus.remove(menu)
    prices.remove(price)
else:
    print(f"{menu}는 없습니다.")

print("----------------------------------")
print(menus)
print(prices)