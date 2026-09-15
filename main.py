from bot import TicTacToeBot

class TicTacToe: 
    def __init__(self):
        self.board = ['-','-','-','-','-','-','-','-','-']

    def game_over(self) -> bool:
        for row in range(0, 9, 3):
            if self.board[row] != '-' and self.board[row] == self.board[row+1] == self.board[row+2]:
                print(f"{self.board[row]} Wins!")
                return True
            
        for col in range(3):
            if self.board[col] != '-' and self.board[col] == self.board[col+3] == self.board[col+6]: 
                print(f"{self.board[col]} Wins!")
                return True 
            
        if self.board[0] != '-' and self.board[0] == self.board[4] == self.board[8]: 
            print(f"{self.board[0]} Wins!")
            return True 
        
        if self.board[2] != '-' and self.board[2] == self.board[4] == self.board[6]: 
            print(f"{self.board[2]} Wins!")
            return True 
        
        if all(cell != '-' for cell in self.board): 
            print("Draw!")
            return True 
        
        return False

def main():
    print("=" * 100)
    print("TIC-TAC-TOE")
    print("=" * 100)

    player_turn = True if input("Do you want to go first?(Y/N): ").lower().strip() == "y" else False 

    if player_turn: 
        player_token, bot_token = 'X' , 'O'
    else: 
        player_token, bot_token = 'O' , 'X'

if __name__ == "__main__":
    main()