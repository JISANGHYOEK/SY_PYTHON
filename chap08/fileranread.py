import random

wish = open("test/wish.txt", "r", encoding="UTF-8")
wish_list = wish.readlines()
wish.close()

random = random.randint(0,len(wish_list)-1)
print(wish_list[random])