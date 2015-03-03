import pickle
games = [] 
class Games:
    def __init__(self):
        self.name = None
        self.platform = None
        self.genre = None
        self.cost = None
        self.no_of_players = None
        self.online_functionality = None
def load_games(filename):
    with open("games.txt", moder="r", encoding="utf-8"):
        
    pass

def save_games(filename, games):
    with open("games.txt", mode="w", encoding="utf-8"):
        pickle.dump(games)    
    pass

#the parameter is games because eventually you will be displaying
#multiple games using this function
def display_games(games):
    length = len(games)
    for count in range(length):
        print("-"*25)
        print("| Name | {0} |".format(new_game.name))
        print("| Platform | {0} |".format(new_game.platform))
        print("| Genre | {0} |".format(new_game.genre))
        print("| Cost | {0} |".format(new_game.cost))
        print("| Players | {0} |".format(new_game.no_of_players))
        print("| Online | {0} |".format(new_game.online_functionality))
    pass

def get_game_from_user(games):
    done = False
    while done == False:
        new_game = Games()
        new_game.name = input("Please enter the name of the game(enter -1 to end): ")
        if new_game.name == "-1":
            done = True    
        new_game.platform = input("Please enter the platform of the game: ")
        new_game.genre = input("Please enter the genre of the game: ")
        new_game.cost = input("Please enter the cost of the game in pounds: ")
        new_game.no_of_players = input("Please enter the number of players: ")
        new_game.online_functionality = input("Does the game have online functionality?: ")
        games.append(new_game)
    return games      
    pass

def display_menu():
    print()
    print("***Welcome to the Computer and Video Game Database***")
    print()
    print("1. Add new games")
    print("2. Display games")
    print("3. Exit program")
    print()

def main():
    load_games()
    exit_program = False
    while not exit_program:
        try:
            display_menu()
            selected_option = int(input("Please select a menu option: "))
            if selected_option == 1:
               get_game_from_user(games)
               pass
            elif selected_option == 2:
                 display_games(games)
                pass
            elif selected_option == 3:
                 save_games(filename, games)
                 exit_program = True
                 pass
            else:
                 print("Please enter a valid option (1-3)")
                 print()
        except ValueError:
            print("That was not an integer. Please try again.")

if __name__ == "__main__":
    main()



