game_title = """
    ====================================
            MYSTERY ISLAND
    ====================================

    A storm has destroyed your ship.
    You wake up on a strange island.

    Your mission:
    Find the missing objects.
    Restore the lighthouse beacon.
    Escape before your energy runs out.
"""
print(game_title)

player_name = input("Enter your name: ").strip()

if not player_name:
    player_name = "Advanturer"

welcome_msg = f"""
    Welcome, {player_name}!

    ====================================
                BEACH
    ====================================

    You wake up on a quiet beach.
    The waves crash against the shore.
    You notice a thick jungle to the north.

    Energy: 5

    What would you like to do?
"""

print(welcome_msg)


while True:

    print("""
        Pick a Choice:

        1. Look around
        2. Quit game
    """)
    choice = input("Choose your choice: ").strip()

    if choice == "1":
        print("You're currently in the beach.")
    elif choice == "2":
        print("Goodbye!")
        break
    else:
        print("Invalid choice")