import tkinter as tk
from tkinter import simpledialog, messagebox
import random

class DiceGame:
    def __init__(self, root):
        self.root = root
        # self.root.title("Dice Roll Game")

        self.max_score = 50
        self.players = self.get_player_count()
        self.player_scores = [0] * self.players
        self.current_player = 0

        self.create_widgets()
        self.update_status()

    def get_player_count(self):
        while True:
            try:
                count = simpledialog.askinteger("Players", "Enter number of players (2-4):")
                if count and 2 <= count <= 4:
                    return count
                else:
                    messagebox.showerror("Error", "Please enter a number between 2 and 4.")
            except:
                continue

    def create_widgets(self):
        self.status_label = tk.Label(self.root, text="", font=("Arial", 14))
        self.status_label.pack(pady=10)

        self.roll_button = tk.Button(self.root, text="Roll Dice", font=("Arial", 12), command=self.roll_dice)
        self.roll_button.pack(pady=10)

        self.result_label = tk.Label(self.root, text="", font=("Arial", 18))
        self.result_label.pack(pady=10)

        self.score_labels = []
        for i in range(self.players):
            lbl = tk.Label(self.root, text=f"Player {i+1}: 0", font=("Arial", 12))
            lbl.pack()
            self.score_labels.append(lbl)

    def roll_dice(self):
        value = random.randint(1, 6)
        self.result_label.config(text=f"Player {self.current_player+1} rolled a {value}")

        if value == 1:
            self.result_label.config(text=f"Player {self.current_player+1} rolled a 1! Turn over!")
            self.next_player()
        else:
            self.player_scores[self.current_player] += value
            self.score_labels[self.current_player].config(text=f"Player {self.current_player+1}: {self.player_scores[self.current_player]}")

            if self.player_scores[self.current_player] >= self.max_score:
                messagebox.showinfo("Game Over", f"Player {self.current_player+1} wins!")
                self.root.quit()
                return

        self.update_status()

    def next_player(self):
        self.current_player = (self.current_player + 1) % self.players

    def update_status(self):
        self.status_label.config(text=f"Player {self.current_player+1}'s turn")

if __name__ == "__main__":
    root = tk.Tk()
    game = DiceGame(root)
    root.mainloop()
