# Blake Sutherland
# CS230--Dr. Ogden
# Quest for Adventure - Milestone 3
# December 6, 2022

# Ending scenarios: 
#           1) User dies in battle and loses. 
#           2) User kills boss, timed escape doesn't engage, user wins. 
#           3) User kills boss, timed escape engages, user runs out of time and loses.
#           4) User kills boss, timed escape engages, user escapes in time and wins.
#           5) User fights boss, runs out of items, and automatically loses.

# importing modules
import os
import random
import time


# the rooms and their corresponding items.
rooms = {
    'volcano': {
        'south': 'obsidian throne room',
        'Item': 'shield'
    },
     'obsidian throne room': {
        'north': 'volcano',
        'east': 'performing room',
        'Item': 'obsidian sword'
    },
     'performing room': {
        'south': 'stone room',
        'east': 'hallway',
        'west': 'obsidian throne room',
        'Item': 'dodge skill'
    },
     'stone room': {
        'north': 'performing room',
        'south': 'cavern',
        'east': 'courtyard',
        'west': 'armory',
        'Item': None
    },
     'armory': {
        'east': 'stone room',
        'Item': 'kick skill'
    },
     'cavern': {
        'north': 'stone room',
        'south': 'pit',
        'east': 'dragon egg museum',
        'Item': 'bow and arrow'
    },
     'pit': {
        'north': 'cavern',
        'Item': 'spear'
    },
     'dragon egg museum': {
        'north': 'courtyard',
        'west': 'cavern',
        'Item': 'poison'
    },
     'courtyard': {
        'north': 'hallway',
        'south': 'dragon egg museum',
        'east': 'dining hall',
        'west': 'stone room',
        'Item': None
    },
     'hallway': {
        'north': 'mirror maze',
        'south': 'courtyard',
        'east': 'marble throne room',
        'west': 'performing room',
        'Item': 'deep breath skill'
    },
     'mirror maze': {
        'south': 'hallway',
        'Item': 'glass cannon'
    },
     'marble throne room': {
        'south': 'dining hall',
        'east': 'room of light',
        'west': 'hallway',
        'Item': 'shuriken'
    },
     'room of light': {
        'west': 'marble throne room',
        'Item': 'lightning bolt'
    },
     'dining hall': {
        'north': 'marble throne room',
        'south': 'arena',
        'east': 'lounge',
        'west': 'courtyard',
        'Item': 'healing potion'
    },
     'arena': {
        'north': 'dining hall',
        'Item': 'whip'
    },
     'lounge': {
        'west': 'dining hall',
        'Item': 'boomerang'
    },
}

# if the user uses the 'info' command
items = {
    'shield': {
        'attack value': None,
        'defense value': 10,
        'special effect': None
     },
     'obsidian sword': {
        'attack value': 15,
        'defense value': None,
        'special effect': 'Critical hit (25 percent chance to deal double damage)'
     },
     'dodge skill': {
        'attack value': None,
        'defense value': '3-7',
        'special effect': 'Reduces enemy damage by three to seven. Can be used an infinite number of times.'
     },
     'kick skill': {
        'attack value': '3-7',
        'defense value': None,
        'special effect': 'Deals three to seven damage. Can be used an infinite number of times.'
     },
     'bow and arrow': {
        'attack value': 6,
        'defense value': None,
        'special effect': 'Shoots three arrows, each dealing six damage'
     },
     'spear': {
        'attack value': 12,
        'defense value': None,
        'special effect': None
     },
     'poison': {
        'attack value': 20,
        'defense value': None,
        'special effect': None
     },
     'deep breath skill': {
        'attack value': None,
        'defense value': None,
        'special effect': 'Heals 4 HP. Can be used an infinite number of times.'
     },
     'glass cannon': {
        'attack value': 40,
        'defense value': -15,
        'special effect': 'The highest damaging weapon in this game, but it explodes when you shoot it, dealing 15 damage to you'
     },
     'shuriken': {
        'attack value': 7,
        'defense value': None,
        'special effect': 'Throws three shurikens, each dealing seven damage'
     },
     'lightning bolt': {
        'attack value': 30,
        'defense value': None,
        'special effect': 'crit chance (25 percent chance to deal 50 percent more damage)'
     },
     'healing potion': {
        'attack value': None,
        'defense value': None,
        'special effect': 'Heals 20 HP. This potion can also raise your HP past 100.'
     },
     'whip': {
        'attack value': 10,
        'defense value': None,
        'special effect': None
     },
     'boomerang': {
        'attack value': 3,
        'defense value': None,
        'special effect': 'Deals three damage twice, once for each time it hits the enemy. Can be used an infinite number of times.'
     }
}

