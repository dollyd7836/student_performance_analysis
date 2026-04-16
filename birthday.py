'''import tkinter as tk
from tkinter import messagebox
import threading
import time
import random
import winsound

root = tk.Tk()
root.title("💖 Secret Birthday Unlock 💖")
root.geometry("450x500")
root.config(bg="#ffc0cb")

q_index = 0

questions = [
    {"question": "😏 Who is the most annoying person in your life?",
     "options": ["Me 😏", "You 😎", "No one"], "correct": None},

    {"question": "🍕 What is your favorite thing?",
     "options": ["Food 😋", "Sleep 😴", "Me 💖"], "correct": "Me 💖"},

    {"question": "🎂 Will you share your birthday cake with me?",
     "options": ["Yes 💖", "No 😤"], "correct": "Yes 💖"},

    {"question": "📱 Who do you love more?",
     "options": ["Phone 📱", "Me 💕", "Friends"], "correct": "Me 💕"},

    {"question": "😂 Who wins in fights?",
     "options": ["Me 😎", "You 😏", "No one"], "correct": None},

    {"question": "💖 Who loves you the most?",
     "options": ["Me 💕", "Friends", "Phone 📱"], "correct": "Me 💕"}
]

# 🔝 Top
top_frame = tk.Frame(root, bg="#ffc0cb")
top_frame.pack(fill="x")

title = tk.Label(top_frame,
    text="💖✨ Tripti's Secret Unlock ✨💖",
    font=("Georgia", 16, "bold"),
    bg="#ffc0cb", fg="#d63384")
title.pack(pady=10)

progress_label = tk.Label(top_frame,
    text="🔍 Initializing Scan...",
    bg="#ffc0cb")
progress_label.pack()

# 🎯 Middle (Question Center)
middle_frame = tk.Frame(root, bg="#ffc0cb")
middle_frame.pack(expand=True)

question_label = tk.Label(middle_frame,
    text="",
    font=("Arial", 14, "bold"),
    wraplength=350,
    bg="#ffc0cb")
question_label.pack(expand=True)

# 🔽 Bottom (Options)
button_frame = tk.Frame(root, bg="#ffc0cb")
button_frame.pack(pady=20)

# Scanner
def start_scan():
    def scan():
        for t in ["Scanning emotions... 💭","Checking sweetness... 🍭","Almost done... 💖"]:
            progress_label.config(text=t)
            time.sleep(1)
        progress_label.config(text="Scan Complete ✅")
    threading.Thread(target=scan).start()

# Load question
def load_question():
    global q_index

    for w in button_frame.winfo_children():
        w.destroy()

    if q_index < len(questions):
        q = questions[q_index]
        question_label.config(text=q["question"])

        for opt in q["options"]:
            tk.Button(button_frame,
                text="💖 "+opt+" 💖",
                width=26,
                font=("Comic Sans MS", 11, "bold"),
                bg="#ff69b4",
                fg="white",
                bd=0,
                command=lambda o=opt: check_answer(o)
            ).pack(pady=8)
    else:
        show_gift_box()

# Check answer
def check_answer(selected):
    global q_index
    correct = questions[q_index]["correct"]

    if correct is None:
        messagebox.showinfo("😂","Hahaha 😂")
        q_index+=1
        load_question()

    elif selected == correct:
        messagebox.showinfo("💖","Correct 😎")
        q_index+=1
        load_question()
    else:
        show_access_denied()

# 🚫 Access denied
def show_access_denied():
    for w in root.winfo_children():
        w.destroy()

    f = tk.Frame(root,bg="red")
    f.pack(fill="both",expand=True)

    tk.Label(f,text="🚫 ACCESS DENIED 🚫",
             font=("Arial",18,"bold"),
             bg="red",fg="white").pack(expand=True)

    winsound.Beep(400,500)

    def back():
        time.sleep(2)
        rebuild_ui()

    threading.Thread(target=back).start()

def rebuild_ui():
    for w in root.winfo_children():
        w.destroy()

    global top_frame, middle_frame, button_frame, question_label, progress_label

    top_frame = tk.Frame(root, bg="#ffc0cb")
    top_frame.pack(fill="x")

    tk.Label(top_frame,
        text="💖✨ Tripti's Secret Unlock ✨💖",
        bg="#ffc0cb", fg="#d63384").pack()

    progress_label = tk.Label(top_frame,text="Scan Active...",bg="#ffc0cb")
    progress_label.pack()

    middle_frame = tk.Frame(root, bg="#ffc0cb")
    middle_frame.pack(expand=True)

    question_label = tk.Label(middle_frame,bg="#ffc0cb")
    question_label.pack(expand=True)

    button_frame = tk.Frame(root, bg="#ffc0cb")
    button_frame.pack(pady=20)

    load_question()

# 🎁 Gift box
def show_gift_box():
    for w in root.winfo_children():
        w.destroy()

    canvas = tk.Canvas(root,width=450,height=500,bg="#ffc0cb",highlightthickness=0)
    canvas.pack()

    lid = canvas.create_rectangle(140,170,310,220,fill="#ff1493")
    box = canvas.create_rectangle(150,220,300,350,fill="#ff69b4")

    canvas.create_text(225,120,text="🎁 Click to Open 🎁",
                       font=("Arial",14,"bold"))

    def open_box(e):
        for _ in range(25):
            canvas.move(lid,0,-3)
            root.update()
            time.sleep(0.02)
        show_final_message(canvas)

    canvas.bind("<Button-1>", open_box)

# 🎈 Real balloons + pop 💥
def balloons(canvas):
    balloon_items = []
    colors = ["red","blue","yellow","green","pink","purple","orange"]

    for _ in range(8):
        x = random.randint(50,400)
        y = random.randint(300,500)

        b = canvas.create_oval(x,y,x+30,y+40,fill=random.choice(colors),outline="")
        s = canvas.create_line(x+15,y+40,x+15,y+70)

        balloon_items.append((b,s))

    def float_up():
        while True:
            for b,s in balloon_items:
                canvas.move(b,0,-2)
                canvas.move(s,0,-2)

                if canvas.coords(b)[1] < 0:
                    nx = random.randint(50,400)
                    canvas.coords(b,nx,500,nx+30,540)
                    canvas.coords(s,nx+15,540,nx+15,570)
            time.sleep(0.05)

    def pop(event):
        x,y = event.x,event.y
        for b,s in balloon_items:
            c = canvas.coords(b)
            if c[0] < x < c[2] and c[1] < y < c[3]:
                canvas.delete(b)
                canvas.delete(s)

                for _ in range(6):
                    dot = canvas.create_oval(x,y,x+5,y+5,fill="white")

                    def anim(d=dot):
                        for _ in range(5):
                            canvas.move(d,random.randint(-5,5),random.randint(-5,5))
                            time.sleep(0.02)
                        canvas.delete(d)

                    threading.Thread(target=anim).start()

    canvas.bind("<Button-1>", pop)
    threading.Thread(target=float_up, daemon=True).start()

# 🎊 Final screen
def show_final_message(canvas):
    canvas.delete("all")

    balloons(canvas)

    canvas.create_text(225,200,
        text="🎉 Happy Birthday Tripti 🎂",
        font=("Georgia",16,"bold"),
        fill="#d63384")

    canvas.create_text(225,260,
        text="🎀 Meri chotuu si sweet bhenaa\nEnjoy your day 🎉",
        font=("Arial",12),
        fill="#d63384")

    play_music()

# 🎶 Music
def play_music():
    notes=[(264,300),(264,200),(297,500),(264,500)]
    for f,d in notes:
        winsound.Beep(f,d)

# Start
start_scan()
load_question()
root.mainloop()'''









