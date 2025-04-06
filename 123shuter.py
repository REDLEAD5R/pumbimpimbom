#Создай собственный Шутер!

from pygame import *
from random import randint
from time import time as timer
window = display.set_mode((700, 500))
display.set_caption('шутер')
background = transform.scale(image.color(255, 255, 255), (700,500))
window_fill(200, 255, 255)

# mixer.init()
# mixer.music.load('space.ogg')
# mixer.music.play()


# game = True
# clock = time.Clock()
# FPS = 60
# lost = 0
# score = 0

# class GameSprite(sprite.Sprite):
#     def __init__(self, player_image, player_x, player_y, player_speed,size_x,size_y):
#         super().__init__()
#         self.image = transform.scale(image.load(player_image), (size_x,size_y))
#         self.speed = player_speed
#         self.rect = self.image.get_rect()
#         self.rect.x = player_x
#         self.rect.y = player_y
#     def reset(self):
#         window.blit(self.image, (self.rect.x, self.rect.y))
        

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

# player = Player('rocket.png', 5, 395, 5, 80, 100)

# rel_time = False

# num_fire = 0
# finish = False
# while game:
#     for e in event.get():
#         if e.type == QUIT:
#             game = False
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

#     if finish != True:
#         window.blit(background,(0, 0))
#         text_score = font1.render('Счёт:  ' + str(score), 1, (255, 255, 255))
#         window.blit(text_score, (10, 10))

#         text_lose = font1.render('Пропущена: ' + str(lost), 1, (255, 255, 255))
#         window.blit(text_lose, (10, 50))
#         player.update()
#         # cyborg.update()

#         # cyborg.reset()
#         player.reset()

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
#     clock.tick(FPS)
#     display.update()