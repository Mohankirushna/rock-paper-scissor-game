"""ROCK PAPER SCISSOR"""

import tkinter as tk
from tkinter import Button, Label, messagebox
import random

class RockPaperScissorsGame:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Rock, Paper, Scissors Game")

        self.player_wins = 0
        self.computer_wins = 0

        self.label_score = Label(self.window, text="Player: 0 | Computer: 0 | Player Wins: 0")
        self.label_score.pack(pady=10)
        self.label_score.config(foreground="blue", background="yellow")

        self.button_rock = Button(self.window, text="Rock", command=lambda: self.on_button_click("Rock"))
        self.button_rock.pack(side=tk.LEFT, padx=10)

        self.button_paper = Button(self.window, text="Paper", command=lambda: self.on_button_click("Paper"))
        self.button_paper.pack(side=tk.LEFT, padx=10)

        self.button_scissors = Button(self.window, text="Scissors", command=lambda: self.on_button_click("Scissors"))
        self.button_scissors.pack(side=tk.LEFT, padx=10)

    def determine_winner(self, player_choice):
        choices = ["Rock", "Paper", "Scissors"]
        computer_choice = random.choice(choices)

        result = f"Computer chose {computer_choice}.\n"

        if player_choice == computer_choice:
            result += "It's a tie!"
        elif (
            (player_choice == "Rock" and computer_choice == "Scissors") or
            (player_choice == "Paper" and computer_choice == "Rock") or
            (player_choice == "Scissors" and computer_choice == "Paper")
        ):
            result += "You win!"
            self.player_wins += 1
        else:
            result += "Computer wins!"
            self.computer_wins += 1

        self.label_score.config(text=f"Player: {self.player_wins} | Computer: {self.computer_wins} | Player Wins: {self.player_wins}")

        messagebox.showinfo("Result", result)

    def on_button_click(self, choice):
        self.determine_winner(choice)

if __name__ == "__main__":
    game = RockPaperScissorsGame()
    game.window.mainloop()

