#import
import pygame
import json

pygame.init()

#variables
game_height = 800
game_width = 800
running = True

pieces_per_person = ["pawn", "pawn", "pawn", "pawn", "pawn", "pawn", "pawn", "pawn",
                     "rook", "knight", "bishop", "queen", "king", "bishop", "knight", "rook"]


#objects
class Piece(pygame.sprite.Sprite):
    def __init__(self, posx, posy, colour, type, id):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(f"Resources\\images\\pieces\\{colour}_{type}.png")
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = posx, posy
        self.rect.size = (100,100)
        self.image = pygame.transform.scale(self.image, (100,100))
        self.name = f"{colour} {type}"
        self.id = id

    def move(self, pos):
        self.rect.x = pos[0]-50
        self.rect.y = pos[1]-50

class Cursor(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([15, 15])
        self.rect = self.image.get_rect()
        self.x, self.y = x, y
        self.rect.x, self.rect.y = x, y
        self.dragging = None

    def update(self):
        pos = pygame.mouse.get_pos()
        self.x = pos[0]
        self.y = pos[1]
        self.rect.x, self.rect.y = self.x, self.y


### Square object ###
### Piece objects ###




#build game
class Main:
    def __init__(self):
        self.ticks = 120
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((game_width, game_height))
        self.pieces = pygame.sprite.Group()
        self.cursor = pygame.sprite.Group()
        self.c = Cursor(0,0)
        self.cursor.add(self.c)
# build loop
        self.draw_pieces()


#main loop
        while running:
            self.events()
            self.c.update()
            self.clock.tick(self.ticks)
            self.screen.blit(pygame.image.load("Resources\\images\\board.png"),(0,0))
            self.move_piece()
            self.pieces.draw(self.screen)
            pygame.display.update()

            pass

    def events(self):
        e = pygame.event.poll()
        if e.type == pygame.QUIT:
            pygame.quit()
        if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
            if self.c.dragging == None:
                try:
                    self.c.dragging = pygame.sprite.spritecollide(self.c, self.pieces, False)[0]
                except:
                    pass
            else:
                self.c.dragging = None

    def draw_pieces(self):
        x = 0
        y = 600
        id = 0
        for colour in ["white", "black"]:
            if colour == "white":
                x = 0
                y = 600
            else:
                x = 0
                y = 100
            for piece in pieces_per_person:
                self.pieces.add(Piece(x, y, colour, piece, id))
                id += 1
                x += 100
                if x >= 800:
                    x = 0
                    if colour == "white":
                        y += 100
                    else:
                        y -= 100

    def move_piece(self):
        if self.c.dragging != None:
            self.c.dragging.move(pygame.mouse.get_pos())