locations = {
    "Beach": ["Jungle"],
    "Jungle": ["Beach", "Cave"],
    "Cave": ["Jungle"]
}


def new_game(name):
    player = {
        "name": name,
        "location": "Beach",
        "energy": 5,
        "inventory": [],
        "game_over": False,
        "won": False
    }

    return player


def available_actions(player):
    current_location = player["location"]

    return locations[current_location]

def move_player(player, destination):
    current_location = player["location"]

    possible_destinations = available_actions[player]

    if destination not in possible_destinations:
        return "False", f"You cannot move from {current_location} to {destination}"

    player["location"] = destination

    return True, f"You moved to {destination}"