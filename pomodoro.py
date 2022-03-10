from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #

#FF5C58
#FE8F8F
#FCD2D1
#FFEDD3
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1
    
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    
    if reps % 8 == 0:
        count_down(long_break_sec)
        
    elif reps % 2 ==0:
        count_down(short_break_sec)
        
    else:
        count_down(work_sec)
        
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec == 0:
        count_sec = "00"
    elif count_sec < 10:
        count_sec = f"0{count_sec}"
    
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        
# ---------------------------- UI SETUP ------------------------------- #
# 1. 앱의 사이즈 결정

# 2. UI 구성(grid 활용)

window = Tk()
window.title("Your Own Pomodoro")
window.config(padx=70, pady=70, bg="#FF5C58")

canvas = Canvas(width=400, height=500, bg="#FE8F8F", highlightthickness=0)
canvas.grid(row=1, column=1)
timer_text = canvas.create_text(200, 235, text="00:00", font=("Courier", 80, "bold"), fill="white")

start_btn = Button(canvas, text="Start", width=20, height=5, bg="#FFEDD3", command=start_timer)
start_btn.place(x=150, y=300)

name_label = Label(text="Your Own 🍅", bg="#FF5C58")
name_label.grid(row=0, column=0)

setting_btn = Button(text="Setting", highlightthickness=0, bg="#FFEDD3")
setting_btn.grid(row=0, column=4)


window.mainloop()