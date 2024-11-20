import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.player = 'X'
        self.opponent = 'human'
        self.difficulty = 'beginner'
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_buttons()
        self.reset_button = tk.Button(self.root, text="Reset", command=self.reset_game)
        self.reset_button.grid(row=3, column=0, columnspan=3)
        self.create_options()

    def create_buttons(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.root, text="", font=('normal', 40), width=5, height=2,
                                               bg='lightblue', command=lambda i=i, j=j: self.on_button_click(i, j))
                self.buttons[i][j].grid(row=i, column=j)

    def create_options(self):
        self.opponent_var = tk.StringVar(value='human')
        self.difficulty_var = tk.StringVar(value='beginner')

        tk.Label(self.root, text="Opponent:").grid(row=4, column=0)
        tk.Radiobutton(self.root, text="Human", variable=self.opponent_var, value='human').grid(row=4, column=1)
        tk.Radiobutton(self.root, text="Computer", variable=self.opponent_var, value='computer').grid(row=4, column=2)

        tk.Label(self.root, text="Difficulty:").grid(row=5, column=0)
        tk.Radiobutton(self.root, text="Beginner", variable=self.difficulty_var, value='beginner').grid(row=5, column=1)
        tk.Radiobutton(self.root, text="Professional", variable=self.difficulty_var, value='professional').grid(row=5, column=2)
        tk.Radiobutton(self.root, text="Legendary", variable=self.difficulty_var, value='legendary').grid(row=5, column=3)

    def on_button_click(self, i, j):
        if self.buttons[i][j]['text'] == "" and self.check_winner() is False:
            self.buttons[i][j]['text'] = self.player
            self.buttons[i][j]['bg'] = 'lightgreen' if self.player == 'X' else 'lightcoral'
            if self.check_winner():
                messagebox.showinfo("Tic Tac Toe", f"Player {self.player} wins!")
            elif self.check_draw():
                messagebox.showinfo("Tic Tac Toe", "It's a draw!")
            else:
                self.player = 'O' if self.player == 'X' else 'X'
                if self.opponent_var.get() == 'computer' and self.player == 'O':
                    self.computer_move()

    def computer_move(self):
        if self.difficulty_var.get() == 'beginner':
            self.random_move()
        elif self.difficulty_var.get() == 'professional':
            self.block_or_random_move()
        elif self.difficulty_var.get() == 'legendary':
            self.minimax_move()

    def random_move(self):
        empty_cells = [(i, j) for i in range(3) for j in range(3) if self.buttons[i][j]['text'] == ""]
        if empty_cells:
            i, j = random.choice(empty_cells)
            self.on_button_click(i, j)

    def block_or_random_move(self):
        # Try to block the opponent's winning move
        for i in range(3):
            for j in range(3):
                if self.buttons[i][j]['text'] == "":
                    self.buttons[i][j]['text'] = 'X'
                    if self.check_winner():
                        self.buttons[i][j]['text'] = 'O'
                        self.buttons[i][j]['bg'] = 'lightcoral'
                        return
                    self.buttons[i][j]['text'] = ""
        self.random_move()

    def minimax_move(self):
        best_score = -float('inf')
        best_move = None
        for i in range(3):
            for j in range(3):
                if self.buttons[i][j]['text'] == "":
                    self.buttons[i][j]['text'] = 'O'
                    score = self.minimax(False)
                    self.buttons[i][j]['text'] = ""
                    if score > best_score:
                        best_score = score
                        best_move = (i, j)
        if best_move:
            self.on_button_click(best_move[0], best_move[1])

    def minimax(self, is_maximizing):
        if self.check_winner():
            return 1 if not is_maximizing else -1
        if self.check_draw():
            return 0

        if is_maximizing:
            best_score = -float('inf')
            for i in range(3):
                for j in range(3):
                    if self.buttons[i][j]['text'] == "":
                        self.buttons[i][j]['text'] = 'O'
                        score = self.minimax(False)
                        self.buttons[i][j]['text'] = ""
                        best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for i in range(3):
                for j in range(3):
                    if self.buttons[i][j]['text'] == "":
                        self.buttons[i][j]['text'] = 'X'
                        score = self.minimax(True)
                        self.buttons[i][j]['text'] = ""
                        best_score = min(score, best_score)
            return best_score

    def check_winner(self):
        for i in range(3):
            if self.buttons[i][0]['text'] == self.buttons[i][1]['text'] == self.buttons[i][2]['text'] != "":
                return True
            if self.buttons[0][i]['text'] == self.buttons[1][i]['text'] == self.buttons[2][i]['text'] != "":
                return True
        if self.buttons[0][0]['text'] == self.buttons[1][1]['text'] == self.buttons[2][2]['text'] != "":
            return True
        if self.buttons[0][2]['text'] == self.buttons[1][1]['text'] == self.buttons[2][0]['text'] != "":
            return True
        return False

    def check_draw(self):
        for row in self.buttons:
            for button in row:
                if button['text'] == "":
                    return False
        return True

    def reset_game(self):
        self.player = 'X'
        for row in self.buttons:
            for button in row:
                button['text'] = ""
                button['bg'] = 'lightblue'

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
