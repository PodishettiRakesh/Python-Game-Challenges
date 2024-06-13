def initialize_rooms():
    rooms={
        "start":{
            "description":"you are in the start room",
            "north":"hallroom",
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
            "description":"you are in the hall and there is a key",
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
        item=rooms[current_room]["items"].pop()
        inventory.append(item)
        print(f"{item} picked and added to inventory list")
    else:
        print("no items in this room")
# rooms=initialize_rooms()
# currentroom="livingroom"
# inventory=[]
# take_item(currentroom,rooms,inventory)
    
# print(inventory)

def use_item(item,inventory,rooms,current):
    if item in inventory:
        if item=="key" and current=="hallroom":
            rooms[current]["north"]="garden"
            print("you have used the key to unlock the garden way")
        else:
            print("you can not use this item here")
    else:
        print("you don't have this item")

