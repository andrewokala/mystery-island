from game import new_game, available_actions, move_player

def display_title():
    print("""
    ====================================
            MYSTERY ISLAND
    ====================================

    A storm has destroyed your ship.
    You wake up on a strange island.

    Your mission:
    Find the missing objects.
    Restore the lighthouse beacon.
    Escape before your energy runs out.
    """)
def display_location(player):
    location = player["location"]

    descriptions = {
        "Beach": "You wake up on a quiet beach. The waves crash agianst the shore.",
        "Jungle": "You enter a thick jungle filled with strange sounds.",
        "Cave": "You discover a dark cave hidden behind the jungle."
    }

    print(f"\nCurrent Location: {location}")
    print(descriptions[location])

def display_menu(player):
    destinations = available_actions(player)

    print("\nWhat would you like to do?")
    print("1. Move")
    print("2. Look around")
    print("3. Quit game")

    print("\nAvailable destinations:")

    for destination in destinations:
        print((f"- {destination}"))

def main():
    display_title

    player_name = input("Enter your name: ").strip()

    if not player_name:
        player_name = "Advanturer"

    player = new_game(player_name)

    print(f"\nWelcome, {player['name']}!")

    while True:
        display_location(player)
        display_menu(player)

        choice = input("\nChoose an action: ").strip()

        if choice == "1":
            destination = input ("Where would you like to go? ").strip().title()

            success, message = move_player(player, destination)

            print(message)

        elif choice == "2":
            print("You look around carefully.")
        
        elif choice == "3":
            print("Goodbye! Thanks for playing Mystery Island.")
            break

        else:
            print("Invalid choice. Please select 1, 2 or 3.")

if __name__ == "__main__":
    main()