import random
import simplegui

# Game variables
player_health = 100
inventory = []
current_room = 'start'
rooms = {
    'start': "You are in a dark, cold room. There is a door to the north and south.",
    'north_room': "You move to the North room. There's a dark cave ahead.",
    'south_room': "You move to the South room. You see a river with a boat.",
}
items = ['sword', 'shield', 'health_potion']

# Load images
background_start = simplegui.load_image("assets/start_room.png")
background_north = simplegui.load_image("assets/north_room.png")
background_south = simplegui.load_image("assets/south_room.png")
sword_image = simplegui.load_image("assets/sword.png")
health_potion_image = simplegui.load_image("assets/health_potion.png")
monster_image = simplegui.load_image("assets/monster.png")

# Create GUI components
def draw(canvas):
    canvas.draw_text(f"Health: {player_health}", (20, 20), 24, "White")
    canvas.draw_text(f"Inventory: {', '.join(inventory)}", (20, 60), 24, "White")
    
    # Draw room background based on the current room
    if current_room == 'start':
        canvas.draw_image(background_start, (200, 150), (400, 300), (200, 150), (400, 300))
    elif current_room == 'north_room':
        canvas.draw_image(background_north, (200, 150), (400, 300), (200, 150), (400, 300))
    elif current_room == 'south_room':
        canvas.draw_image(background_south, (200, 150), (400, 300), (200, 150), (400, 300))
    
    # Draw item images in inventory
    if 'sword' in inventory:
        canvas.draw_image(sword_image, (32, 32), (64, 64), (300, 100), (64, 64))
    if 'health_potion' in inventory:
        canvas.draw_image(health_potion_image, (32, 32), (64, 64), (300, 180), (64, 64))

def update_room_description():
    global current_room
    description = rooms[current_room]
    label.set_text(description)

def go_north():
    global current_room
    current_room = 'north_room'
    update_room_description()
    random_event()

def go_south():
    global current_room
    current_room = 'south_room'
    update_room_description()
    random_event()

def pick_up_item(item):
    inventory.append(item)
    items.remove(item)
    label.set_text(f"Picked up {item}! Inventory: {', '.join(inventory)}")

def examine_room():
    if current_room == 'north_room':
        pick_up_item('sword')
    elif current_room == 'south_room':
        pick_up_item('health_potion')

def random_event():
    event = random.randint(1, 3)
    if event == 1:
        label.set_text("A monster appears! Prepare to fight.")
        fight_monster()
    elif event == 2:
        label.set_text("You found a hidden treasure!")
        pick_up_item('gold')
    else:
        label.set_text("The room is quiet and peaceful.")

def fight_monster():
    global player_health
    outcome = random.choice(['win', 'lose'])
    if outcome == 'win':
        label.set_text("You defeated the monster!")
    else:
        player_health -= 20
        label.set_text(f"You were hurt in the fight. Health: {player_health}")

# Setup GUI components
frame = simplegui.create_frame("Text-Based Adventure", 400, 300)
label = frame.add_label("You are standing in a dark room.", 20)
frame.add_button("Go North", go_north)
frame.add_button("Go South", go_south)
frame.add_button("Examine Room", examine_room)

frame.set_draw_handler(draw)
frame.start()