# keeps track of the HP values
HP_values = {
    'boss HP': 230,
    'user HP': 100
}

# if the user uses the 'help' command
moves = {
    'go {direction}': 'travel north, south, east, or west',
    'get {item}': 'add nearby item to inventory',
    'use {item}': 'put the item you specify into effect (only available during battle for most items)',
    'info {item}': 'gives the attack, defense, and effect values for the item you specify',
    'retreat': 'retreats from battle and allows you to pass through freely (only available when you have below 25% HP)',
    'quit': 'exits the game at any time'
}

# keeps track of how many times each item has been picked up
item_values = {
    'shield': 3,
    'obsidian sword': 3,
    'dodge skill': 1,
    'kick skill': 1,
    'bow and arrow': 3,
    'spear': 3,
    'poison': 3,
    'deep breath skill': 1,
    'glass cannon': 3,
    'shuriken': 3,
    'lightning bolt': 3,
    'healing potion': 3,
    'whip': 3,
    'boomerang': 3
}


# clears the screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


#   Start menu
def begin_playing():
    # Start condition for while loop
    x = True

    # Loop for testing user input to start playing the game
    while x:

        start = input('Would you like to play the game? (y/n)\n> ')

        # Start the game and break the input test loop
        if start.lower() == 'y':
            input("Very well, let's begin. Press the ENTER key to continue.\n")
            x = False

        # If the user decides not to play the game
        elif start.lower() == 'n':
            print('Okay, maybe some other time.')
            x = False

            global begin
            begin = False
            return x, begin

        # If the user inputs something other than y or n
        else:
            print('Invalid input. Please try again.')


# Intro message
def intro():
    print("\n\n\tWelcome to my game.\n\n\
        In this game, you will be exploring various rooms. In some of the rooms, there will be an item, which you can retrieve.\n\n\
        A boss will be hiding in one of the rooms, of which you will not be informed. In order to win this game, you must defeat the boss.\n\n\
        When you encounter the boss, you will have to fight him. Use the 'use' command to initiate a battle sequence.\n\n\
        The boss will return fire. You may retreat at any time once your HP drops below 25. There are two items in this game to help with healing.\n\n\
        These are the only two items that may be used both in and out of battle.\n\n\
        Tip: Use the 'info' command to learn about your items to know how to use them best.\n\n\
        Moves:\n\
        \t'go {direction}' (travel north, south, east, or west)\n\
        \t'get {item}' (add nearby item to inventory)\n\
        \t'use {item}' (put the item you specify into effect (only available during battle for most items))\n\
        \t'info {item}' (give the attack value, defense value, and special effect for the item you specify)\n\
        \t'retreat' (retreats from battle and allows you to pass through freely (only available when your HP is below 25%))\n\
        \t'quit' (exits the game)\n\
        \t'HP' (shows the HP values for you and the boss)\n\
        \tYou can see the this moves menu at any time by saying 'help'")


    begin_playing()


# Formats the display of items in the current room each turn
def item_format():
    if nearby_item is not None and nearby_item not in inventory:

        # List of vowels
        vowels = ['a', 'e', 'i', 'o', 'u']

        # Plural
        if nearby_item[-1] == 's':
            print(f'You see {nearby_item}')

        # Starts with vowel
        if nearby_item[0] in vowels:
            print(f'You see an {nearby_item}')

        # Starts with consonant
        else:
            print(f'You see a {nearby_item}')

    else:
        print('There is no item nearby.')