'''

import tkinter as tk
from tkinter import messagebox
import threading
import time
import random
import winsound

root = tk.Tk()
root.title("💖 Secret Birthday Unlock 💖")
root.geometry("450x500")
root.config(bg="#ffc0cb")

q_index = 0
score = 0

questions = [
    {"question": "😏 Who is the most annoying person in your life?",
     "options": ["Me 😏", "You 😎", "No one"], "correct": None},

    {"question": "🍕 What is your favorite thing?",
     "options": ["Food 😋", "Sleep 😴", "Me 💖"], "correct": "Me 💖"},

    {"question": "🎂 Will you share your birthday cake with me?",
     "options": ["Yes 💖", "No 😤"], "correct": "Yes 💖"},

    {"question": "📱 Who do you love more?",
     "options": ["Phone 📱", "Me 💕", "Friends"], "correct": "Me 💕"},

    {"question": "😂 Who wins in fights?",
     "options": ["Me 😎", "You 😏", "No one"], "correct": None},

    {"question": "💖 Who loves you the most?",
     "options": ["Me 💕", "Friends", "Phone 📱"], "correct": "Me 💕"}
]

# 🔝 Top
top_frame = tk.Frame(root, bg="#ffc0cb")
top_frame.pack(fill="x")

title = tk.Label(top_frame,
    text="💖✨ Tripti's Secret Unlock ✨💖\nScore: 0 🎯",
    font=("Georgia", 16, "bold"),
    bg="#ffc0cb", fg="#d63384")
title.pack(pady=10)

progress_label = tk.Label(top_frame,
    text="🔍 Initializing Scan...",
    bg="#ffc0cb")
progress_label.pack()

# 🎯 Middle
middle_frame = tk.Frame(root, bg="#ffc0cb")
middle_frame.pack(expand=True)

question_label = tk.Label(middle_frame,
    text="",
    font=("Arial", 14, "bold"),
    wraplength=350,
    bg="#ffc0cb")
question_label.pack(expand=True)

# 🔽 Bottom
button_frame = tk.Frame(root, bg="#ffc0cb")
button_frame.pack(pady=20)

# Scanner
def start_scan():
    def scan():
        for t in ["Scanning emotions... 💭","Checking sweetness... 🍭","Almost done... 💖"]:
            progress_label.config(text=t)
            time.sleep(1)
        progress_label.config(text="Scan Complete ✅")
    threading.Thread(target=scan).start()

# Load question
def load_question():
    global q_index

    for w in button_frame.winfo_children():
        w.destroy()

    if q_index < len(questions):
        q = questions[q_index]
        question_label.config(text=q["question"])

        for opt in q["options"]:
            tk.Button(button_frame,
                text="💖 "+opt+" 💖",
                width=26,
                font=("Comic Sans MS", 11, "bold"),
                bg="#ff69b4",
                fg="white",
                bd=0,
                command=lambda o=opt: check_answer(o)
            ).pack(pady=8)
    else:
        show_gift_box()

# Check answer
def check_answer(selected):
    global q_index, score
    correct = questions[q_index]["correct"]

    if correct is None:
        score += 1
        title.config(text=f"💖✨ Tripti's Secret Unlock ✨💖\nScore: {score} 🎯")
        messagebox.showinfo("😂","Hahaha 😂")
        q_index+=1
        load_question()

    elif selected == correct:
        score += 2
        title.config(text=f"💖✨ Tripti's Secret Unlock ✨💖\nScore: {score} 🎯")
        messagebox.showinfo("💖","Correct 😎")
        q_index+=1
        load_question()
    else:
        show_access_denied()

# 🚫 Access denied
def show_access_denied():
    for w in root.winfo_children():
        w.destroy()

    f = tk.Frame(root,bg="red")
    f.pack(fill="both",expand=True)

    tk.Label(f,text="🚫 ACCESS DENIED 🚫",
             font=("Arial",18,"bold"),
             bg="red",fg="white").pack(expand=True)

    winsound.Beep(400,500)

    def back():
        time.sleep(2)
        rebuild_ui()

    threading.Thread(target=back).start()

def rebuild_ui():
    for w in root.winfo_children():
        w.destroy()

    global top_frame, middle_frame, button_frame, question_label, progress_label

    top_frame = tk.Frame(root, bg="#ffc0cb")
    top_frame.pack(fill="x")

    tk.Label(top_frame,
        text=f"💖✨ Tripti's Secret Unlock ✨💖\nScore: {score} 🎯",
        bg="#ffc0cb", fg="#d63384").pack()

    progress_label = tk.Label(top_frame,text="Scan Active...",bg="#ffc0cb")
    progress_label.pack()

    middle_frame = tk.Frame(root, bg="#ffc0cb")
    middle_frame.pack(expand=True)

    question_label = tk.Label(middle_frame,bg="#ffc0cb")
    question_label.pack(expand=True)

    button_frame = tk.Frame(root, bg="#ffc0cb")
    button_frame.pack(pady=20)

    load_question()

# 🎁 Gift box
def show_gift_box():
    for w in root.winfo_children():
        w.destroy()

    canvas = tk.Canvas(root,width=450,height=500,bg="#ffc0cb",highlightthickness=0)
    canvas.pack()

    lid = canvas.create_rectangle(140,170,310,220,fill="#ff1493")
    box = canvas.create_rectangle(150,220,300,350,fill="#ff69b4")

    canvas.create_text(225,120,text="🎁 Click to Open 🎁",
                       font=("Arial",14,"bold"))

    def open_box(e):
        for _ in range(25):
            canvas.move(lid,0,-3)
            root.update()
            time.sleep(0.02)
        show_final_message(canvas)

    canvas.bind("<Button-1>", open_box)

# 🎈 Balloons + Golden balloon
def balloons(canvas):
    global score
    balloon_items = []

    for _ in range(7):
        x = random.randint(50,400)
        y = random.randint(300,500)

        b = canvas.create_oval(x,y,x+30,y+40,fill=random.choice(
            ["red","blue","green","pink","purple"]),outline="")
        s = canvas.create_line(x+15,y+40,x+15,y+70)

        balloon_items.append((b,s,1))

    # golden
    x = random.randint(50,400)
    y = random.randint(300,500)
    gb = canvas.create_oval(x,y,x+35,y+45,fill="gold",outline="")
    gs = canvas.create_line(x+18,y+45,x+18,y+75)
    balloon_items.append((gb,gs,5))

    def float_up():
        while True:
            for b,s,val in balloon_items:
                canvas.move(b,0,-2)
                canvas.move(s,0,-2)

                if canvas.coords(b)[1] < 0:
                    nx = random.randint(50,400)
                    canvas.coords(b,nx,500,nx+30,540)
                    canvas.coords(s,nx+15,540,nx+15,570)
            time.sleep(0.05)

    def pop(event):
        global score
        x,y = event.x,event.y

        for b,s,val in balloon_items:
            c = canvas.coords(b)
            if c[0] < x < c[2] and c[1] < y < c[3]:
                canvas.delete(b)
                canvas.delete(s)

                score += val
                title.config(text=f"💖✨ Tripti's Secret Unlock ✨💖\nScore: {score} 🎯")

                for _ in range(6):
                    dot = canvas.create_oval(x,y,x+5,y+5,fill="white")

                    def anim(d=dot):
                        for _ in range(5):
                            canvas.move(d,random.randint(-5,5),random.randint(-5,5))
                            time.sleep(0.02)
                        canvas.delete(d)

                    threading.Thread(target=anim).start()

    canvas.bind("<Button-1>", pop)
    threading.Thread(target=float_up, daemon=True).start()

# 🎊 Final screen
def show_final_message(canvas):
    canvas.delete("all")

    balloons(canvas)

    canvas.create_text(225,180,
        text="🎉 Happy Birthday Tripti 🎂",
        font=("Georgia",16,"bold"),
        fill="#d63384")

    canvas.create_text(225,240,
        text="🎀 Meri chotuu si sweet bhenaa\nEnjoy your day 🎉",
        font=("Arial",12),
        fill="#d63384")

    btn = tk.Button(root,text="💌 Secret Message",
                    bg="#ff69b4",fg="white",
                    command=secret_popup)
    btn.place(x=150,y=420)

    play_music()

# 💌 Secret message
def secret_popup():
    messagebox.showinfo("💖 Secret",
        "You are the best sister ever 💕\nStay happy always 😘")

# 🎶 Music
def play_music():
    notes=[(264,300),(264,200),(297,500),(264,500)]
    for f,d in notes:
        winsound.Beep(f,d)

# Start
start_scan()
load_question()
root.mainloop()'''








