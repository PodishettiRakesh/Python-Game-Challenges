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
