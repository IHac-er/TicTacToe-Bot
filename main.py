import sys

from bot import TicTacToeBot
from TicTacToe import TicTacToe, OccupiedPosition
from TicTacToeGUI import TicTacToeGUI

def cli():
    print("=" * 100)
    print("TIC-TAC-TOE")
    print("=" * 100)

    while True:
        user_choice = input("Do you want to go first?(Y/N): ").lower().strip()

        if user_choice not in ['y', 'n']:
            print("Invalid Input! Try Again.")
            continue

        player_turn = (user_choice == "y")
        break
    
    if player_turn: 
        player_token, bot_token = 'X' , 'O'
    else: 
        player_token, bot_token = 'O' , 'X'

    board = TicTacToe() 
    bot = TicTacToeBot(bot_token, player_token)

    board.print_board()

    status = False, False
    while not status[1]:

        if player_turn: 
            try: 
                player_choice = int(input("Enter a number (1-9): "))
                if not 1 <= player_choice <= 9: 
                    continue 
            except: 
                print("Invalid Input! Try Again.")
                continue

            try:
                board.play_move(player_choice-1, player_token)
            except OccupiedPosition as e: 
                print(f"{e}! Try Again.")
                continue

            bot.update_board(board.get_board())
            board.print_board()
            player_turn = False 

        else:
            print("Bot Thinking...")
            bot_pos = bot.best_move()
            board.play_move(bot_pos, bot_token)
            bot.update_board(board.get_board())
            board.print_board()
            player_turn = True

        status = board.game_over()

    print(f"{status[0]} Wins!")

def main():
    if "--cli" in sys.argv:
        cli()
    else: 
        app = TicTacToeGUI()
        app.run()

if __name__ == "__main__":
    main()