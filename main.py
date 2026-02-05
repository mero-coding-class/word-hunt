import tkinter as tk
import random

# List of words
words = ["apple", "ball", "cat", "dog", "elephant"]

# Choose a random word
secret_word = random.choice(words)

guessed_letters = []
chances = 6

# Function to update displayed word
def update_word():
    display = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    word_label.config(text=display)

# Function when a letter button is clicked
def guess_letter(letter):
    global chances

    if letter not in guessed_letters:
        guessed_letters.append(letter)

        if letter not in secret_word:
            chances -= 1
            chances_label.config(text="Chances left: " + str(chances))

        update_word()
        check_game()

# Function to check win or lose
def check_game():
    if chances == 0:
        result_label.config(text="❌ You Lost! Word was: " + secret_word)
        disable_buttons()

    win = True
    for letter in secret_word:
        if letter not in guessed_letters:
            win = False

    if win:
        result_label.config(text="🎉 You Won!")
        disable_buttons()

# Disable all buttons after game ends
def disable_buttons():
    for btn in buttons:
        btn.config(state="disabled")

# Create main window
window = tk.Tk()
window.title("Hangman Game")
window.geometry("400x400")

# Labels
word_label = tk.Label(window, text="", font=("Arial", 20))
word_label.pack(pady=20)

chances_label = tk.Label(window, text="Chances left: 6", font=("Arial", 12))
chances_label.pack()

result_label = tk.Label(window, text="", font=("Arial", 14))
result_label.pack(pady=10)

# Frame for letter buttons
button_frame = tk.Frame(window)
button_frame.pack()

buttons = []

# Create A-Z buttons
for i in range(26):
    letter = chr(97 + i)  # a to z
    btn = tk.Button(button_frame, text=letter, width=4,
                    command=lambda l=letter: guess_letter(l))
    btn.grid(row=i//7, column=i%7)
    buttons.append(btn)

# Start game
update_word()

# Run window
window.mainloop()
