# TextBasedGame.py
# Author: Yashwantini Bhautkar
# Title: Whispers in the Asylum
# A text-based horror adventure game

# -------- FUNCTION DEFINITIONS -------- #

def show_instructions():
    """Display the game title, storyline, and available commands."""
    print("""
    -------------------------------
         WHISPERS IN THE ASYLUM
    -------------------------------
    You wake up in a cursed asylum. 
    Collect all 6 protective artifacts before facing the Warden's Spirit.

    Commands:
      go North / go South / go East / go West
      get [item name]
      quit - to end the game
    -------------------------------
    """)


def show_status(current_room, inventory, rooms):
    """Display the player's current location, inventory, and visible item."""
    print(f"\nYou are in the {current_room}")
    print("Inventory:", inventory)
    if "item" in rooms[current_room]:
        print(f"You see a {rooms[current_room]['item']}")
    else:
        print("There’s nothing of interest here.")
    print("-------------------------------")


# -------- MAIN GAME FUNCTION -------- #

def main():
    # Dictionary linking rooms and items with exact directions
    rooms = {
        'Patient Ward': {'North': 'Security Office', 'West': 'Cafeteria', 'East': 'Kitchen', 'South': 'Operating Theater'},
        'Security Office': {'South': 'Patient Ward', 'North': 'Isolation Cell', 'East': 'Morgue', 'item': 'Security Keycard'},
        'Kitchen': {'West': 'Patient Ward', 'South': 'Storage Room', 'item': 'Candle Stub'},
        'Cafeteria': {'East': 'Patient Ward', 'item': 'Patient Journal'},
        'Operating Theater': {'North': 'Patient Ward', 'East': 'Storage Room', 'item': 'Rusty Scalpel'},
        'Storage Room': {'West': 'Operating Theater', 'North': 'Kitchen', 'item': 'Old Photograph'},
        'Morgue': {'West': 'Security Office', 'item': 'Broken Rosary'},
        'Isolation Cell': {'South': 'Security Office', 'item': 'Warden\'s Spirit'}  # villain
    }

    inventory = []  # List to track collected items
    current_room = 'Patient Ward'  # Starting point
    show_instructions()  # Show intro

    while True:
        show_status(current_room, inventory, rooms)

        # Get user input
        move = input("Enter your move: ").strip().title()

        if move.lower() == 'quit':
            print("You gave up... the Warden's Spirit claims another soul.")
            break

        # --- Handle movement ---
        elif move.startswith('Go '):
            direction = move[3:]
            if direction in rooms[current_room]:
                current_room = rooms[current_room][direction]
            else:
                print("You can’t go that way. The path is blocked or locked.")

        # --- Handle item collection ---
        elif move.startswith('Get '):
            item_name = move[4:]
            if "item" in rooms[current_room] and item_name.lower() == rooms[current_room]["item"].lower():
                inventory.append(item_name)
                print(f"You picked up the {item_name}.")
                del rooms[current_room]['item']
            else:
                print("You can’t get that item here.")

        else:
            print("Invalid command. Try again.")

        # --- Check win condition ---
        if len(inventory) == 6:
            print("""
            You have collected all artifacts!
            The Warden's Spirit cannot stop you.
            YOU WIN!
            -------------------------------
            """)
            break

        # --- Check lose condition ---
        if "item" in rooms[current_room] and rooms[current_room]["item"] == "Warden's Spirit":
            if len(inventory) < 6:
                print("""
                The Warden's Spirit appears!
                You have not collected all artifacts...
                GAME OVER.
                """)
                break
            else:
                print("""
                You face the Warden's Spirit with all artifacts!
                The spirit screams and disappears.
                YOU WIN!
                -------------------------------
                """)
                break


# -------- START THE GAME -------- #
if __name__ == "__main__":
    main()