import tkinter as tk
from tkinter import messagebox
import threading
import time
import random
import winsound

root = tk.Tk()
root.title("💖 Secret Birthday Unlock 💖")
root.geometry("450x500")
root.config(bg="#ffc0cb")

q_index = 0
score = 0

questions = [
    {"question": "😏 Who is the most annoying person in your life?",
     "options": ["Me 😏", "You 😎", "No one"], "correct": None},

    {"question": "🍕 What is your favorite thing?",
     "options": ["Food 😋", "Sleep 😴", "Me 💖"], "correct": "Me 💖"},

    {"question": "🎂 Will you share your birthday cake with me?",
     "options": ["Yes 💖", "No 😤"], "correct": "Yes 💖"},

    {"question": "📱 Who do you love more?",
     "options": ["Phone 📱", "Me 💕", "Friends"], "correct": "Me 💕"},

    {"question": "😂 Who wins in fights?",
     "options": ["Me 😎", "You 😏", "No one"], "correct": None},

    {"question": "💖 Who loves you the most?",
     "options": ["Me 💕", "Friends", "Phone 📱"], "correct": "Me 💕"}
]

# 🔝 Top Frame
top_frame = tk.Frame(root, bg="#ffc0cb")
top_frame.pack(fill="x")

title = tk.Label(
    top_frame,
    text="💖✨ Tripti's Secret Unlock ✨💖\nScore: 0 🎯",
    font=("Georgia", 20, "bold"),   # 🔥 Bigger font
    bg="#ffc0cb", fg="#d63384"
)
title.pack(pady=10)

