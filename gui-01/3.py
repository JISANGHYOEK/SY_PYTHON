from tkinter import *

#이벤트 함수
def validate(*agrs):
    if new_pw.get() == "":
        state_label.configure(text="")
    elif new_pw.get() == confirm_pw.get():
        state_label.configure(text = "패스워드 일치!", foreground="green")
    else:
        state_label.configure(text = "에러: 패스워드 불일치!", foreground="red")

def change_btn_func():
    if new_pw.get() == "":
        state_label.configure(text="")
    elif new_pw.get() == confirm_pw.get():
        state_label.configure(text = "패스워드 변경완료", foreground="green")
    else:
        state_label.configure(text = "에러: 패스워드 변경 취소!", foreground="red")

#윈도우 생성
window = Tk()
window.geometry("500x130")
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=1)

#입력 데이터
new_pw = StringVar()
confirm_pw = StringVar()
confirm_pw.trace("w", validate)

#UI 만들고 배치
state_label = Label(window, text="")
state_label.grid(column=0, row=0, columnspan=3, padx=5, pady=5)
label = Label(window, text="New Password: ").grid(column=0, row=1, padx=5, pady=5)
label = Label(window, text="Confirm Password: ").grid(column=0, row=2, padx=5, pady=5)

new_entry = Entry(window, textvariable=new_pw, show="*")
new_entry.grid(column=1, row=1, padx=5, pady=5)
new_entry.focus()

confirm_entry = Entry(window, textvariable=confirm_pw, show="*")
confirm_entry.grid(column=1, row=2, padx=5, pady=5)

change_btn = Button(window, text="Change", command=change_btn_func)
change_btn.grid(column=1, row=3, padx=5, pady=5)

#윈도우 실행
window.mainloop()