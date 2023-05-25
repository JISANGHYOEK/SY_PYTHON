from tkinter import *
import random

#이벤트 함수 정의
def random_num():
    return random.randint(0,len(text_list)-1)

def btn_func():
    label.configure(text=text_list[random_num()])

text_list = [
    '친구와 사이좋게 지내기',
    '물을 멀리하기',
    '돈 보다는 명예',
    '일단 고',
    '책을 가까이 하기'
]

#화면 생성
window = Tk()
window.title("window name")
window.geometry("500x500")
window.resizable(width=FALSE, height=TRUE)

#UI 생성
label = Label(window, text="라벨입니다.")
btn = Button(window, text="클릭", fg="red", command=btn_func)

#UI 배치
label.pack()
btn.pack()

#메인루프 실행
window.mainloop()