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

    def available_moves(self) -> list: 
        position_list = list()

        for index_pos in range(0,len(self.board)):
            if self.board[index_pos] == '-':
                position_list.append(index_pos)

        return position_list

    def play_move(self, position, token) -> None:
        self.board[position] = token

    def undo_move(self, position) -> None: 
        self.board[position] = '-'

    def minimax(self, max_player):
        winner = self.is_game_over() 
        if winner: 
            if winner == self.bot_token:
                return 1 
            else: 
                return -1 
        
        if self.is_draw():
            return 0 
        
        if max_player:
            max_score = float('-inf')

            for position in self.available_moves():
                self.play_move(position, self.bot_token)
                max_score = max(max_score, self.minimax(False))
                self.undo_move(position)

            return max_score
        
        else: 
            min_score = float('inf')

            for position in self.available_moves():
                self.play_move(position, self.player_token)
                min_score = min(min_score, self.minimax(True))
                self.undo_move(position)

            return min_score

    def best_move(self):
        best_score = float('-inf')
        best_position = None

        for position in self.available_moves():
            self.play_move(position, self.bot_token)

            current_score = self.minimax(False)

            self.undo_move(position)

            if current_score > best_score: 
                best_score = current_score
                best_position = position

        return best_position

    def update_board(self, new_board):
        self.board = new_board