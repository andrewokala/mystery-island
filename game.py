locations = {
    "Beach": ["Jungle"],
    "Jungle": ["Beach", "Cave"],
    "Cave": ["Jungle", "Old Bridge"],
    "Old Bridge": ["Cave", "Lighthouse"],
    "Lighthouse": ["Old Bridge"]
}

items_by_location = {
    "Jungle": "Lantern",
    "Cave": "Rope"
}


def new_game(name):
    return {
        "name": name,
        "location": "Beach",
        "energy": 5,
        "inventory": [],
        "game_over": False,
        "won": False
    }


def available_actions(player):
    current_location = player["location"]

    return locations[current_location]


def move_player(player, destination):
    if player["game_over"]:
        return False, "The game has already ended. Start a new adventure."

    current_location = player["location"]

    possible_destinations = available_actions(player)

    if destination not in possible_destinations:
        return False, f"You cannot move from {current_location} to {destination}."

    if (
        current_location == "Old Bridge"
        and destination == "Lighthouse"
        and not can_cross_bridge(player)
    ):
        return False, "You need a rope to cross the Old Bridge."
        
    player["location"] = destination
    player["energy"] -= 1

    if player["energy"] <= 0:
        player["game_over"] = True
        player["won"] = False
        return False, "You have run out of energy. Game over!"

    return True, f"You moved to {destination}!"


def collect_item(player, item):
    if player["game_over"]:
        return False, "The game has already ended. Start a new advanture."
        
    current_location = player["location"]

    available_item = items_by_location.get(current_location)

    if item != available_item:
        return False, "This item is not available here."

    if item in player["inventory"]:
        return False, "You have already collected this item."

    player["inventory"].append(item)

    return True, f"{item} successfully added to your inventory."


def display_inventory(player):
    return player["inventory"]


def can_cross_bridge(player):
    return "Rope" in player["inventory"]


def can_light_beacon(player):
    return (
        player["location"] == "Lighthouse"
        and "Lantern" in player["inventory"]
    )


def item_at_location(player):
    item = items_by_location.get(player["location"])

    if item is None or item in player["inventory"]:
        return None
    
    return item

def light_beacon(player):
    if player["game_over"]:
        return False, "the game has already ended. Start a new adventure"

    if not can_light_beacon(player):        
        if player["location"] != "Lighthouse":
            return False, f"Cannot light beacon in {player['location']}."
        
        return False, "Lantern is required to light the beacon."

    player["won"] = True
    player["game_over"] = True

    return True, "You successfully light the beacon. You won!"