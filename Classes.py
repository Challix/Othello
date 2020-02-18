import pygame as pg        

pg.init()
COLOR_INACTIVE = pg.Color(50,50,50)
COLOR_ACTIVE = pg.Color(0,0,0)
FONT = pg.font.Font('freesansbold.ttf', 32)

class Board:
    '''
        handles all board operations
    '''
    def __init__(self):
        print('initialized')
        self.board = self.build_grid()
    
    def build_grid(something):
        '''
            Creates a 2 dimensional array.
        '''
        grid = []
        for row in range(8):
            # Add an empty array that will hold each cell in this row
            grid.append([])
            for column in range(8):
                grid[row].append(0)  # Append a cell
        grid[3][3] = 1
        grid[3][4] = 2
        grid[4][3] = 2
        grid[4][4] = 1
        return grid
    
    def show_valid(self, player):
        '''
            Displays valid moves
        '''
        for row,line in enumerate(self.board):
            for column,cell in enumerate(line):
                if cell == 3:
                    self.board[row][column] = 0
        
        for row,level in enumerate(self.board):
            for column,cell in enumerate(level):                
                if cell == player:
                    self.check_avaliable(player,row,column,'left','down')
                    self.check_avaliable(player,row,column,'left','up')
                    self.check_avaliable(player,row,column,'right','down')
                    self.check_avaliable(player,row,column,'right','up')
                    self.check_avaliable(player,row,column,None,'down')
                    self.check_avaliable(player,row,column,None,'up')
                    self.check_avaliable(player,row,column,'left')
                    self.check_avaliable(player,row,column,'right')

#        for row in self.board:
#            print(row)
        
    def check_avaliable(self,player,row,column,hor=None,vert=None):
        '''
            allows to check every direction in grid and set 
        '''
        check = 5
        count = 0
        while check != player or 0 or 3:
            if hor == 'left' and vert == 'down':
                row += 1
                column -= 1
            
            if hor == 'left' and vert == 'up':
                row -= 1
                column -= 1
                
            if hor == 'right' and vert == 'down':
                row += 1
                column += 1
                
            if hor == 'right' and vert == 'up':
                row -= 1
                column += 1
                
            if hor == 'left' and vert == None:
                column -= 1
                
            if hor == 'right' and vert == None:
                column += 1
                
            if hor == None and vert == 'down':
                row += 1
                
            if hor == None and vert == 'up':
                row -= 1
            
            if 0 > row or row > 7 or 0 > column or column > 7:
                break

            print('check: ',row,column)
            check = self.board[row][column]
            if check != player and check != 0 and check != 3:
                count += 1
            if check == 3:
                break
            if count > 0 and check == 0:
                print('count:',count)
                print('possible pts',row,column,'player',player)
                self.board[row][column] = 3
                break    
            if count == 0 and check == 0:
                break
            
            
            
    def check_valid(self,player,row,column):
        '''
            checks click if valid move
        '''
        if 0 > row or row > 7 or 0 > column  or column > 7:
            return False
        if self.board[row][column] == 3:
            if player == 1:
                self.board[row][column] = 1
            elif player == 2:
                self.board[row][column] = 2
            return True
        else:
            print('not valid')
            return False
    
    def tile_flip(self,player,row,column):
        '''
            flips the required tiles after a move
        '''
        self.set_tile_flip(player,row,column,'left','down')
        self.set_tile_flip(player,row,column,'left','up')
        self.set_tile_flip(player,row,column,'right','down')
        self.set_tile_flip(player,row,column,'right','up')
        self.set_tile_flip(player,row,column,None,'down')
        self.set_tile_flip(player,row,column,None,'up')
        self.set_tile_flip(player,row,column,'left')
        self.set_tile_flip(player,row,column,'right')
        
    def set_tile_flip(self,player,row,column,hor=None,vert=None):
        '''
            checks every direction if tile flip is required
        '''
        check = 5
        points = []
        while check != player or 0 or 3:
            if hor == 'left' and vert == 'down':
                row += 1
                column -= 1
            
            if hor == 'left' and vert == 'up':
                row -= 1
                column -= 1
                
            if hor == 'right' and vert == 'down':
                row += 1
                column += 1
                
            if hor == 'right' and vert == 'up':
                row -= 1
                column += 1
                
            if hor == 'left' and vert == None:
                column -= 1
                
            if hor == 'right' and vert == None:
                column += 1
                
            if hor == None and vert == 'down':
                row += 1
                
            if hor == None and vert == 'up':
                row -= 1
            
            if 0 > row or row > 7 or 0 > column  or column > 7:
#                print('index break')
                break

#            print(row,column)
            check = self.board[row][column]
#            print('check',check)
#            print('player',player)
            if check == player or check == 0 or check == 3:
                points.append((row,column))
#                print('check broke')
                break
            else:
                points.append((row,column))
        if points:
#            print('thingy',points)
#            print('last point',points[-1])
#            print('board tile',self.board[points[-1][0]][points[-1][1]])
            if self.board[points[-1][0]][points[-1][1]] == player:
                for point in points:
#                    print(point)
                    row = point[0]
                    column = point[1]
#                    print(row,column)
#                    print('tile color', player)
                    self.board[row][column] = player            

    def update_score(self):
        '''
            updates scoreboard
        '''
        white = 0
        black = 0
        for row in self.board:
            for cell in row:
                if cell == 1:
                    black += 1
                elif cell == 2:
                    white += 1
        return black, white
                    
    def check_win(self):
        '''
            checks for Game Over
        '''
        count = 0
        white = 0
        black = 0
        for row in self.board:
            for cell in row:
                if cell == 0 or 3:
                    count += 1
                if cell == 1:
                    black += 1
                elif cell == 2:
                    white == 1
        if count > 0:
            return False
        else:
            if white < black:
                return 1
            else:
                return 2

        
class InputBox:
    '''
        Handles drawing input boxes
    '''
    def __init__(self, x, y, w, h, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pg.KEYDOWN:
#            print(self.text)
            if self.active:
                if event.key == pg.K_RETURN: 
                    text = self.text
                    self.text = ''
                    self.txt_surface = FONT.render(self.text, True, self.color)
                    return (text)
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pg.draw.rect(screen, self.color, self.rect, 3)
        
class Button:
    '''
        Handles drawing buttons
    '''
    def __init__(self, x, y, w, h, s, text='BUTTON'):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = (pg.font.Font('freesansbold.ttf', s)).render(text, True, (255,255,255))
        self.active = False
        
    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            # If the user clicked on the button rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
            return self.active
            
    def draw(self, screen):
        # Blit the rect.
        pg.draw.rect(screen, self.color, self.rect, 0)
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+7))