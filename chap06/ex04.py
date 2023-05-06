menus = ["김치찌개", "김밥", "떡국", "칼국수", "냉면", "떡볶이"]
prices= [6000, 3000, 5000, 5000, 6000, 3000]

menu = input("메뉴 이름을 입력하세요: ")
price = prices[menu.index(menu)]
print(f"{menu}의 가격은 {price}원 입니다.")