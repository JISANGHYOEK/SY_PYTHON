#20분에 한 번 분열 / 1시간 후에는 몇 마리?
print(2**3)
#2시간이라면
print(2**(3*2))

#10시간이라면
print(2**(3*10))

hour = int(input("시간을 입력하세요: "))
cell_count = 2 ** (3*hour)
print(f"1마리의 대장균은 {hour}시간이 지나면 {cell_count:,}마리로 분열합니다.")