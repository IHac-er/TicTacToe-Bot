class TicTacToeBot: 
    def __init__(self, bot_token, player_token):
        self.board = ['-','-','-','-','-','-','-','-','-']
        self.bot_token = bot_token
        self.player_token = player_token

    def is_draw(self) -> bool:
        return all(cell != '-' for cell in self.board)

    def is_game_over(self) -> str | bool:
        for row in range(0, 9, 3):
            if self.board[row] != '-' and self.board[row] == self.board[row+1] == self.board[row+2]: 
                return self.board[row]
        
        for col in range(3):
            if self.board[col] != '-' and self.board[col] == self.board[col+3] == self.board[col+6]: 
                return self.board[col]
        
        if self.board[0] != '-' and self.board[0] == self.board[4] == self.board[8]: 
            return self.board[0]
        
        if self.board[2] != '-' and self.board[2] == self.board[4] == self.board[6]: 
            return self.board[2]

        return False

    