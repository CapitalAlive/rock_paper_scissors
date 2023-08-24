import random


def compare_choices(p1_choice, list_of_options):
    computer_choice = random.choice(list_of_options)
    if computer_choice == p1_choice:
        print(f"There is a draw ({computer_choice})")
        return 50
    n_of_possible_win_elements = (len(list_of_options) - 1) / 2
    p1_choice_index = list_of_options.index(p1_choice)
    win_index_starts_from = int(p1_choice_index - n_of_possible_win_elements)
    win_range_list = list(range(win_index_starts_from, p1_choice_index))
    p1_wins_of_list = [list_of_options[x] for x in win_range_list]
    if computer_choice in p1_wins_of_list:
        print(f"Well done. The computer chose {computer_choice} and failed")
        return 100
    else:
        print(f"Sorry, but the computer chose {computer_choice}")
        return 0


def get_user_input(p_score, list_of_options):
    while True:
        user_input = input()
        if user_input in list_of_options:
            return user_input
        elif user_input == "!exit":
            print("Bye!")
            exit()
        elif user_input == "!rating":
            print(f"Your rating: {p_score}")
        else:
            print("Invalid input")


def read_rating():
    rating_dict = {}
    with open("rating.txt", "r") as file:
        for line in file:
            name, rating = line.split()
            rating_dict[name] = int(rating)
        return rating_dict


def write_rating(rating_dict):
    with open("rating.txt", "w") as file:
        for name, rating in rating_dict.items():
            file.write(f"{name} {rating}\n")


def game():
    p1_name = input("Enter your name: ")
    print(f"Hello, {p1_name}")
    game_options = input().split(",")
    print("Okay, let's start")
    if game_options == [""]:
        game_options = ["scissors", "rock", "paper"]
    while True:
        rating_dictionary = read_rating()
        p1_score = rating_dictionary.setdefault(p1_name, 0)
        rating_dictionary[p1_name] = p1_score + compare_choices(get_user_input(p1_score, game_options), game_options)
        write_rating(rating_dictionary)


game()
