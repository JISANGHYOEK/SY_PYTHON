old_file = open("test/wish.txt", "r",encoding='UTF-8')
new_file = open("test/wish_copy.txt", "w",encoding='UTF-8')

old_list = old_file.readlines()
for i in old_list:
    new_file.write(i)

old_file.close()
new_file.close()