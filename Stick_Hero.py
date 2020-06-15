import pygame
import random
from os import path

# Directories
img_dir = path.join(path.dirname(__file__), 'img')

# Window properties
WIDTH = 800  # px
HEIGHT = 800  # px
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
SKY = (72, 201, 176)
BROWN = (185,122,86)
PLAYER_DIMENSIONS = (30, 50)


class Stick(pygame.sprite.Sprite):
    def __init__(self, posX):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((0, 0))
        self.rect = self.image.get_rect()
        self.screen = screen
        self.spin = 0
        self.stickSize = 100
        self.stickVel = 1
        self.growing = True
        self.condition = True
        self.isFalling = False

    def drawStick(self):
        self.imageCopy = pygame.transform.scale(
            stick_sprite, (5, self.stickSize))
        self.imageCopy = pygame.transform.rotate(self.imageCopy, self.spin)
        self.screen.blit(self.imageCopy, (int(145), int(
            600) - int(self.imageCopy.get_height())))

    def update(self):
        if self.growing == True:
            if self.stickSize > 500:
                pass
            else:
                self.stickSize += self.stickVel
            self.drawStick()
        if self.growing != True:
            self.drawStick()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and self.condition == True:
                self.growing = False
                self.isFalling = True
                while self.isFalling == True:
                    if self.spin <= -90:
                        self.isFalling = False
                    else:
                        self.spin -= 3
                    self.drawStick()
                self.condition = False

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                self.condition = True
        #stick_tam = self.stickSize


class Player(pygame.sprite.Sprite):
    # Sprite for the Player
    def __init__(self, posX):
        pygame.sprite.Sprite.__init__(self)
        player_img = pygame.image.load(path.join(img_dir,'player-sprite.png')).convert_alpha()
        self.image = player_img
        
        # Diminuindo o tamanho da imagem.
        self.image = pygame.transform.scale(player_img, (30, 50))
        
        # Deixando transparente.
        self.image.set_colorkey(BLACK)
        #self.image.fill(BROWN)
        self.rect = self.image.get_rect()
        self.rect.x = posX
        self.rect.y = 550
        self.speedx = 0

    def update(self):
    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.rect.x+=3

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                pass
                
        if self.rect.bottom < 600:
            self.kill()


class Island(pygame.sprite.Sprite):
    def __init__(self, posX):
        pygame.sprite.Sprite.__init__(self)
        self.randnumber = random.randint(50, 150)
        self.image = pygame.Surface((self.randnumber, 200))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.bottomright = (int(posX), int(HEIGHT))
        self.speedy = 0

    def update(self):
        pass


# Initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Stick Hero")
clock = pygame.time.Clock()


stick_sprite = pygame.image.load(
    path.join(img_dir, 'block.png')).convert_alpha()

# Creating groups
all_sprites = pygame.sprite.Group()
island_group = pygame.sprite.Group()
stick_group = pygame.sprite.Group()

# Creating objects and adding to sprite groups
player = Player(110)

for i in [150, 350]:
    island = Island(i)
    all_sprites.add(island)
    island_group.add(island)

stick = Stick(0)
all_sprites.add(player,stick)
stick_group.add(stick)

# Game Loop
running = True
try:

    
    while running:
        # Keep the game running at the right speed
        clock.tick(FPS)

        # Background color
        screen.fill(SKY)

        # If window is closed, game stops
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
          
        hits = pygame.sprite.spritecollide(player, island_group, False)
        if hits:
            pass

        confirmado = pygame.sprite.spritecollide(stick, island_group, False)
        if confirmado:
            pass

        all_sprites.draw(screen)

        # Update
        all_sprites.update()
        pygame.display.update()

finally:
    pygame.quit()
