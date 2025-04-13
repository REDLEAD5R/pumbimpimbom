#Создай собственный Шутер!
bg = (200, 255, 255)
from pygame import *
from random import randint
from time import time as timer
window = display.set_mode((700, 500))
display.set_caption('шутер')



# background.fill(bg)

# mixer.init()
# mixer.music.load('space.ogg')
# mixer.music.play()
speed_x = 5
speed_y = 5
speed = 5
game = True
clock = time.Clock()
FPS = 60
# lost = 0
# score = 0

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_y, player_x, player_speed,size_x, size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x,size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
        
class Wall(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 300:
            self.rect.y += self.speed

class Woll(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_p] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_l] and self.rect.y < 300:
            self.rect.y += self.speed

# class Player(GameSprite):
#     def update(self):
#         keys_pressed = key.get_pressed()
#         if keys_pressed[K_a] and self.rect.x > 5:
#             self.rect.x -= self.speed
#         if keys_pressed[K_d] and self.rect.x < 695 - 80:
#             self.rect.x += self.speed

#     def fire(self):
#         bullet = Bullet('bullet.png', self.rect.centerx, self.rect.top, -5, 10, 100)
#         bullets.add(bullet)

# class Enemy(GameSprite):
#     def update(self):
#         self.rect.y += self.speed
#         global lost
#         if self.rect.y > 500:
#             self.rect.y = 0
#             self.rect.x = randint(50, 650)
#             lost = lost + 1

# class Bullet(GameSprite):
#     def update(self):
#         self.rect.y += self.speed
#         if self.rect.y < 0:
#             self.kill()

# class Asteroid(GameSprite):
#     def update(self):
#         self.rect.y += self.speed
#         global lost
#         if self.rect.y > 500:
#             self.rect.y = 0
#             self.rect.x = randint(50, 650)
#             lost = lost + 1
# bullets = sprite.Group()

# monsters = sprite.Group()

# asteriods = sprite.Group()

walls = sprite.Group()
ball = sprite.Group()
# for i in range(5):
#     monster = Enemy('ufo.png', randint(50, 650), -40, randint(1,5), 50, 50)
#     monsters.add(monster)

# for i in range(5):
#     asteriod = Asteroid('asteroid.png', randint(50, 650), -40, randint(1,5), 50, 50)
#     asteriods.add(asteriod)
    



# font.init()
# font1 = font.Font(None, 36)
# font2 = font.Font(None, 52)

# win = font1.render('YOU WIN!', True, (255, 255, 255))
# lose = font1.render('YOU LOSE!', True, (180, 0, 0))
wall1 = Wall('направо.png', 5, 0, 5, 50, 200)
wall2 = Woll('налево.png', 5, 650, 5, 50, 200)
ball = GameSprite('очень крутой мяч.png', 5, 300, 10, 100, 100)
# player = Player('rocket.png', 5, 395, 5, 80, 100)

# rel_time = False

# num_fire = 0
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
            ball.rect.x += speed_x
            ball.rect.y += speed_y
#         elif e.type == KEYDOWN:
#             if e.key == K_SPACE:
#                 if num_fire < 5 and rel_time == False:
#                     num_fire = num_fire + 1
#                     player.fire()

#                 if num_fire >= 5 and rel_time == False:
#                     last_time = timer()
#                     rel_time = True
            
#                 player.fire()
#                 bullets.add(bullets)

    if finish != True:
        window.fill(bg)
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if ball.rect.y > 450 or ball.rect.y < 0:
                speed_y *= -1

        # window.blit(background,(0, 0))
#         text_score = font1.render('Счёт:  ' + str(score), 1, (255, 255, 255))
#         window.blit(text_score, (10, 10))

#         text_lose = font1.render('Пропущена: ' + str(lost), 1, (255, 255, 255))
#         window.blit(text_lose, (10, 50))
        wall1.update()
        wall2.update()
        ball.update()
#         # cyborg.update()

#         # cyborg.reset()
        wall1.reset()
        wall2.reset()
        ball.reset()

#         # final.reset()
#         monsters.draw(window)
#         monsters.update()

#         asteriods.draw(window)
#         asteriods.update()

#         bullets.update()
#         bullets.draw(window)

#         if rel_time == True:
#             now_time = timer()
#             if now_time - last_time < 3:
#                 reload = font2.render('Роботы переделываются в пули', 1, (150, 0, 0))
#                 window.blit(reload, (260, 460))
#             else:
#                 num_fire = 0
#                 rel_time = False

    collides = sprite.groupcollide(wall1, walll2, ball, True, True)
#         collides = sprite.groupcollide(monsters, bullets, True, True)
#         for c in collides:
#             score = score + 1
#             monster = Enemy('ufo.png', randint(80, 600 -80), -40, randint(1, 5), 80, 50)
#             monsters.add(monster)
        
#         if sprite.spritecollide(player, monsters, False) or lost >= 5:
#             finish = True
#             window.blit(lose, (200, 200))

#         if score >= 10:
#             finish = True
#             window.blit(win, (200, 200))
    clock.tick(FPS)
    display.update()