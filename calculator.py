import tkinter as tk
import math

def on_click(event):
    text = event.widget["text"]
    if text == "=":
        try:
            expression = entry.get().replace("^", "**")
            result = eval(expression)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    elif text in ["sin", "cos", "tan", "log", "√"]:
        try:
            val = float(entry.get())
            if text == "sin":
                result = math.sin(math.radians(val))
            elif text == "cos":
                result = math.cos(math.radians(val))
            elif text == "tan":
                result = math.tan(math.radians(val))
            elif text == "log":
                result = math.log10(val)
            elif text == "√":
                result = math.sqrt(val)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    else:
        entry.insert(tk.END, text)

# 🪟 Create main window
root = tk.Tk()
root.title("Scientific Calculator")
root.configure(bg="#1e1e1e")

# ✏️ Entry for display
entry = tk.Entry(root, font="Arial 20", bd=8, bg="#333", fg="#fff", justify="right", insertbackground="white")
entry.grid(row=0, column=0, columnspan=5, pady=10, padx=10, sticky="we")

# 🔘 Button labels
buttons = [
    ["7", "8", "9", "/", "C"],
    ["4", "5", "6", "*", "√"],
    ["1", "2", "3", "-", "^"],
    ["0", ".", "=", "+", "log"],
    ["sin", "cos", "tan"]
]

# 🎨 Button creation loop
for i, row in enumerate(buttons):
    for j, text in enumerate(row):
        button = tk.Button(root, text=text, font="Arial 14", width=6, height=2, bg="#444", fg="white", bd=1, relief=tk.FLAT)
        button.grid(row=i+1, column=j, padx=3, pady=3)
        button.bind("<Button-1>", on_click)

# ⏳ Run the application
root.mainloop()