# if timed escape engages
def escape(current_room):

    # assigns the exit to a random room
    random_room = random.choice(list(rooms.keys()))
    rooms[random_room]['escape'] = 'exit'

    # defines the amount of time left to escape
    time_left = 60

    run = True
    last_move = f'You have defeated the boss, but he was able to trigger the emergency defense system before he died. You have {time_left} seconds to escape the dungeon. Good luck!'

    while run:

        # start the clock
        start_time = time.time()

        # if you still have time left
        if time_left > 0:
        
            clear_screen()

            # Basic info to display to user every turn
            print(f"You have {int(time_left)} seconds to escape!\nYou are in the {current_room}\nInventory : {inventory}\n{'-' * 25}")
            print(last_move)
            
            user_input = input('Enter your move:\n> ')
        
            move = user_input.split(' ')
            action = move[0].lower()

            item = ' '.join(move[1:]).lower()

            global end_game

            # moving between rooms
            if action == 'go':
                direction = move[1].lower()
                
                try:
                    current_room = rooms[current_room][direction]
                    last_move = f'You travel {direction}'

                    # lets user know if the escape is nearby
                    if 'escape' in rooms[current_room].keys():
                        last_move = 'You see the exit!'

                    # showing remaining time
                    end_time = time.time()
                    time_left += (start_time - end_time)

                except:
                    last_move = 'You cannot travel in that direction'

                    end_time = time.time()
                    time_left += (start_time - end_time)

            # if the user tries to collect items
            elif action == 'get':
                last_move = 'Collecting items is not a worthwhile use of your time. You must escape!'

                end_time = time.time()
                time_left += (start_time - end_time)

            elif action == 'use':
                # if the user uses the exit
                if item == 'exit':
                    print(f'You escaped the dungeon and beat the game! Congratulations!')
                    run = False
                    end_game = True

                # if the user tries to use items
                else:
                    last_move = 'Using items will not help you escape the dungeon.'

                    end_time = time.time()
                    time_left += (start_time - end_time)

            # if the user has forgotten the movement commands
            elif action == 'help':
                last_move = moves

                end_time = time.time()
                time_left += (start_time - end_time)

            # if the user wants info on something
            elif action == 'info':
                last_move = 'Asking for info is not worth your time. Escape!'

                end_time = time.time()
                time_left += (start_time - end_time)

            # if the user decides to quit the game
            elif action == 'quit':
                run = False
                end_game = True

            
            # if the user enters invalid input
            else: 
                last_move = 'Invalid command'

                end_time = time.time()
                time_left += (start_time - end_time)

        # if the user runs out of time
        else: 
            print('You have run out of time and lost the game! Better luck next time!')
            run = False
            end_game = True

            
      
# Quits the game
def quit_game():
    if action.lower() == 'quit':
        global begin
        begin = False
        return begin


