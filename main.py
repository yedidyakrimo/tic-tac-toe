import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.window.geometry("400x400")
        self.window.resizable(False, False)

        self.board = [[None for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.vs_computer = True

        self.setup_menu()

    def setup_menu(self):
        self.menu_frame = tk.Frame(self.window, bg='lightyellow')
        self.menu_frame.pack(fill='both', expand=True)

        tk.Label(self.menu_frame, text="Tic Tac Toe", font=('Arial', 24, 'bold'), bg='lightyellow', fg='blue').pack(pady=10)
        tk.Label(self.menu_frame, text="Choose Game Mode", font=('Arial', 16), bg='lightyellow', fg='black').pack(pady=10)

        tk.Button(self.menu_frame, text="Player vs Computer", font=('Arial', 14), command=self.start_vs_computer, bg='lightblue').pack(pady=5)
        tk.Button(self.menu_frame, text="Player vs Player", font=('Arial', 14), command=self.start_vs_player, bg='lightgreen').pack(pady=5)

        canvas = tk.Canvas(self.menu_frame, width=200, height=200, bg='lightyellow', highlightthickness=0)
        canvas.pack(pady=10)
        canvas.create_line(50, 0, 50, 150, width=5, fill='black')
        canvas.create_line(100, 0, 100, 150, width=5, fill='black')
        canvas.create_line(0, 50, 150, 50, width=5, fill='black')
        canvas.create_line(0, 100, 150, 100, width=5, fill='black')
        canvas.create_oval(10, 10, 40, 40, outline='red', width=3)
        canvas.create_line(60, 10, 90, 40, fill='blue', width=3)
        canvas.create_line(60, 40, 90, 10, fill='blue')

    def start_vs_computer(self):
        self.vs_computer = True
        self.menu_frame.destroy()
        self.create_widgets()

    def start_vs_player(self):
        self.vs_computer = False
        self.menu_frame.destroy()
        self.create_widgets()

    def create_widgets(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.window, text='', font=('Arial', 24), height=2, width=5,
                                               bg='lightblue', command=lambda row=i, col=j: self.on_click(row, col))
                self.buttons[i][j].grid(row=i, column=j)

    def on_click(self, row, col):
        if self.buttons[row][col]['text'] == '' and not self.check_winner():
            self.buttons[row][col]['text'] = self.current_player
            self.board[row][col] = self.current_player

            if self.check_winner():
                self.animate_winner()
                messagebox.showinfo("Game Over", f"{self.current_player} wins!")
                self.reset_game()
            elif self.is_full():
                messagebox.showinfo("Game Over", "It's a tie!")
                self.reset_game()
            else:
                if self.vs_computer:
                    self.switch_player()
                    self.computer_move()
                else:
                    self.switch_player()

    def computer_move(self):
        if not self.check_winner() and not self.is_full():
            best_score = -float('inf')
            best_move = None

            for i in range(3):
                for j in range(3):
                    if self.board[i][j] is None:
                        self.board[i][j] = 'O'
                        score = self.minimax(self.board, 0, False)
                        self.board[i][j] = None
                        if score > best_score:
                            best_score = score
                            best_move = (i, j)

            if best_move:
                row, col = best_move
                self.buttons[row][col]['text'] = 'O'
                self.board[row][col] = 'O'

                if self.check_winner():
                    self.animate_winner()
                    messagebox.showinfo("Game Over", "Computer wins!")
                    self.reset_game()
                elif self.is_full():
                    messagebox.showinfo("Game Over", "It's a tie!")
                    self.reset_game()
                else:
                    self.switch_player()

    def minimax(self, board, depth, is_maximizing):
        winner = self.get_winner()
        if winner == 'O':
            return 10 - depth
        elif winner == 'X':
            return depth - 10
        elif self.is_full():
            return 0

        if is_maximizing:
            best_score = -float('inf')
            for i in range(3):
                for j in range(3):
                    if board[i][j] is None:
                        board[i][j] = 'O'
                        score = self.minimax(board, depth + 1, False)
                        board[i][j] = None
                        best_score = max(best_score, score)
            return best_score
        else:
            best_score = float('inf')
            for i in range(3):
                for j in range(3):
                    if board[i][j] is None:
                        board[i][j] = 'X'
                        score = self.minimax(board, depth + 1, True)
                        board[i][j] = None
                        best_score = min(best_score, score)
            return best_score

    def is_full(self):
        return all(self.board[i][j] is not None for i in range(3) for j in range(3))

    def check_winner(self):
        # Check rows and columns
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] and self.board[i][0] is not None:
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] and self.board[0][i] is not None:
                return True

        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] is not None:
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] is not None:
            return True

        return False

    def get_winner(self):
        # Check rows and columns
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] and self.board[i][0] is not None:
                return self.board[i][0]
            if self.board[0][i] == self.board[1][i] == self.board[2][i] and self.board[0][i] is not None:
                return self.board[0][i]

        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] is not None:
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] is not None:
            return self.board[0][2]

        return None

    def animate_winner(self):
        for i in range(3):
            for j in range(3):
                if self.buttons[i][j]['text'] == self.current_player:
                    self.buttons[i][j].config(bg='lightgreen')

    def reset_game(self):
        self.board = [[None for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text='', bg='lightblue')
        self.current_player = 'X'

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = TicTacToe()
    game.run()
