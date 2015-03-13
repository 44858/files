import pickle

class Games:
    def __init__(self):
        self.name = None
        self.platform = None
        self.genre = None
        self.cost = None
        self.no_of_players = None
        self.online_functionality = None

    
def load_games(filename):
    try:
        with open(filename, mode="rb")as game_file:
             games = pickle.load(game_file)
             return games
    except FileNotFoundError and EOFError:
        print("File cannot be found.")
    
def save_games(filename, games_list):
    with open(filename, mode="wb"):
        pickle.dump(games_list)
        
#the parameter is games because eventually you will be displaying
#multiple games using this function
def display_games(games_list):
    print("-"*30)
    for game in games:
        print("|Name                |{0:>5}|".format(new_game.name))
        print("|Platform            |{0:>5}|".format(new_game.platform))
        print("|Genre               |{0:>5}|".format(new_game.genre))
        print("|Cost                |{0:>5}|".format(new_game.genre))
        print("|No. of players      |{0:>5}|".format(new_game.no_of_players))
        print("|Online Functionality|{0:>5}|".format(new_game.online_functionality))
        print("-"*30)
                    
def get_game_from_user(games):
    games_list = []
    done = False
    while done == False:
       new_game = Games()
       new_game.name = input("Name: ")
       if new_game.name == "-1":
           done = True
       new_game.platform = input("Platform: ")
       new_game.genre = input("Genre: ")
       new_game.cost = input("Cost(in pounds): ")
       new_game.no_of_players = input("No. of players: ")
       new_game.online_functionality = input("Online functionality: ")
       games_list.append(Games())
    return games_list 
    
def display_menu():
    print()
    print("***Welcome to the Computer and Video Game Database***")
    print()
    print("1. Add new games")
    print("2. Display games")
    print("3. Exit program")
    print()

def main():
    filename = input("Please enter a filename: ")
    games = load_games(filename)
    exit_program = False
    while not exit_program:
        try:
            display_menu()
            selected_option = int(input("Please select a menu option: "))
            if selected_option == 1:
               get_game_from_user(games)
            elif selected_option == 2:
                 display_games(games)
            elif selected_option == 3:
                 save_games(filename, games)
                 exit_program = True
            else:
                 print("Please enter a valid option (1-3)")
                 print()
        except ValueError:
            print("That was not an integer. Please try again.")

if __name__ == "__main__":
    main()