# Carries out battle sequence
def battle(inventory, current_room):

    start = True
    bossHP = HP_values['boss HP']
    userHP = HP_values['user HP']
    last_move = "You found the boss! You always initiate the round of attacks with the 'use' command. The boss will counterattack.\nDon't forget that you can use the 'info' command to see the attack, defense, and effect values for your items."
    
    # random selection lists
    boss_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    crit_chance = [1, 2, 3, 4]
    dmg_def_range = [3, 4, 5, 6, 7]
    escape_dungeon = [1, 2]

    # break condition
    global end_game

    # starting the battle loop
    while start:

        # if the user has items left
        if len(inventory) > 0:

            # making sure the battle should contine
            if userHP > 0 and bossHP > 0:

                # clears screen
                clear_screen()

                # Basic info to display to user every turn
                print(f"You are in the {current_room}\nInventory : {inventory}\n{'-' * 25}")
                print(last_move)
                
                user_input = input('Enter your move:\n> ')
            
                move = user_input.split(' ')
                action = move[0].lower()

                item = ' '.join(move[1:]).lower()
                
                # default damage value
                attack_value = 0

                last_move = 'The boss has attacked. You may attack or defend.'
                
                # if the user is trying to use an item
                if action == 'use':
                    # defining the item being used
                    used_item = ' '.join(move[1:]).lower()

                    # if the item trying to be use has not been collected
                    if used_item not in inventory:
                        last_move = 'You do not have that item.'

                    # runs through each item testing if that's the item being used
                    else:

                        if used_item == 'shield':

                            # the amount of damage the boss will deal
                            boss_attack_value = random.choice(boss_values)
                                
                            # removing the used item from the inventory
                            inventory.remove('shield')
                                
                            # making sure the boss's damage dealt can't be negative
                            if boss_attack_value > 10:
                                    boss_attack_value = boss_attack_value - 10
                            elif boss_attack_value <= 10:
                                    boss_attack_value = 0 

                            # changing the HP value
                            userHP = userHP - boss_attack_value

                            # updating the HP values
                            HP_values['boss HP'] = bossHP
                            HP_values['user HP'] = userHP

                            # action message
                            last_move = f"You used the {used_item}. You dealt {attack_value} damage. The boss dealt {boss_attack_value} damage.\nYour HP is {userHP}. The boss's HP is {bossHP}."

                        elif used_item == 'obsidian sword':

                            boss_attack_value = random.choice(boss_values)

                            inventory.remove(used_item)

                            # defining crit
                            crit = random.choice(crit_chance)

                            # if crit chance is being used
                            if crit == 1:
                                attack_value = 30
                            else:
                                attack_value = 15

                            # updating HP values respectively
                            bossHP = bossHP - attack_value
                            userHP = userHP - boss_attack_value

                            # saving HP values
                            HP_values['boss HP'] = bossHP
                            HP_values['user HP'] = userHP

                            # action message
                            last_move = f"You used the {used_item}. You dealt {attack_value} damage. The boss dealt {boss_attack_value} damage.\nYour HP is {userHP}. The boss's HP is {bossHP}."

                        elif used_item == 'dodge skill':

                            boss_attack_value = random.choice(boss_values)
                            defense_value = random.choice(dmg_def_range)

                            if boss_attack_value > defense_value:
                                    boss_attack_value = boss_attack_value - defense_value
                            else:
                                    boss_attack_value = 0

                            bossHP = bossHP - attack_value
                            userHP = userHP - boss_attack_value

                            HP_values['boss HP'] = bossHP
                            HP_values['user HP'] = userHP

                            last_move = f"You used {used_item}. You dealt {attack_value} damage. The boss dealt {boss_attack_value} damage.\nYour HP is {userHP}. The boss's HP is {bossHP}."


                        elif used_item == 'kick skill':

                            boss_attack_value = random.choice(boss_values)
                            attack_value = random.choice(dmg_def_range)

                            bossHP = bossHP - attack_value
                            userHP = userHP - boss_attack_value

                            HP_values['boss HP'] = bossHP
                            HP_values['user HP'] = userHP

                            last_move = f"You used {used_item}. You dealt {attack_value} damage. The boss dealt {boss_attack_value} damage.\nYour HP is {userHP}. The boss's HP is {bossHP}."

                        elif used_item == 'bow and arrow':

                            inventory.remove(used_item)

                            boss_attack_value = random.choice(boss_values)
                            attack_value = 18

                            bossHP = bossHP - attack_value
                            userHP = userHP - boss_attack_value

                            HP_values['boss HP'] = bossHP
                            HP_values['user HP'] = userHP

                            last_move = f"You used the {used_item}. You dealt {attack_value} damage. The boss dealt {boss_attack_value} damage.\nYour HP is {userHP}. The boss's HP is {bossHP}."

                        elif used_item == 'spear':

                            inventory.remove(used_item)

                            
                            boss_attack_value = random.choice(boss_values)
                            attack_value = 12

                            bossHP = bossHP - attack_value
                            userHP = userHP - boss_attack_value

                            HP_values['boss HP'] = bossHP
                            HP_values['user HP'] = userHP

                            last_move = f"You used the {used_item}. You dealt {attack_value} damage. The boss dealt {boss_attack_value} damage.\nYour HP is {userHP}. The boss's HP is {bossHP}."

                        elif used_item == 'poison':

                            inventory.remove(used_item)

                            boss_attack_value = random.choice(boss_values)
                            attack_value = 20

                            bossHP = bossHP - attack_value
                            userHP = userHP - boss_attack_value

                            HP_values['boss HP'] = bossHP
                            HP_values['user HP'] = userHP

                            last_move = f"You used the {used_item}. You dealt {attack_value} damage. The boss dealt {boss_attack_value} damage.\nYour HP is {userHP}. The boss's HP is {bossHP}."

                        elif used_item == 'deep breath skill':

                            # making sure the user can't raise the HP cap
                            if userHP <= 96:
                    
                                userHP += 4

                                HP_values['user HP'] = userHP

                            elif 96 < userHP <= 99:
                                userHP = 100

                                HP_values['user HP'] = userHP

                            else:
                                last_move = 'Your HP is already full.'

                            
                            boss_attack_value = random.choice(boss_values)

                            bossHP = bossHP - attack_value
                            userHP = userHP - boss_attack_value

                            HP_values['boss HP'] = bossHP
                            HP_values['user HP'] = userHP

                            last_move = f"You used the {used_item}. You dealt {attack_value} damage. The boss dealt {boss_attack_value} damage.\nYour HP is {userHP}. The boss's HP is {bossHP}."

                        elif used_item == 'glass cannon':

                            inventory.remove(used_item)

                            boss_attack_value = random.choice(boss_values)
                            attack_value = 40

                            bossHP = bossHP - attack_value
                            userHP = userHP - boss_attack_value - 15

                            HP_values['boss HP'] = bossHP
                            HP_values['user HP'] = userHP

                            last_move = f"You used the {used_item}. You dealt {attack_value} damage. The boss dealt {boss_attack_value} damage.\nYour HP is {userHP}. The boss's HP is {bossHP}."

                        elif used_item == 'shuriken':

                            inventory.remove(used_item)

                            boss_attack_value = random.choice(boss_values)
                            attack_value = 21

                            bossHP = bossHP - attack_value
                            userHP = userHP - boss_attack_value

                            HP_values['boss HP'] = bossHP
                            HP_values['user HP'] = userHP

                            last_move = f"You used the {used_item}. You dealt {attack_value} damage. The boss dealt {boss_attack_value} damage.\nYour HP is {userHP}. The boss's HP is {bossHP}."

                        elif used_item == 'lightning bolt':

                            inventory.remove(used_item)

                            # defining crit
                            crit = random.choice(crit_chance)

                            # if crit chance is being used
                            if crit == 1:
                                attack_value = 45
                            else:
                                attack_value = 30


                            boss_attack_value = random.choice(boss_values)
                            attack_value = 30

                            bossHP = bossHP - attack_value
                            userHP = userHP - boss_attack_value

                            HP_values['boss HP'] = bossHP
                            HP_values['user HP'] = userHP

                            last_move = f"You used the {used_item}. You dealt {attack_value} damage. The boss dealt {boss_attack_value} damage.\nYour HP is {userHP}. The boss's HP is {bossHP}."

                        elif used_item == 'healing potion':

                            inventory.remove(used_item)

                            userHP += 20

                            boss_attack_value = random.choice(boss_values)

                            bossHP = bossHP - attack_value
                            userHP = userHP - boss_attack_value

                            HP_values['boss HP'] = bossHP
                            HP_values['user HP'] = userHP

                            last_move = f"You used the {used_item}. You dealt {attack_value} damage. The boss dealt {boss_attack_value} damage.\nYour HP is {userHP}. The boss's HP is {bossHP}."

                        elif used_item == 'whip':

                            inventory.remove(used_item)

                            boss_attack_value = random.choice(boss_values)
                            attack_value = 10

                            bossHP = bossHP - attack_value
                            userHP = userHP - boss_attack_value

                            HP_values['boss HP'] = bossHP
                            HP_values['user HP'] = userHP

                            last_move = f"You used the {used_item}. You dealt {attack_value} damage. The boss dealt {boss_attack_value} damage.\nYour HP is {userHP}. The boss's HP is {bossHP}."

                        elif used_item == 'boomerang':

                            boss_attack_value = random.choice(boss_values)
                            attack_value = 6

                            bossHP = bossHP - attack_value
                            userHP = userHP - boss_attack_value

                            HP_values['boss HP'] = bossHP
                            HP_values['user HP'] = userHP

                            last_move = f"You used the {used_item}. You dealt {attack_value} damage. The boss dealt {boss_attack_value} damage.\nYour HP is {userHP}. The boss's HP is {bossHP}."


                        else:
                            last_move = ('Invalid command')

                elif action == 'info':
                    item = ' '.join(move[1:]).lower()

                    if item in rooms:
                        last_move = 'You cannot ask for info about the rooms.'

                    elif item in items: 
                        if item not in inventory:
                            last_move = f'You have not retrieved {item}.'

                        else:
                            last_move = items[item]
                
                elif action == 'go':
                    last_move = "You may not leave the battle."
                
                elif action == 'get':

                    item = ' '.join(move[1:]).lower()
                        
                    try:
                        if item == rooms[current_room]['Item']:

                            if item not in inventory:

                                 # if the item has yet to be collected the three time maximum
                                if item in item_values and item_values[item] > 0 :
                                    # updating the number of times the item has been collected
                                    item_values[item] = item_values[item] - 1
                            
                                    # adding the collected item to inventory and letting the user know the action has been completed
                                    inventory.append(rooms[current_room]['Item'])
                                    last_move = f'You retrieved the {item}!'
                        
                                # if the item has already been collected the maximum number of allowed times
                                elif item in item_values and item_values[item] < 1:
                                    last_move = 'You have already collected this item three times. You may not collect it again.'

                            else:
                                    last_move = f'You already have the {item}.'

                        else:
                                last_move = f"Can't find {item}."

                    except:
                            last_move = f"Can't find {item}."

                # if the user wishes to quit the game
                elif action == 'quit':
                    start = False
                    end_game = True
    

                # if the user wishes to retreat from battle
                elif action == 'retreat':
                    if userHP <= 25:
                        print('You have retreated from battle.')

                        start = False
                    else:
                        last_move = 'You cannot retreat from battle unless your HP is at or below 25'

            # if the user dies in battle
            elif userHP <= 0: 
                print('You ran out of HP, you have lost the game.')
                start = False
                end_game = True
                

            # if the user kills the boss
            elif bossHP <= 0:
                # 50% chance to engage the timed escape
                escape_chance = random.choice(escape_dungeon)

                # victory without timed escape
                if escape_chance == 1:
                    print('Congratulations! You have won the game!')
                    start = False
                    end_game = True
                    
                    
                # engage timed excape
                elif escape_chance == 2:
                    escape(current_room)
                    start = False

        else:
            print('You ran out of items and lost the game. Better luck next time!')
            start = False
            end_game = True

