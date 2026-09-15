from bot import TicTacToeBot

def main():
    print("=" * 100)
    print("TIC-TAC-TOE")
    print("=" * 100)

    player_turn = True if input("Do you want to go first?(Y/N): ").lower().strip() == "y" else False 

if __name__ == "__main__":
    main()