progress_label = tk.Label(
    top_frame,
    text="🔍 Initializing Scan...",
    font=("Arial", 11),
    bg="#ffc0cb"
)
progress_label.pack()

# 🎯 Middle Frame (CENTER ALIGN FIX)
middle_frame = tk.Frame(root, bg="#ffc0cb")
middle_frame.pack(expand=True)

# Spacer to push question to center
tk.Label(middle_frame, bg="#ffc0cb").pack(expand=True)

question_label = tk.Label(
    middle_frame,
    text="",
    font=("Arial", 16, "bold"),   # 🔥 Bigger question font
    wraplength=350,
    bg="#ffc0cb",
    justify="center"
)
question_label.pack()

# Options frame JUST BELOW question
button_frame = tk.Frame(middle_frame, bg="#ffc0cb")
button_frame.pack(pady=15)

# Bottom spacer
tk.Label(middle_frame, bg="#ffc0cb").pack(expand=True)

# Scanner
def start_scan():
    def scan():
        for t in ["Scanning emotions... 💭","Checking sweetness... 🍭","Almost done... 💖"]:
            progress_label.config(text=t)
            time.sleep(1)
        progress_label.config(text="Scan Complete ✅")
    threading.Thread(target=scan).start()

# Load question
def load_question():
    global q_index

    for w in button_frame.winfo_children():
        w.destroy()

    if q_index < len(questions):
        q = questions[q_index]
        question_label.config(text=q["question"])

        for opt in q["options"]:
            tk.Button(
                button_frame,
                text="💖 "+opt+" 💖",
                width=26,
                font=("Comic Sans MS", 12, "bold"),  # 🔥 Bigger buttons
                bg="#ff69b4",
                fg="white",
                bd=0,
                command=lambda o=opt: check_answer(o)
            ).pack(pady=6)
    else:
        show_gift_box()

