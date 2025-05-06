

import tkinter as tk

def calculate():
    try:
        result = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Main window setup
window = tk.Tk()
window.title("Simple Calculator")
window.geometry("500x550")
window.config(bg="light blue")
window.resizable(False, False)

entry = tk.Entry(window, width=20, font=("Arial", 24), justify='left', bd=5,relief="sunken")
entry.grid(row=0, column=0, columnspan=4,padx=10,pady=10)
button_style = {"width": 8, "height": 2, "font": ("Arial", 14), "bg": "light grey", "fg": "black", "relief": "raised", "bd": 10}
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ('C', 5, 0, 4)
]

for (text, row, col, *colspan) in buttons:
    action = lambda x=text: entry.insert(tk.END, x) if x != "=" and x != "C" else (calculate() if x == "=" else entry.delete(0, tk.END))
    tk.Button(window, text=text,  command=action,**button_style).grid(row=row, column=col, columnspan=colspan[0] if colspan else 1,padx=5,pady=5)

window.mainloop()

