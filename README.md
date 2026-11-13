# Mystery Island

## Overview

Mystery Island is a Python-based, text adventure game where players must make decisions, explore different locations, collect essential items, and manage their energy to survive and escape from a mysterious island.

The game focuses on problem-solving, decision-making, and resource management.

## Story

You are an adventurer who becomes stranded on a mysterious island after being separated from your group of sailors during a storm.

Your fellow sailors search for you but eventually assume you are lost and leave the island.

With limited energy and no immediate way to escape, you must explore the island, collect useful items, overcome obstacles, and find a way to signal for rescue.

Your ultimate objective is to reach the Lighthouse and light its beacon before you run out of energy.

Will you survive Mystery Island?

## Features

The game provides the following features:

1. **Move:** Travel between connected locations on the island.
2. **Look Around:** Explore your current location and discover available items.
3. **Collect Items:** Find and collect essential items such as the Rope and Lantern.
4. **View Inventory:** Check the items you have collected.
5. **Light Beacon:** Light the Lighthouse beacon when you have the required item.
6. **Quit Game:** Exit the current adventure.
7. **Replay:** Start a new adventure after completing or losing a game.

## Game Rules

### Energy Management
- Every successful movement consumes one energy point.
- The player starts with five energy points.
- Invalid movements do not consume energy.
- The game ends in defeat when the player's energy reaches zero or below.

### Movement
- The player can move only between connected locations.
- The island has five locations: Beach, Jungle, Cave, Old Bridge, and Lighthouse.

### Items
There are two essential items:

- **Lantern:** Found in the Jungle. Required to light the Lighthouse beacon.
- **Rope:** Found in the Cave. Required to cross the Old Bridge and reach the Lighthouse.

Each item can only be collected once.

### Old Bridge Restriction
The player must collect the Rope before crossing from the Old Bridge to the Lighthouse.

Attempting to cross without the Rope will prevent movement.

### Beacon Requirement
The player must reach the Lighthouse and have the Lantern in their inventory before lighting the beacon.

### Winning the Game
The player wins by successfully lighting the Lighthouse beacon.

### Losing the Game
The player loses when their energy reaches zero or below before successfully completing the objective.

## Requirements

- Python 3.12 or later.
- No external Python packages are required.
- Python's built-in `unittest` module is used for automated testing.

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/andrewokala/mystery-island.git
```

### 2. Enter the Project Directory

```bash
cd mystery-island
```

## Running the Game

Run the following command from the project directory:

```bash
python3 main.py
```

## Running Tests

To execute the automated test suite, run:

```bash
python3 -m unittest discover -s tests -v
```

The tests verify important game behaviours, including:

- Initial player state.
- Valid and invalid movement.
- Inventory management.
- Item collection restrictions.
- Beacon requirements.
- Victory and defeat conditions.
- Prevention of actions after the game ends.
- Creation of a fresh player state for a new adventure.

## Project Structure

```text
mystery-island/
│
├── tests/
│   └── test_game.py
│
├── .gitignore
├── game.py
├── main.py
└── README.md
```

### File Descriptions

- **main.py:** Handles user interaction, displays menus, receives input, and controls the game flow.
- **game.py:** Contains the game logic, location data, movement rules, inventory management, energy management, and game-ending conditions.
- **tests/test_game.py:** Contains automated unit tests for verifying the game logic.
- **.gitignore:** Specifies files and directories Git should ignore.
- **README.md:** Provides project information, setup instructions, game rules, and testing instructions.

## Limitations

The current version has the following limitations:

- The game uses a command-line interface; it does not have a graphical interface.
- Game progress is not saved between sessions.
- The game does not support multiplayer gameplay.
- The game uses predefined locations, items, and rules rather than dynamically generated content.