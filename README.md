# UMU Rogue Dungeon
#### Created By Jacob Sanford & Alec Barker
A Basic Rogue Dungeon Game in Python

Created for the University of Mount Union's CSC 221: Intermediate Programming in Python class taught by Dr. Kenneth Weber

## How to Run the Program
1. Open Command Prompt or Python Shell
2. Navigate to the directory that the program is stored in
3. Run `main.py`
	- If the user does not have pygame installed on their computer, the program will prompt them to install it by running `py -m pip install -U pygame --user` in the Command Prompt window
4. The user will see a menu and be prompted for an input. They can type in:
	- `Play` to play the game
	- `Instructions` to read the gameplay instructions listed below
	- `Quit` to close out of the program

## Gameplay Instructions
The objective of the game is to obtain points while avoiding death. You can get points by killing monsters or collecting loot in a level.

The game remains static until you move the player character. This means that monsters can't move until you choose to move. Therefore, you should be strategic about every move you make.

You will take damage by moving onto the same tile or staying within one tile of a monster. If you receive too much damage, your character will die and the game will end. Monsters have a chance to dodge or counter attack, so try to avoid attacking them in large groups.

To collect loot, simply move the player character over top of the loot.

Objects:
- Green Box  :  Player
- Red Boxes  :  Monsters
- Yellow Boxes  :  Loot
- Blue Boxes  :  Walls
- Black Boxes  :  Empty Tiles

Controls:
- W or ↑  :  Move Up
- S or ↓  :  Move Down
- A or ←  :  Move Left
- D or →  :  Move Right
- E  :  Attack
- Esc  :  Exit Game

## Current Features
- A user is presented with a menu upon starting the game. They can:
	- Play the game
	- View the instructions
	- Enter gameplay modifiers in the options
	- Quit the program
- In the game, there are four types of objects the user will encounter:
	- The player character
		- There is one player character that is randomly generated on the playing grid
		- The user can control the player character using the WASD keys or arrow keys to move around the grid
		- The player character can use the E key to attack enemies and will gain points from killing them
		- The player character can't move onto walls
		- The player character will be dealt damage and lose points if they move over top of an enemy, but they will kill the enemy in the process
	- Enemies
		- There are multiple enemies that randomly generate on the playing grid
		- Enemies can only move around the grid when the user makes the player character move
		- Enemies can't move onto other enemies or onto walls
		- When the player character moves over top of an enemy, the enemy will deal damage to the player character and make them lose points, but the enemy will die
	- Loot
		- There are multiple pieces of loot that randomly generate on the playing grid
		- Loot does not move around the grid at all
		- The player character can pick up loot by moving over top of it
	- Walls
		- There are multiple walls that randomly generate on the playing grid
		- Neither the player character nor enemies can move over top of a wall
- Options
	- Users can customize some aspects of the game such as:
		- Grid size
		- Number of enemies
		- Number of loot items
		- Number of walls
		- Base player character health

## Possible Features in the Future
- Custom Dungeons
	- Randomly generate small dungeon rooms that are connected by hallways
		- Some rooms will be special rooms
	       	- Chest Room
	       	- Locked Room
	       	- Traps
- Add custom 2D sprites for each type of object
- Multiple levels
	- If a user collects all loot and/or kills all enemies, they can progress on to a new randomly generated dungeon