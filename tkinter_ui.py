import tkinter as tk
from tkinter import messagebox
from game_logic import Board

class QuadGridUI:
    def __init__(self, root):
        self.root = root
        self.root.title("QuadGrid Showdown")
        self.root.geometry("420x550")
        self.root.resizable(False, False)
        self.board = Board()
        self.buttons = []
        self.create_widgets()

    def create_widgets(self):
        self.frame = tk.Frame(self.root, padx=10, pady=10, bg="#ecf7f9")
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.status = tk.Label(self.frame, text=f"Current Player: {self.board.get_current_player()}",
                               font=('Arial', 14, 'bold'), bg="#ecf7f9", fg="#0c3f69")
        self.status.pack(pady=(0, 8))

        self.prob_label = tk.Label(self.frame, text="Win Probabilities: X: 50.0% | O: 50.0%",
                                   font=('Arial', 12), bg="#ecf7f9", fg="#0c3f69")
        self.prob_label.pack(pady=(0, 8))

        grid_frame = tk.Frame(self.frame, bg="#f4f7fb")
        grid_frame.pack(padx=8, pady=8)

        for row in range(4):
            button_row = []
            for col in range(4):
                btn = tk.Button(grid_frame, text='', font=('Arial', 22, 'bold'), width=4, height=2,
                                bd=2, relief=tk.RIDGE, bg='#eaf2ff', fg='#0b3f72', activebackground='#a0d9ff',
                                highlightthickness=1, highlightbackground='#1c6cb3',
                                command=lambda r=row, c=col: self.on_click(r, c))
                btn.grid(row=row, column=col, padx=2, pady=2, ipadx=4, ipady=4)
                button_row.append(btn)
            self.buttons.append(button_row)

        controls = tk.Frame(self.frame, bg="#f4f7fb")
        controls.pack(pady=(10, 0))

        reset_btn = tk.Button(controls, text='Reset', font=('Arial', 12), command=self.reset_game, width=10)
        reset_btn.pack(side=tk.LEFT, padx=6)

        quit_btn = tk.Button(controls, text='Quit', font=('Arial', 12), command=self.root.destroy, width=10)
        quit_btn.pack(side=tk.LEFT, padx=6)

    def on_click(self, row, col):
        if not self.board.make_move(row, col):
            messagebox.showwarning("Invalid Move", "This cell is already occupied.")
            return

        self.buttons[row][col].config(text=self.board.get_board()[row][col])
        winner = self.board.check_win()
        if winner:
            self.status.config(text=f"Winner: {winner}")
            messagebox.showinfo("Game Over", f"Player {winner} wins!")
            self.disable_buttons()
            return

        if self.board.check_draw():
            self.status.config(text="It's a draw!")
            messagebox.showinfo("Game Over", "It's a draw!")
            self.disable_buttons()
            return

        self.status.config(text=f"Current Player: {self.board.get_current_player()}")

        # Update win probabilities
        probs = self.board.get_win_probabilities()
        self.prob_label.config(text=f"Win Probabilities: X: {probs['X']}% | O: {probs['O']}%")

    def disable_buttons(self):
        for row in self.buttons:
            for btn in row:
                btn.config(state=tk.DISABLED)

    def reset_game(self):
        self.board.reset()
        for row in self.buttons:
            for btn in row:
                btn.config(text='', state=tk.NORMAL)
        self.status.config(text=f"Current Player: {self.board.get_current_player()}")
        probs = self.board.get_win_probabilities()
        self.prob_label.config(text=f"Win Probabilities: X: {probs['X']}% | O: {probs['O']}%")

if __name__ == "__main__":
    root = tk.Tk()
    app = QuadGridUI(root)
    root.mainloop()