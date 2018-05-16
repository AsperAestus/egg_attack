#!/bin/python
# ***** BEGIN GPL LICENSE BLOCK *****
# 
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# Contributor(s): "NaMoogly"
#
# ***** END GPL LICENSE BLOCK *****
import pygame
import time
from math import *
pygame.font.init()
pygame.init()

screen_width = 512
screen_height = 512

win = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Egg Attack")


#grass
bg = pygame.image.load('images/bg.png')

#font
myfont = pygame.font.SysFont('Times New Roman', 18)

#endscreen
end1 = pygame.image.load('images/end1.png')
end2 = pygame.image.load('images/end2.png')
gameover = False
gameover2 = False

#nest
nest = pygame.image.load('images/egg_nest.png')
nest_xpos = 224
nest_ypos = 224

flames = []

class cutscene(object):
    opening1 = pygame.image.load('images/opening1.png')
    opening2 = pygame.image.load('images/opening2.png')
    opening3 = pygame.image.load('images/opening3.png')
    opening4 = pygame.image.load('images/opening4.png')
    opening5 = pygame.image.load('images/opening5.png')
    opening6 = pygame.image.load('images/opening6.png')

    def __init__(self, width, height, count):
        self.height = height
        self.width = width
        self.count = 1

    def draw(self, win):
        if self.count == 1:
            win.blit(self.opening1, (0,0))
        elif self.count == 2:
            win.blit(self.opening2, (0,0))
        elif self.count == 3:
            win.blit(self.opening3, (0,0))
        elif self.count == 4:
            win.blit(self.opening4, (0,0))
        elif self.count == 5:
            win.blit(self.opening5, (0,0))
        elif self.count == 6:
            win.blit(self.opening6, (0,0))


class enemy(object):
    walk_up = [pygame.image.load('images/thief1_UP.png'), pygame.image.load('images/thief2_UP.png')]
    walk_down = [pygame.image.load('images/thief1_DOWN.png'), pygame.image.load('images/thief2_DOWN.png')]
    walk_left = [pygame.image.load('images/thief1_LEFT.png'), pygame.image.load('images/thief2_LEFT.png')]
    walk_right = [pygame.image.load('images/thief1_RIGHT.png'), pygame.image.load('images/thief2_RIGHT.png')]

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.walk_count = 0
        self.velocity = 1

    def draw(self, win):
        if self.left:
                win.blit(self.walk_left[self.walk_count], (self.x, self.y))
                self.walk_count = abs(self.walk_count - 1)
        elif self.right:
                win.blit(self.walk_right[self.walk_count], (self.x, self.y))
                self.walk_count = abs(self.walk_count - 1)
        elif self.up:
                win.blit(self.walk_up[self.walk_count], (self.x, self.y))
                self.walk_count = abs(self.walk_count - 1)
        elif self.down:
                win.blit(self.walk_down[self.walk_count], (self.x, self.y))
                self.walk_count = abs(self.walk_count - 1)


class projectile(object):

    flame_up = pygame.image.load('images/flame_UP.png')
    flame_down = pygame.image.load('images/flame_DOWN.png')
    flame_left = pygame.image.load('images/flame_LEFT.png')
    flame_right = pygame.image.load('images/flame_RIGHT.png')


    def __init__(self, x, y, width, height, duration):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.left = False
        self.right = False
        self.up = True
        self.down = False
        self.velocity = 10
        self.duration = duration
        self.start_time = time.time()

    def draw(self, win):
        if self.left:
                win.blit(self.flame_left, (self.x, self.y))
        elif self.right:
                win.blit(self.flame_right, (self.x, self.y))
        elif self.up:
                win.blit(self.flame_up, (self.x, self.y))
        elif self.down:
                win.blit(self.flame_down, (self.x, self.y))

class player(object):

    walk_up = [pygame.image.load('images/spyro1_UP.png'), pygame.image.load('images/spyro2_UP.png')]
    walk_down = [pygame.image.load('images/spyro1_DOWN.png'), pygame.image.load('images/spyro2_DOWN.png')]
    walk_left = [pygame.image.load('images/spyro1_LEFT.png'), pygame.image.load('images/spyro2_LEFT.png')]
    walk_right = [pygame.image.load('images/spyro1_RIGHT.png'), pygame.image.load('images/spyro2_RIGHT.png')]

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.left = False
        self.right = False
        self.up = True
        self.down = False
        self.walk_count = 0
        self.velocity = 5

    def draw(self, win):
        if self.left:
                win.blit(self.walk_left[self.walk_count], (self.x, self.y))
                self.walk_count = abs(self.walk_count - 1)
        elif self.right:
                win.blit(self.walk_right[self.walk_count], (self.x, self.y))
                self.walk_count = abs(self.walk_count - 1)
        elif self.up:
                win.blit(self.walk_up[self.walk_count], (self.x, self.y))
                self.walk_count = abs(self.walk_count - 1)
        elif self.down:
                win.blit(self.walk_down[self.walk_count], (self.x, self.y))
                self.walk_count = abs(self.walk_count - 1)

