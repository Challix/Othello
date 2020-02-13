import pygame
from Classes import InputBox
from Classes import Button
from Classes import Board

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 150, 0)
RED = (255, 0, 0)
 
# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 40
HEIGHT = 40
 
# This sets the margin between each cell
MARGIN = 5
WINDOW_SIZE = [365, 420] 

#initializes the board
board = Board()

# Score text
BLACK_SCORE = 'Black\n{}'

WHITE_SCORE = 'White\n{}'

def turn(position,player,p1_pos,p2_pos):
    '''
        structures the turn for each player
    '''
    board.show_valid(player)
    
    
def text_obj(text,font,color):
    '''
        handles text items
    '''
    textSurface = font.render(text,True,color)
    return textSurface, textSurface.get_rect()
    
def intro():
    '''
        gathers user data in beginning
    '''
    WINDOW_SIZE = [365,365]
    input_box = InputBox(80, 200, 140, 40) #(x,y,w,h,text)
    button = Button(122,200,120,32,20,'Start Game') #(x,y,w,h,s,text)
    player1 = ''
    player2 = ''
    pressed = False
    
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            clicked = button.handle_event(event)
            player_data = input_box.handle_event(event)

            if clicked:
                pressed = True
# Input box and screen color
        input_box.update()
        screen.fill(GREEN)
        if pressed:
            input_box.draw(screen)

# Input box text
        if player_data != None:
            if player1 == '':
                player1 = player_data
                player_data = None
                player = '2'
            elif player2 == '':
                player2 = player_data
        else:
            player = '1'
            
        if player1 != '':
            player = '2'
            
        if pressed:
            subtext = pygame.font.Font('freesansbold.ttf',25)
            textSurf, textRect = text_obj("Player {}'s name".format(player), subtext,BLACK)
            textRect.center = ((WINDOW_SIZE[0]/2),(WINDOW_SIZE[1]/4 + 98))
            screen.blit(textSurf,textRect)
        
        if player1 and player2:
            return player1, player2

# Button
        if not pressed:
            button.draw(screen)
# Title text        
        title = pygame.font.Font('freesansbold.ttf',50)
        textSurf, textRect = text_obj('OTHELLO',title,BLACK)
        textRect.center = ((WINDOW_SIZE[0]/2),(WINDOW_SIZE[1]/4 + 30))
        screen.blit(textSurf,textRect)
        
        pygame.display.update()
        pygame.display.flip()
        clock.tick(60)

    
# Initialize pygame
pygame.init()
 
# Set the HEIGHT and WIDTH of the screen
screen = pygame.display.set_mode(WINDOW_SIZE)
 
# Set title of screen
pygame.display.set_caption("Othello")
pygame.display.set_icon(pygame.image.load('othelloPic.PNG'))
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

def main():
    player1, player2 = intro()
    print(player1,player2)
    player = 1
    player_name = player1
    running = True
    validated = False
    
    while running:
        pressed = False

        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                running = False  # Flag that we are done so we exit this loop
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                # User clicks the mouse. Get the position
                pos = pygame.mouse.get_pos()
                # Change the x/y screen coordinates to grid coordinates
                column = pos[0] // (WIDTH + MARGIN)
                row = pos[1] // (HEIGHT + MARGIN)
                print("Click ", pos, "Grid coordinates: ", int(row)+1, int(column)+1)
                print('turn player:',player)
                pressed = board.check_valid(player,row,column)
        
        # changes players for every turn
        if pressed:                        
            print('pressed')
            
            validated = False
            if player == 1:
               print('Black player')
#               print(row,column)
               board.tile_flip(player,row,column)
               board.show_valid(player)
               player = 2
               player_name = player2
            elif player == 2:
               print('White player')
               board.tile_flip(player,row,column)
               board.show_valid(player)
               player = 1
               player_name = player1
               
        # shows valid moves
        if not validated:
            board.show_valid(player)
            validated = True
       
        # Set the screen background
        screen.fill(BLACK)
     
        # Draw the grid
        for level in range(8):
            for column in range(8):
                color = GREEN
                pygame.draw.rect(screen,color,[(MARGIN + WIDTH) * column + MARGIN,
                                  (MARGIN + HEIGHT) * level + MARGIN,WIDTH,HEIGHT])
                if board.board[level][column] == 1:
                    pygame.draw.circle(screen,BLACK,[(MARGIN + WIDTH) * column + MARGIN + 20,
                                  (MARGIN + HEIGHT) * level + MARGIN + 20],15) 
                if board.board[level][column] == 2:
                    pygame.draw.circle(screen,WHITE,[(MARGIN + WIDTH) * column + MARGIN + 20,
                                  (MARGIN + HEIGHT) * level + MARGIN + 20],15) 
                if board.board[level][column] == 3:
                    pygame.draw.circle(screen,RED,[(MARGIN + WIDTH) * column + MARGIN + 20,
                                  (MARGIN + HEIGHT) * level + MARGIN + 20],5)
        
        name_length = len(player_name)
        # Draw player turn text
        if board.check_win():
            print('winner winner')
            winner = board.check_win()
            if winner == 1:
                winner = player1
            else:
                winner = player2
            player_text = pygame.font.Font('freesansbold.ttf',50)
            textSurf, textRect = text_obj("{} Won".format(winner),player_text,WHITE)
            textRect.center = ((WINDOW_SIZE[0]/2),(WINDOW_SIZE[1]/2 + 180))
            screen.blit(textSurf,textRect)
        else:
            player_text = pygame.font.Font('freesansbold.ttf',int(51-(4*name_length)))
            textSurf, textRect = text_obj("{}'s Turn".format(player_name),player_text,WHITE)
            textRect.center = ((WINDOW_SIZE[0]/2),(WINDOW_SIZE[1]/2 + 180))
            screen.blit(textSurf,textRect)
        
        # Draw scoreboard
        black_score,white_score = board.update_score()
        
        player_text = pygame.font.Font('freesansbold.ttf',15)
        textSurf, textRect = text_obj('Black: {}'.format(black_score),player_text,WHITE)
        textRect.center = ((WINDOW_SIZE[0]/8),(WINDOW_SIZE[1]/2 + 180))
        screen.blit(textSurf,textRect)
        
#        player_text = pygame.font.Font('freesansbold.ttf',15)
        textSurf, textRect = text_obj('White: {}'.format(white_score),player_text,WHITE)
        textRect.center = ((WINDOW_SIZE[0]/8 * 7),(WINDOW_SIZE[1]/2 + 180))
        screen.blit(textSurf,textRect)
    
    # Limit to 60 frames per second
        clock.tick(60)
     
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
 
    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
    

if __name__ == '__main__':    
    main()
    pygame.quit()