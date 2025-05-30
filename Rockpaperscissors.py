import tkinter as tk
import random

# Set up the main window
window = tk.Tk()
window.title("Rock Paper Scissors")
window.geometry("400x400")
window.config(bg="#F0F8FF")

# Score variables
user_score = 0
computer_score = 0

# Possible moves
moves = ["rock", "paper", "scissors"]

# Functions
def play(user_move):
    global user_score, computer_score

    computer_move = random.choice(moves)
    result = ""

    if user_move == computer_move:
        result = "It's a tie!"
    elif (user_move == "rock" and computer_move == "scissors") or \
         (user_move == "paper" and computer_move == "rock") or \
         (user_move == "scissors" and computer_move == "paper"):
        user_score += 1
        result = "You win!"
    else:
        computer_score += 1
        result = "Computer wins!"

    result_label.config(text=f"Computer chose: {computer_move}\n{result}")
    score_label.config(text=f"You: {user_score} | Computer: {computer_score}")

# UI Elements
title_label = tk.Label(window, text="Rock Paper Scissors", font=("Arial", 20, "bold"), bg="#F0F8FF")
title_label.pack(pady=20)

button_frame = tk.Frame(window, bg="#F0F8FF")
button_frame.pack()

rock_btn = tk.Button(button_frame, text="Rock", width=12, height=2, command=lambda: play("rock"))
rock_btn.grid(row=0, column=0, padx=10)

paper_btn = tk.Button(button_frame, text="Paper", width=12, height=2, command=lambda: play("paper"))
paper_btn.grid(row=0, column=1, padx=10)

scissors_btn = tk.Button(button_frame, text="Scissors", width=12, height=2, command=lambda: play("scissors"))
scissors_btn.grid(row=0, column=2, padx=10)

result_label = tk.Label(window, text="", font=("Arial", 14), bg="#F0F8FF")
result_label.pack(pady=20)

score_label = tk.Label(window, text="You: 0 | Computer: 0", font=("Arial", 14), bg="#F0F8FF")
score_label.pack()

# Run the app
window.mainloop()