def redrawGameWindow():
    win.blit(bg, (0,0))
    win.blit(nest, (nest_xpos, nest_ypos))
    spyro.draw(win)
    for thief in thieves:
        thief.draw(win)
    for flame in flames:
        flame.draw(win)
    win.blit(textsurface,(0,0))
    if gameover == True:
        win.blit(end1, (0,0))
    if gameover2 == True:
        win.blit(end2, (0,0))
    opening.draw(win)
    pygame.display.update()

def distance(p, q):
    return sqrt(pow (p[0] - q[0], 2) + pow (p[1] - q[1], 2))

thieves = []
started = False
last_fire_time = 0
game_start_time = 0
last_scene_time = 0
thief_spawn_time = 0
spyro = player(224, 215, 64, 64)
opening = cutscene(512, 512, 1)
#thief = enemy(224, 0, 64, 64)

#main game loop
run = True
while run:



    pygame.time.delay(20)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and 0.3 + last_scene_time <= time.time():
        last_scene_time = time.time()
        opening.count += 1

    if opening.count >= 7 and not started:
        started = True
        game_start_time = time.time()

    textsurface = myfont.render(str(floor(time.time() - game_start_time)), False, (255, 255, 255))



    if keys[pygame.K_LEFT] and spyro.x > spyro.velocity:
        spyro.x -= spyro.velocity
        spyro.left = True
        spyro.right = False
        spyro.up = False
        spyro.down = False
    elif keys[pygame.K_RIGHT] and spyro.x < screen_width - spyro.width:
        spyro.x += spyro.velocity
        spyro.left = False
        spyro.right = True
        spyro.up = False
        spyro.down = False
    elif keys[pygame.K_UP] and spyro.y > spyro.velocity:
        spyro.y -= spyro.velocity
        spyro.left = False
        spyro.right = False
        spyro.up = True
        spyro.down = False
    elif keys[pygame.K_DOWN] and spyro.y < screen_width - spyro.width:
        spyro.y += spyro.velocity
        spyro.left = False
        spyro.right = False
        spyro.up = False
        spyro.down = True
    else:
        spyro.walk_count = 0

    if keys[pygame.K_SPACE] and 0.1 + last_fire_time <= time.time():
        last_fire_time = time.time()

        flame = projectile(spyro.x, spyro.y, 64, 64, 1)
        flame.left = spyro.left
        flame.right = spyro.right
        flame.up = spyro.up
        flame.down = spyro.down
        flame.velocity = spyro.velocity + 5
        flames.append(flame)

    for flame in flames:
        if distance((256,256),(flame.x, flame.y)) < 32:
            gameover2 = True

        if flame.start_time + flame.duration < time.time():
            flames.remove(flame)
        if flame.left:
            flame.x -= flame.velocity
        elif flame.right:
            flame.x += flame.velocity
        elif flame.up:
            flame.y -= flame.velocity
        elif flame.down:
            flame.y +=flame.velocity


    if started and thief_spawn_time + 5 < time.time():
        thief_spawn_time = time.time()

        #bottom
        thief = enemy(256, 512, 64, 64)
        thief.up = True
        thieves.append(thief)

        #left
        thief = enemy(0, 256, 64, 64)
        thief.right = True
        thieves.append(thief)

        #top
        thief = enemy(256, 0, 64, 64)
        thief.down = True
        thieves.append(thief)

        #right
        thief = enemy(512, 256, 64, 64)
        thief.left = True
        thieves.append(thief)


    for thief in thieves:
        if distance((thief.x, thief.y),(flame.x, flame.y)) < 32:
            thieves.remove (thief)
            continue
        elif distance((256,256),(thief.x, thief.y)) < 32:
            gameover = True

        trajectory_x = (nest_xpos - thief.x)
        trajectory_y = (nest_ypos - thief.y)
        length_trajectory = sqrt(pow(trajectory_x, 2) + pow(trajectory_y, 2))
        trajectory_x /= length_trajectory
        trajectory_y /= length_trajectory
        trajectory_x *= thief.velocity
        trajectory_y *= thief.velocity
        thief.x += trajectory_x
        thief.y += trajectory_y




    redrawGameWindow()

pygame.quit()
