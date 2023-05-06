menus = ["김치찌개", "김밥", "떡국", "칼국수", "냉면", "떡볶이"]
prices= [6000, 3000, 5000, 5000, 6000, 3000]

menu = input("추가할 메뉴를 입력하세요.: ")
price = int(input("해당 음식의 가격을 입력하세요: "))

print(f"입력한 음식은 {menu}, 가격은 {price}원 입니다.")

menus.append(menu)
prices.append(price)

print(menus)
print(prices)