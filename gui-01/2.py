from tkinter import *

#이벤트 함수
def submit():
    label.configure(text=name_var.get())

def it_has_been_written(*args):
    if name_var.get() == ' ':
        label.configure(text="")
    else:
        label.configure(text="typing...")
                        
#윈도우 생성
window = Tk()
window.geometry("400x100")
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=1)


#데이터
name_var = StringVar()
name_var.trace("w", it_has_been_written)

#UI 만들기
Label(window, text="Name: ").grid(column=0, row=0, padx=5, pady=5)
name = Entry(window, textvariable=name_var)
btn = Button(window, text="Submit", command=submit)
label = Label(window, text="입력창에 텍스트를 작성하고 버튼을 클릭하세요.")

#UI 배치
name.grid(column=1, row=0, padx=5, pady=5)
btn.grid(column=2, row=0, padx=5, pady=5)
label.grid(column=1, row = 1, padx=5, pady=5)

#메인루프 실행
window.mainloop()