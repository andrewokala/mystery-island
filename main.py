from game import (
    new_game,
    available_actions,
    move_player,
    collect_item,
    display_inventory,
    item_at_location,
    light_beacon
)


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
        "Beach": "You wake up on a quiet beach. The waves crash against the shore.",
        "Jungle": "You enter a thick jungle filled with strange sounds.",
        "Cave": "You discover a dark cave hidden behind the jungle.",
        "Old Bridge": "You discover an old bridge connecting the cave to the lighthouse.",
        "Lighthouse": "You have reached the lighthouse. Its beacon is dark."
    }

    print(f"\nCurrent Location: {location}")
    print(descriptions[location])


def display_menu(player):
    destinations = available_actions(player)

    print("""
    What would you like to do?

    1. Move
    2. Look around
    3. Collect item
    4. View inventory
    5. Light beacon
    6. Quit game
    """)

    print("Available destinations:")

    for destination in destinations:
        print(f"- {destination}")


def main():
    display_title()

    while True:

        player_name = input("Enter your name: ").strip()

        if not player_name:
            player_name = "Adventurer"

        player = new_game(player_name)

        quit_requested = False

        print(f"\nWelcome, {player['name']}!")

        while not player["game_over"]:
            display_location(player)
            display_menu(player)

            choice = input("\nChoose an action: ").strip()

            if choice == "1":
                destination = input(
                    "Where would you like to go? "
                ).strip().title()

                success, message = move_player(player, destination)

                print(message)

            elif choice == "2":
                item = item_at_location(player)

                print("You look around carefully.")

                if item:
                    print(f"You discover something: {item}!")

            elif choice == "3":
                item = input("Which item would you like to collect? ").strip().title()

                success, message = collect_item(player, item)

                print(message)

            elif choice == "4":
                inventory = display_inventory(player)

                if not inventory:
                    print("Your inventory is empty.")
                else:
                    print("\nYour inventory:")

                    for item in inventory:
                        print(f"- {item}")

            elif choice == "5":
                success, message = light_beacon(player)
                print(message)

            elif choice == "6":
               quit_requested = True
               player["game_over"] = True

            else:
                print("Invalid choice. Please select 1, 2, 3, 4, 5 or 6.")

        while True:

            if quit_requested:
                print("\nThank you for playing Mystery Island!")
                return

            replay = input(
                "\nWould you like to play again? (yes/no): "
            ).strip().lower()

            if replay in ("yes", "y"):
                print("\nStarting a new adventure...")
                break
            elif replay in ("no", "n"):
                print("\nThank you for playing Mystery Island!")
                return
            else:
                print("Invalid response, enter yes or no.")



if __name__ == "__main__":
    main()