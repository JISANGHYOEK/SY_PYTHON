import random

lotto_list = []
input_list = []

def get_lotto():
    while len(lotto_list) < 6:
        rand_num = random.randint(1,45)
        if rand_num not in lotto_list:
            lotto_list.append(rand_num)
    lotto_list.sort()
    print("-----번호가 생성되었습니다.-----")
    return lotto_list

def input_lotto():
    while len(input_list) < 6:
        input_num = int(input("1~45사이의 번호를 입력해주세요: "))
        if input_num > 46:
            print("45보다 큰 수를 입력하였습니다. 다시 입력하세요.")
        elif input_num in input_list:
            print("중복된 번호입니다. 다시 입력하세요..")
        else:
            input_list.append(input_num)
            print(f"현재까지 입력한 번호: {input_list}")
    input_list.sort()
    print(f"최종 입력된 번호: {input_list}")
    return input_list

def compare_two_list(list_1,list_2):
    count = 0
    for i in list_2:
        if i in list_1:
            count += 1
    return count

new_lotto_list = get_lotto()
new_input_list = input_lotto()
new_count = compare_two_list(new_lotto_list,new_input_list)
print(f"입력한 번호 {new_input_list}\n로또 번호는 {new_lotto_list}")
print(f"맞춘 번호는 {new_count}개 입니다.")