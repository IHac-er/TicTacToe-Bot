import tkinter as tk 

from TicTacToe import TicTacToe, OccupiedPosition
from bot import TicTacToeBot

class TicTacToeGUI: 
    def __init__(self):
        self.root = tk.Tk() 
        self.root.title("Tic-Tac-Toe")
        self.root.resizable(False, False)

        self.game = TicTacToe() 
        self.bot = TicTacToeBot("O", "X")

        self.board_frame = tk.Frame(self.root)
        self.board_frame.pack(padx=10, pady=10)

        self.status_label = tk.Label(self.root, text="")
        self.status_label.pack()

        self.create_board()

    def handle_cell_click(self, position):
        try: 
            self.game.play_move(position, 'X')
        except OccupiedPosition:
            return 
        
        self.buttons[position].config(text='X')

        if self.game.game_over()[1]:
            winner = self.game.game_over()[0]

            if winner == "-":
                self.status_label.config(text="Draw!")
            else: 
                self.status_label.config(text=f"{winner} Wins!")

            return

        self.bot.update_board(self.game.get_board())

        bot_position = self.bot.best_move()

        self.game.play_move(bot_position, 'O')
        self.buttons[bot_position].config(text='O')

        self.bot.update_board(self.game.get_board())

        if self.game.game_over()[1]:
            winner = self.game.game_over()[0]
        
            if winner == "-":
                self.status_label.config(text="Draw!")
            else: 
                self.status_label.config(text=f"{winner} Wins!")
        
            return

    def create_board(self):
        self.buttons = [] 

        for position in range(9):
            row = position // 3 
            column = position % 3 

            button = tk.Button(
                self.board_frame,
                text=" ",
                width=10,
                height=4,
                command=lambda position=position: self.handle_cell_click(position)
            )
            button.grid(row=row, column=column)
            self.buttons.append(button)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = TicTacToeGUI()
    app.run()