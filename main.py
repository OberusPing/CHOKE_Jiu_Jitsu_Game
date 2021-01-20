from player import *
from npc import *
from button import *

# Initialize the pygame
pygame.init()

# Create the screen
windowWidth = 1000
windowHeight = 800
screen = PG_Window_UI(windowWidth, windowHeight)

# Set the font formats for text in the game
title_font = pygame.font.SysFont('lucidasanstypewriteroblique', 40)
button_font = pygame.font.SysFont('lucidasanstypewriteroblique', 20)

# Title and Icon
pygame.display.set_caption("CHOKE")
icon = pygame.image.load('kimono.png')
pygame.display.set_icon(icon)


# Player Turn Function
def player_turn(player, npc):
    running = True
    while running:
        # Clear the screen, and get all events
        screen.clear(255, 255, 238)
        events = pygame.event.get()
        handleEvents(events, screen)

        positionImg = pygame.image.load(globalPositions[player.current_position][IMAGE])
        screen.window.blit(positionImg, (40, 400))

        # Assign buttons for every move available to the player, depending on the current position
        buttons = [
            Button(move, (100, 100 + (globalPositions[player.current_position][MOVES].index(move) + 1) * 70),
                   outline=False)
            for move
            in
            globalPositions[player.current_position][MOVES]]

        # Draw move prompt text on the screen
        blit_text(screen.window,
                  player.name + " is now in " + player.current_position + " and has the following moves to choose " 
                                                                          "from: ", (100, 20), button_font)



        # DRAWING THE BUTTONS
        for button in buttons:
            button.render(screen.window)
            if button.clicked(events):
                print(f"button at position: {button.position} was  clicked")
                player.current_move = globalPositions[player.current_position][MOVES][buttons.index(button)]
                player.check_success(
                    globalMoves[globalPositions[player.current_position][MOVES][buttons.index(button)]],
                    npc)
                npc.turn = True
                running = False

        screen.update()


# Display the result of the player's turn
def player_after_move(player, npc):
    running = True
    while running:
        screen.clear(255, 255, 238)
        events = pygame.event.get()
        handleEvents(events, screen)

        blit_text(screen.window, player.name + " attempted to perform " + player.current_move, (100, 40), button_font)

        if player.last_roll >= globalMoves[player.current_move][DC]:
            blit_text(screen.window, player.name + " succeeded and is now in " + player.current_position, (100, 60),
                      button_font)
        else:
            blit_text(screen.window, player.name + " failed and is still in " + player.current_position, (100, 60),
                      button_font)

        next_button = Button('Next Turn', (70, 120), outline=False)
        next_button.render(screen.window)

        positionImg = pygame.image.load(globalPositions[player.current_position][IMAGE])
        screen.window.blit(positionImg, (40, 400))

        if next_button.clicked(events):
            if player.current_position == 'Submission':
                submission(player, npc)
            running = False


        pygame.display.update()


# NPC Turn to perform a move
def npc_turn(player, npc):
    running = True
    while running:
        # Set up the screen and events handler
        screen.clear(255, 255, 238)
        events = pygame.event.get()
        handleEvents(events, screen)

        if npc.turn:
            npc.npc_mechanic(player)

        if npc.last_roll >= globalMoves[npc.current_move][DC]:
            blit_text(screen.window, npc.name + " attempted " + npc.current_move + " and passed the DC!", (100, 60),
                      button_font)
            blit_text(screen.window,
                      npc.name + " is now in " + npc.current_position, (100, 90), button_font)
            blit_text(screen.window, player.name + " is now in " + player.current_position, (100, 120), button_font)

        else:
            blit_text(screen.window, npc.name + " attempted " + npc.current_move + " and failed to pass the DC!",
                      (100, 60), button_font)
            blit_text(screen.window,
                      npc.name + " is still in " + npc.current_position, (100, 90), button_font)
            blit_text(screen.window, player.name + " is still in " + player.current_position, (100, 120), button_font)

        next_button = Button('Next Turn', (70, 160), outline=False)
        next_button.render(screen.window)

        positionImg = pygame.image.load(globalPositions[npc.current_position][IMAGE])
        screen.window.blit(positionImg, (40, 400))


        if next_button.clicked(events):
            if npc.current_position == 'Submission':
                submission(player, npc)
            running = False


        # Update the screen
        pygame.display.update()


# Main Menu
def main_menu():
    while True:
        # Fill the screen with colour
        screen.clear(255, 255, 238)

        # Text of the game
        draw_text('CHOKE: A Jiu-Jitsu Adventure', title_font, (0, 0, 0), screen.window, 20, 20)

        events = pygame.event.get()
        handleEvents(events, screen)

        # Button to start the game
        start_button = Button('Start Game', (70, 120), outline=False)
        start_button.render(screen.window)

        # Check if Start Button was clicked
        if start_button.clicked(events):
            game()

        # Update the screen
        pygame.display.update()

def submission(player, npc):
    running = True
    while running:
        screen.clear(255, 255, 238)
        events = pygame.event.get()
        handleEvents(events, screen)

        if player.current_position == 'Submission':
            blit_text(screen.window, player.name + ' submitted ' + npc.name + '!', (100,60), button_font)

        elif npc.current_position == 'Submission':
            blit_text(screen.window, npc.name + ' submitted ' + player.name + '!', (100,60), button_font)

        play_again = Button('Play Again', (70, 120), outline=False)
        play_again.render(screen.window)

        if play_again.clicked(events):
            game()

        pygame.display.update()

# Game loop
def game():
    player = Player('Gordon')
    npc = Npc('Keenan')

    while True:
        player_turn(player, npc)
        player_after_move(player, npc)
        if npc.turn:
            npc_turn(player, npc)

main_menu()
