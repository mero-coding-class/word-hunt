import tkinter as tk
import random
import string

# ------------------ GAME SETUP ------------------
words = ["apple", "ball", "cat", "dog", "elephant"]

def start_new_game():
    global secret_word, guessed_letters, chances

    secret_word = random.choice(words)
    guessed_letters = []
    chances = 6

    chances_label.config(text="❤️ Chances left: 6")
    result_label.config(text="")
    guessed_label.config(text="Guessed Letters: ")

    for btn in buttons:
        btn.config(state="normal", bg="#FFD966")

    update_word()

# ------------------ GAME LOGIC ------------------
def update_word():
    display = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display += letter.upper() + " "
        else:
            display += "_ "
    word_label.config(text=display)

def guess_letter(letter, button):
    global chances

    if letter not in guessed_letters:
        guessed_letters.append(letter)
        guessed_label.config(
            text="Guessed Letters: " + " ".join(l.upper() for l in guessed_letters)
        )

        if letter not in secret_word:
            chances -= 1
            chances_label.config(text=f"❤️ Chances left: {chances}")
            button.config(bg="#FF6F61")  # red for wrong
        else:
            button.config(bg="#6BCF63")  # green for correct

        button.config(state="disabled")
        update_word()
        check_game()

def check_game():
    if chances == 0:
        result_label.config(
            text=f"❌ You Lost! Word was: {secret_word.upper()}",
            fg="red"
        )
        disable_buttons()

    if all(letter in guessed_letters for letter in secret_word):
        result_label.config(text="🎉 You Won!", fg="green")
        disable_buttons()

def disable_buttons():
    for btn in buttons:
        btn.config(state="disabled")

# ------------------ UI SETUP ------------------
window = tk.Tk()
window.title("🎯 Word Puzzle Game")
window.geometry("520x520")
window.config(bg="#E3F2FD")

title = tk.Label(
    window, text="WORD PUZZLE GAME 🎯",
    font=("Comic Sans MS", 20, "bold"),
    bg="#E3F2FD", fg="#0D47A1"
)
title.pack(pady=10)

word_label = tk.Label(
    window, text="", font=("Arial", 26, "bold"),
    bg="#E3F2FD", fg="#1B5E20"
)
word_label.pack(pady=15)

chances_label = tk.Label(
    window, text="❤️ Chances left: 6",
    font=("Arial", 14),
    bg="#E3F2FD"
)
chances_label.pack()

guessed_label = tk.Label(
    window, text="Guessed Letters: ",
    font=("Arial", 12),
    bg="#E3F2FD"
)
guessed_label.pack(pady=5)

result_label = tk.Label(
    window, text="", font=("Arial", 16, "bold"),
    bg="#E3F2FD"
)
result_label.pack(pady=10)

# ------------------ LETTER BUTTONS ------------------
button_frame = tk.Frame(window, bg="#E3F2FD")
button_frame.pack(pady=10)

buttons = []

for i, letter in enumerate(string.ascii_lowercase):
    btn = tk.Button(
        button_frame,
        text=letter.upper(),
        width=4,
        height=2,
        font=("Arial", 10, "bold"),
        bg="#FFD966",
        command=lambda l=letter, b=None: None
    )
    btn.config(command=lambda l=letter, b=btn: guess_letter(l, b))
    btn.grid(row=i // 7, column=i % 7, padx=3, pady=3)
    buttons.append(btn)

# ------------------ RESTART BUTTON ------------------
restart_btn = tk.Button(
    window,
    text="🔄 Restart Game",
    font=("Arial", 12, "bold"),
    bg="#4CAF50",
    fg="white",
    command=start_new_game
)
restart_btn.pack(pady=15)

# Start first game
start_new_game()

window.mainloop()
