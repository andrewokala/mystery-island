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

    return True, f"You moved to {destination}!"


def collect_item(player, item):
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