# assigns the user to a random room
random_room_user = random.choice(list(rooms.keys()))
    
# assigns the boss to a random room
random_room_boss = random.choice(list(rooms.keys()))
rooms[random_room_boss]['boss'] = 'Resident Evil'

# List to track inventory
inventory = []

# Tracks current room and assigns the starting room
current_room = random_room_user

# Result of last move
last_move = ""

# Gameplay loop start condition
begin = True

# break condition
end_game = False

intro()

# Gameplay loop (one iteration per turn)
while begin:
    # clears screen
    clear_screen()

    # Basic info to display to user every turn
    print(f"You are in the {current_room}\nInventory : {inventory}\n{'-' * 25}")

    # Display the outcome of the user's last move
    print(last_move)

    # Indicate if there's an item in the room
    if 'Item' in rooms[current_room].keys():

        nearby_item = rooms[current_room]['Item']

        item_format()

        # boss encounter
        if 'boss' in rooms[current_room].keys():
            if len(inventory) > 4:
                battle(inventory, current_room)

            if end_game == True:
                break

        # getting input from the user and converting it to usable values
        user_input = input('Enter your move:\n> ')
        move = user_input.lower().split(' ')

        action = move[0].lower()

        # Changing current room
        if action == 'go':
            # defining the direction the user wishes to travel
            direction = move[1].lower()
            
            # trying to go the specified direction
            try:
                current_room = rooms[current_room][direction]
                last_move = f'You travel {direction}'

            # can't go the specified direction
            except:
                last_move = 'You cannot travel in that direction.'
            

        # Picking items up
        elif action == 'get':
            # defining the item the user wants to collect
            item = ' '.join(move[1:]).lower()

            # trying to pick up the item
            try:
                # making sure the item is in the room the user is in
                if item == rooms[current_room]['Item']:

                    # making sure the item hasn't already been collected
                    if item not in inventory:
                       
                        # if the item has yet to be collected the three time maximum
                        if item in item_values and item_values[item] > 0 :
                            # updating the number of times the item has been collected
                            item_values[item] = item_values[item] - 1
                           
                            # adding the collected item to inventory and letting the user know the action has been completed
                            inventory.append(rooms[current_room]['Item'])
                            last_move = f'You retrieved the {item}!'
                        
                        # if the item has already been collected the maximum number of allowed times
                        elif item in item_values and item_values[item] < 1:
                            last_move = 'You have already collected this item three times. You may not collect it again.'

                    # if the item has already been collected
                    else:
                        last_move = f'You already have the {item}.'

                # if the item trying to be collected is in a different room
                else:
                    last_move = f"Can't find {item}."

            # if there is a typo in their command
            except:
                last_move = f"Can't find {item}."

        # using items
        elif action == 'use':
            # defining the item being used in a way that is readable
            used_item = ' '.join(move[1:]).lower()

            # making sure the item is one of the two allowed to be used outside of battle
            if item == 'deep breath skill':
                # defining HP in a readable way
                userHP = HP_values['user HP']

                # updating HP value
                if userHP <= 96:
                
                    userHP += 4

                    # updates user HP
                    HP_values['user HP'] = userHP

                    # prints success message to the user
                    last_move = f"You used the {used_item}. You healed 4 HP. Your HP is {userHP}."

                # if the user tries to raise the HP cap
                elif 96 < userHP <= 99:
                    userHP = 100

                    HP_values['user HP'] = userHP

                    last_move = f'You used the {used_item}. Your HP is {userHP}.'

                # if the user tries to raise the HP cap
                else:
                    last_move = 'Your HP is already full.'

            # making sure the item is allowed
            elif item == 'healing potion':
                # making sure the item is in the inventory
                if item in inventory:
                    # try to remove item from inventory and raise the HP
                    # this item is allowed to raise the HP cap
                    try:
                        inventory.remove(used_item)

                        userHP = HP_values['user HP']
                        
                        userHP += 20 

                        HP_values['user HP'] = userHP

                        last_move = f"You used the {used_item}. Your HP is {userHP}."

                    # avoiding can't remove item from inventory error
                    except:
                        last_move = 'invalid command'

                # if the user enters invalid input
                else:
                    last_move = 'Invalid command.'

            # if the user enters invalid input
            else:
                last_move = "Invalid command."

        # Info command
        elif action == 'info':
            # defining the item
            item = ' '.join(move[1:]).lower()

            # if the user is trying to collect info about a room
            if item in rooms:
                last_move = 'You cannot ask for info about the rooms.'

            # if the user is asking for info about an item
            elif item in items: 
                if item not in inventory:
                    last_move = f'You have not retrieved {item}.'

                else:
                    last_move = items[item]

            # if the user wishes to see the HP values
            elif item == 'hp':
                last_move = HP_values

            # if the user enters invalid input
            else: 
                last_move = 'Invalid command.'   

        # if the user wishes to see the moves they can make
        elif action == 'help':
                last_move = moves 

        elif action == 'hp':
                last_move = HP_values

        # Exit the game at any time
        elif action == 'quit':
            quit_game()

        # If the user has not entered a valid move
        else:
            last_move = 'Invalid command'