import tkinter as tk
from tkinter import simpledialog
import threading
import time

class CountdownTimer:
    def __init__(self, root):
        self.root = root
        self.root.title("Linux Countdown Timer")
        self.root.geometry("300x200")
        self.root.resizable(False, False)

        self.timer_text = tk.StringVar(value="00:00")
        self.timer_label = tk.Label(root, textvariable=self.timer_text, font=("Helvetica", 36))
        self.timer_label.pack(pady=20)

        button_frame = tk.Frame(root)
        button_frame.pack(pady=10)

        self.set_button = tk.Button(button_frame, text="Set Timer", width=10, command=self.set_timer)
        self.set_button.grid(row=0, column=0, padx=5)

        self.start_button = tk.Button(button_frame, text="Start", width=10, command=self.start_timer)
        self.start_button.grid(row=0, column=1, padx=5)

        self.reset_button = tk.Button(button_frame, text="Reset", width=10, command=self.reset_timer)
        self.reset_button.grid(row=1, column=0, columnspan=2, pady=10)

        self.count = [0]
        self.running = False

    def set_timer(self):
        try:
            minutes = simpledialog.askinteger("Set Minutes", "Enter minutes:", minvalue=0)
            seconds = simpledialog.askinteger("Set Seconds", "Enter seconds:", minvalue=0, maxvalue=59)
            self.count[0] = minutes * 60 + seconds
            self.update_timer_display()
        except:
            pass

    def update_timer_display(self):
        mins, secs = divmod(self.count[0], 60)
        self.timer_text.set(f"{mins:02d}:{secs:02d}")

    def start_timer(self):
        if self.count[0] > 0 and not self.running:
            self.running = True
            threading.Thread(target=self.countdown).start()

    def countdown(self):
        while self.count[0] > 0 and self.running:
            self.update_timer_display()
            time.sleep(1)
            self.count[0] -= 1

        if self.count[0] == 0:
            self.timer_text.set("⏰ Time's Up!")
            self.running = False

    def reset_timer(self):
        self.running = False
        self.count[0] = 0
        self.timer_text.set("00:00")

if __name__ == "__main__":
    root = tk.Tk()
    app = CountdownTimer(root)
    root.mainloop()

