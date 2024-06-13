def initialize_rooms():
    rooms={#dict of dict
        "start":{
            "description":"you are in the start room",
            "north":"hallroom",#make each direction as key
            "items":[]
        },
        "hallroom":{
            "description":"you are in the hall",
            "west":"livingroom",
            "south":"start",
            "east":"kitchen",
            "items":[]
        },
        "livingroom":{
            "description":"you are in the livingroom and there is a key",
            "east":"hallroom",
            "items":["key"]
        },
        "kitchen":{
            "description":"you are in the kitchen",
            "west":"hallroom",
            "items":["knife"]
        },
        'garden': {
            'description': 'You are in the garden. Congratulations, you have won!',
            'items': []
        }
    }
    return rooms
# print(initialize_rooms())

def move(current_room,direction,rooms):
    if direction in rooms[current_room]:
        return rooms[current_room][direction]
    else:
        print("you can't go that direction")
        return current_room

def take_item(current_room,rooms,inventory):
    if rooms[current_room]["items"]:
        item=rooms[current_room]["items"].pop()#remove item from room
        inventory.append(item)
        print(f"{item} picked and added to inventory list")
    else:
        print("no items in this room")


def use_item(item,inventory,rooms,current):
    if item in inventory:
        if item=="key" and current=="hallroom":
            rooms[current]["north"]="garden"#add direction to the hallroom
            print("you have used the key to unlock the garden way")
        else:
            print("you can not use this item here")
    else:
        print("you don't have this item")

def main():
    print("welcome to the adventure game")
    rooms=initialize_rooms()
    current_room="start"
    inventory_list=[]
    while current_room!="garden":
        print("you need move to garden area")
        print(rooms[current_room]["description"])
        action=str(input("enter your action move/use/quit/take: "))
        if action=="move":
            direction = input("Which direction? (north, south, east, west): ").strip().lower()
            current_room=move(current_room,direction,rooms)
        elif action == 'take':
            take_item(current_room, rooms, inventory_list)
        elif action == 'use':
            item = input("Which item? ").strip().lower()
            current_room=use_item(item, inventory_list, rooms, current_room)
        elif action == 'quit':
            print("Thanks for playing!")
            break
        else:
            print("Invalid action. Please choose 'move', 'take', 'use', or 'quit'.")
    if current_room == 'garden':
        print("Congratulations, you have reached the garden and won the game!")

        
main()