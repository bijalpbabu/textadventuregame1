import world
from player import Player
from playsound import playsound

def play(level):
    playsound("alexander-nakarada-chase.mp3", False)
    world.load_tiles(level)
    player = Player()
    #These lines load the starting room and display the text
    room = world.tile_exists(player.location_x, player.location_y)
    print(room.intro_text())
    while player.is_alive() and not player.victory:
        room = world.tile_exists(player.location_x, player.location_y)
        room.modify_player(player)
        # Check again since the room could have changed the player's state
        if player.is_alive() and not player.victory:
            print("Choose an action:\n")
            available_actions = room.available_actions()
            for action in available_actions:
                print(action)
            action_input = input('Action: ')
            for action in available_actions:
                if action_input == action.hotkey:
                    player.do_action(action, **action.kwargs)
                    break


if __name__ == "__main__":
   
    for i in range(1, 4):
        play(i)
