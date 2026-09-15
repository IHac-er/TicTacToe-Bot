class OccupiedPosition(Exception): 
    pass 

class TicTacToe: 
    def __init__(self):
        self.board = ['-','-','-','-','-','-','-','-','-']

    def game_over(self) -> tuple[str, bool]:
        for row in range(0, 9, 3):
            if self.board[row] != '-' and self.board[row] == self.board[row+1] == self.board[row+2]:
                return (self.board[row], True)
            
        for col in range(3):
            if self.board[col] != '-' and self.board[col] == self.board[col+3] == self.board[col+6]: 
                return (self.board[col], True)
            
        if self.board[0] != '-' and self.board[0] == self.board[4] == self.board[8]: 
            return (self.board[0], True)
        
        if self.board[2] != '-' and self.board[2] == self.board[4] == self.board[6]: 
            return (self.board[2], True)
        
        if all(cell != '-' for cell in self.board): 
            return ("-", True) 
        
        return ("", False)

    def play_move(self, position, token) -> None:
        if self.board[position]  != '-':
            raise OccupiedPosition("Position is occupied!")
        self.board[position] = token

    def get_board(self) -> list[str]:
        return self.board

    def print_board(self) -> None:
        for i in range(0,7,3):
            print(f"{self.board[i]} {self.board[i+1]} {self.board[i+2]}")