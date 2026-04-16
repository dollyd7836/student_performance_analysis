import tkinter as tk
from tkinter import messagebox 
import matplotlib.pyplot as plt
root = tk.Tk()
root.title("self budget manager")
root.geometry("400x500")
root.config(bg = "#f107f1",highlightthickness=6,highlightbackground="#ff69b4",highlightcolor="#ff69b4") 

#Title Label
title_label = tk.Label(
    root,
    text="💰 Self budget manager ",
    font=("Georgia", 18, "bold"),
    bg="#5C0952",
    fg="#f1c40f")
title_label.pack(pady=15)

category_label = tk.Label(root, text = "Select category", font = ("Verdana", 11), bg="#f107f1", fg= "White")
category_label.pack(pady=(10 ,2))

category_var = tk.StringVar()
category_var.set("Food")# default value

category_menu = tk.OptionMenu(
    root,
    category_var,
    "Food",
    "Transport",
    "Shopping",
    "Bills",
    "Others"
)
category_menu.config(
   font = ("Verdana", 10),
   bg = "#ff69b4",
   fg = "White",
   width = 15
)

category_menu.pack(pady=5)


#Entry field
expense_entry = tk.Entry(
    root,
    font=("Verdana", 13),
    bd=3,
    relief="ridge",
    bg="#fff0f5",
    fg="#2c3e50",
    insertbackground="#2c3e50"
)
expense_entry.pack(pady=5)


#function to handle button click
total = 0 # create total variable first
expenses = []
monthly_limit = 2000 
def add_expense():
    global total, expenses

    try:
       amount = float(expense_entry.get().strip())
       category = category_var.get()
       
       if amount <= 0:
         
         expense_text.delete("1.0", tk.END)
         expense_text.insert(tk.END, "Please enter a Valid amount greater than 0")
         return
       else:
            
            expenses.append((category, amount))
            total += amount
            if total > monthly_limit:
             messagebox.showwarning(
                  "Budget Alert",
                  "⚠️ You have exceeded your monthly budget limit!"
    )
             
       #build display text
            display_text = ""

            for cat, amt in expenses:
                display_text += f"{cat:<12} ₹{amt:.2f}\n"
            display_text +="--------------------\n"
            display_text += f"{'Total': <12} ₹{total:.2f}"

            # Category summary
            category_total = {}

            for cat, amt in expenses:
                category_total[cat] = category_total.get(cat, 0) + amt

            display_text += "\n\nCategory Summary:\n"

            for cat, amt in category_total.items():
                display_text += f"{cat}: ₹{amt:.2f}\n"


       expense_text.delete("1.0", tk.END)
       expense_text.insert(tk.END, display_text)
       expense_entry.delete(0,tk.END)
            
       # ADD THIS FOR BUTTON FLASH
       add_button.config(bg="#ff1493")
       add_button.after(150, lambda:add_button.config(bg="#ff69b4"))
       
    except ValueError:
        messagebox.showerror("Error", text="please enter a valid number")
def show_pie_chart():   # ✅ HERE
    if not expenses:
        messagebox.showinfo("No Data", "No expenses to display!")
        return

    category_total = {}

    for cat, amt in expenses:
        category_total[cat] = category_total.get(cat, 0) + amt

    labels = list(category_total.keys())
    values = list(category_total.values())

    plt.figure(figsize=(7,7), facecolor="#fff0f5")

    colors = ["#ff69b4","#ff1493","#ff85c1","#c02ba7","#ffb6c1"]

    plt.pie(values, labels=labels, autopct="%1.1f%%",
            startangle=140, colors=colors, shadow=True)

    plt.title("Student Expense Distribution", fontsize=14, fontweight="bold")
    plt.axis("equal")
    plt.show()
    
def reset_total():
   
   global total
   confirm = messagebox.askyesno("Confirm reset",
                                 "Are you sure you want to reset everything?")
   if confirm:
      total = 0
      expenses.clear() 
      expense_text.delete("1.0", tk.END)
      expense_text.insert(tk.END, "Total ₹ 0.00")

#Button 
add_button = tk.Button(
    root,
    text="➕ Add Expense",
    command=add_expense,
    font=("Verdana", 11, "bold"),
    bg="#ff69b4",
    fg="white",
    activebackground="#ff85c1",
    width=18,
    bd=0
)
add_button.pack(pady=5)  

reset_button = tk.Button(
    root,
    text="🔄 Reset",
    command=reset_total,
    font=("Verdana", 11, "bold"),
    bg="#c02ba7",
    fg="white",
    activebackground="#e73cc2",
    width=18,
    bd=0
)
reset_button.pack(pady=5)
chart_button = tk.Button(
    root,
    text="📊 Show Expense Chart",
    command=show_pie_chart,
    font=("Verdana", 11, "bold"),
    bg="#8e44ad",
    fg="white",
    activebackground="#a569bd",
    width=18,
    bd=0
)
chart_button.pack(pady=5)
# Expense display box
text_frame = tk.Frame(root)
text_frame.pack(pady=10)
expense_text = tk.Text(
    text_frame,
    height=12,
    width=40,
    font=("Courier New", 11),
    bg="#fff0f5",
    fg="#2c3e50",
    bd=3,
    relief="ridge"
)
expense_text.pack(side=tk.LEFT)

scrollbar = tk.Scrollbar(text_frame, command=expense_text.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

expense_text.config(yscrollcommand=scrollbar.set)
root.mainloop()