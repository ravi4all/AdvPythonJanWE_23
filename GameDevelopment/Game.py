import pygame
import random
pygame.init()

width = 1000
height = 600

SCREEN = pygame.display.set_mode((width, height))

RED = 255,0,0
BLUE = 0,0,255
BLACK = 0,0,0
WHITE = 255,255,255


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.image = pygame.Surface((50,50))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = width/2
        self.rect.y = height - 50
        self.moveX = 0

    def update(self):
        keypress = pygame.key.get_pressed()
        if keypress[pygame.K_RIGHT]:
            self.moveX = 5
        elif keypress[pygame.K_LEFT]:
            self.moveX = -5
        else:
            self.moveX = 0

        self.rect.x += self.moveX

    def shoot(self):
        bulletX = self.rect.x + self.image.get_width()/2 - 4
        bulletY = self.rect.y
        bullet = Bullet(bulletX, bulletY)
        bulletGroup.add(bullet)
        all_sprites.add(bullet)


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, width - 50)
        self.rect.y = random.randint(-height, 0)
        self.moveY = random.randint(1,4)

    def update(self, *args):
        self.rect.y += self.moveY
        if self.rect.y > height:
            self.rect.y = random.randint(-height, 0)


class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super(Bullet, self).__init__()
        self.image = pygame.Surface((6,10))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.moveX = -3

    def update(self, *args, **kwargs):
        self.rect.y += self.moveX

        if self.rect.y < 0:
            self.kill()


# Sprite for whole game
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

# Sprite group for player
playerGroup = pygame.sprite.Group()
playerGroup.add(player)

enemyGroup = pygame.sprite.Group()

bulletGroup = pygame.sprite.Group()

for i in range(10):
    enemy = Enemy()
    enemyGroup.add(enemy)
    all_sprites.add(enemy)

FPS = 100
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()

    pygame.sprite.groupcollide(bulletGroup, enemyGroup, True, True)

    SCREEN.fill(WHITE)
    all_sprites.draw(SCREEN)
    all_sprites.update()
    pygame.display.update()
    clock.tick(FPS)