# Check answer
def check_answer(selected):
    global q_index, score
    correct = questions[q_index]["correct"]

    if correct is None:
        score += 1
        title.config(text=f"💖✨ Tripti's Secret Unlock ✨💖\nScore: {score} 🎯")
        messagebox.showinfo("😂","Hahaha 😂")
        q_index+=1
        load_question()

    elif selected == correct:
        score += 2
        title.config(text=f"💖✨ Tripti's Secret Unlock ✨💖\nScore: {score} 🎯")
        messagebox.showinfo("💖","Correct 😎")
        q_index+=1
        load_question()
    else:
        show_access_denied()

# 🚫 Access denied
def show_access_denied():
    for w in root.winfo_children():
        w.destroy()

    f = tk.Frame(root,bg="red")
    f.pack(fill="both",expand=True)

    tk.Label(
        f,
        text="🚫 ACCESS DENIED 🚫",
        font=("Arial",22,"bold"),
        bg="red",
        fg="white"
    ).pack(expand=True)

    winsound.Beep(400,500)

    def back():
        time.sleep(2)
        rebuild_ui()

    threading.Thread(target=back).start()

def rebuild_ui():
    root.destroy()
    import os
    os.system("python " + __file__)

# 🎁 Gift box
def show_gift_box():
    for w in root.winfo_children():
        w.destroy()

    canvas = tk.Canvas(root,width=450,height=500,bg="#ffc0cb",highlightthickness=0)
    canvas.pack()

    lid = canvas.create_rectangle(140,170,310,220,fill="#ff1493")
    box = canvas.create_rectangle(150,220,300,350,fill="#ff69b4")

    canvas.create_text(
        225,120,
        text="🎁 Click to Open 🎁",
        font=("Arial",16,"bold")
    )

    def open_box(e):
        for _ in range(25):
            canvas.move(lid,0,-3)
            root.update()
            time.sleep(0.02)
        show_final_message(canvas)

    canvas.bind("<Button-1>", open_box)

