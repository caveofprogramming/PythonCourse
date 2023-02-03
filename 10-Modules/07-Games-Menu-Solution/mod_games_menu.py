#!./venv/bin/python

from games import game_of_life as gol, wordgame

def main():

    games = {
        "Game of Life": gol.main,
        "Guess the Word": wordgame.main,
    }

    games_list = list(games.keys())

    for i in range(0, len(games_list)):
        print(f"{i + 1}. {games_list[i]}")

    user_input = input("Choose a game: ")

    if not user_input.isnumeric():
        print("Invalid option.")
        return

    choice = int(user_input)

    if choice < 1 or choice > len(games_list):
        print("Invalid option.")
        return

    game_key = games_list[choice - 1]

    games[game_key]()

if __name__ == '__main__':
    main()