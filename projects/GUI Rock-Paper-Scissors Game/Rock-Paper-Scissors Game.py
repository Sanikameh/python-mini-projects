import tkinter as tk
from random import choice

# -------------------------
# Main Window
# -------------------------
root = tk.Tk()
root.title("Rock-Paper-Scissors")
root.geometry("450x500")
root.config(bg="#1e3a8a")  # Blue background

# -------------------------
# Variables
# -------------------------
choices = ["Rock ✊", "Paper ✋", "Scissors ✌️"]
player_score = 0
computer_score = 0
ties = 0

# -------------------------
# Functions
# -------------------------
def play(player_choice):
    global player_score, computer_score, ties

    computer_choice = choice(choices)
    result = ""

    if player_choice == computer_choice:
        result = f"🤝 Tie! Both chose {player_choice}"
        ties += 1
    elif (player_choice.startswith("Rock") and computer_choice.startswith("Scissors")) or \
         (player_choice.startswith("Paper") and computer_choice.startswith("Rock")) or \
         (player_choice.startswith("Scissors") and computer_choice.startswith("Paper")):
        result = f"🎉 You Win! {player_choice} beats {computer_choice}"
        player_score += 1
    else:
        result = f"😢 You Lose! {computer_choice} beats {player_choice}"
        computer_score += 1

    result_label.config(text=result)
    score_label.config(text=f"Player: {player_score} | Computer: {computer_score} | Ties: {ties}")

def reset_game():
    global player_score, computer_score, ties
    player_score = computer_score = ties = 0
    result_label.config(text="Make your move!")
    score_label.config(text="Player: 0 | Computer: 0 | Ties: 0")

# -------------------------
# UI Elements
# -------------------------
title_label = tk.Label(root, text="Rock - Paper - Scissors", font=("Helvetica", 20, "bold"),
                       fg="#FFD60A", bg="#1e3a8a")  # Yellow text
title_label.pack(pady=20)

# Result label
result_label = tk.Label(root, text="Make your move!", font=("Helvetica", 16),
                        fg="#FFD60A", bg="#1e3a8a")
result_label.pack(pady=10)

# Score label
score_label = tk.Label(root, text="Player: 0 | Computer: 0 | Ties: 0", font=("Helvetica", 14),
                       fg="#FFD60A", bg="#1e3a8a")
score_label.pack(pady=10)

# Buttons
button_frame = tk.Frame(root, bg="#1e3a8a")
button_frame.pack(pady=30)

rock_btn = tk.Button(button_frame, text="Rock ✊", width=10, font=("Helvetica", 14, "bold"),
                     bg="#FFD60A", fg="#1e3a8a", activebackground="#FFF176",
                     command=lambda: play("Rock ✊"))
rock_btn.grid(row=0, column=0, padx=10, pady=10)

paper_btn = tk.Button(button_frame, text="Paper ✋", width=10, font=("Helvetica", 14, "bold"),
                      bg="#FFD60A", fg="#1e3a8a", activebackground="#FFF176",
                      command=lambda: play("Paper ✋"))
paper_btn.grid(row=0, column=1, padx=10, pady=10)

scissors_btn = tk.Button(button_frame, text="Scissors ✌️", width=10, font=("Helvetica", 14, "bold"),
                         bg="#FFD60A", fg="#1e3a8a", activebackground="#FFF176",
                         command=lambda: play("Scissors ✌️"))
scissors_btn.grid(row=0, column=2, padx=10, pady=10)

# Reset button
reset_btn = tk.Button(root, text="Reset Score", font=("Helvetica", 14, "bold"),
                      bg="#FFD60A", fg="#1e3a8a", width=20, activebackground="#FFF176",
                      command=reset_game)
reset_btn.pack(pady=20)

root.mainloop()
