def intro():
    print("You wake up in a dark forest. You can go left or right.")
    choice = input("Which direction do you choose? (left/right): ").strip().lower()
    if choice == "left":
        left_path()
    elif choice == "right":
        right_path()
    elif choice == "center":
        center_path()
    else:
        print("You stand still, unsure what to do. The forest swallows you.")

def left_path():
    print("You walk left and find a mysterious glowing sword stuck in a stone.")
    print("You pull the sword from the stone and feel heroic power surge through you.")
    print("You move forward on you journey and defeat a dragon.")
def right_path():
    print("You walk right and encounter a talking squirrel who challenges you to a duel.")
    print("You cheat during the duel by using a potion and beat the squirrel")
    print("You take all of the squirrels loot.")
if __name__ == "__main__":
    intro()