# 🎈 Balloons
def balloons(canvas):
    balloon_items = []

    for _ in range(7):
        x = random.randint(50,400)
        y = random.randint(300,500)

        b = canvas.create_oval(x,y,x+30,y+40,fill=random.choice(
            ["red","blue","green","pink","purple"]),outline="")
        s = canvas.create_line(x+15,y+40,x+15,y+70)

        balloon_items.append((b,s,1))

    def float_up():
        while True:
            for b,s,val in balloon_items:
                canvas.move(b,0,-2)
                canvas.move(s,0,-2)

                if canvas.coords(b)[1] < 0:
                    nx = random.randint(50,400)
                    canvas.coords(b,nx,500,nx+30,540)
                    canvas.coords(s,nx+15,540,nx+15,570)
            time.sleep(0.05)

    canvas.bind("<Button-1>", lambda e: None)
    threading.Thread(target=float_up, daemon=True).start()

# 🎊 Final screen
def show_final_message(canvas):
    canvas.delete("all")

    balloons(canvas)

    canvas.create_text(
        225,180,
        text="🎉 Happy Birthday Tripti 🎂",
        font=("Georgia",18,"bold"),
        fill="#d63384"
    )

    canvas.create_text(
        225,240,
        text="🎀 Meri chotuu si sweet bhenaa\nEnjoy your day 🎉",
        font=("Arial",13),
        fill="#d63384"
    )

    btn = tk.Button(
        root,
        text="💌 Secret Message",
        bg="#ff69b4",
        fg="white",
        command=secret_popup
    )
    btn.place(x=150,y=420)

    play_music()

# 💌 Secret message
def secret_popup():
    messagebox.showinfo(
        "💖 Secret",
        "You are the best sister ever 💕\nStay happy always 😘"
    )

# 🎶 Music
def play_music():
    notes=[(264,300),(264,200),(297,500),(264,500)]
    for f,d in notes:
        winsound.Beep(f,d)

# Start
start_scan()
load_question()
root.mainloop()