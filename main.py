#################
#Devansh
#V4
#this version is the finished polished game where the objective is to survive as long as you can
# there is an invincibility timer of 10 seconds for the player
# the collisions all work
#################

import pygame, random, math, time, asyncio, sys # imports the required libraries
       
        
class Player(pygame.sprite.Sprite):
    # Player is a class, which the player is based created from from

    def __init__(self, y_speed, x_speed, x_pos, y_pos, direction):
        #The init function has a bunch of parameters needed, ,such as y_speed, x_speed, x_pos, y_pos, direction, that are used
        #for the following attributes

        super().__init__()
        #the next chunk of code is for adding sprites to a list, then scaling their sizes + setting up animation code 
        self.sprites = []
        self.sprites.append(pygame.image.load("run1.png").convert_alpha())
        self.sprites.append(pygame.image.load("run2.png").convert_alpha())
        self.sprites.append(pygame.image.load("run3.png").convert_alpha())
        self.sprites.append(pygame.image.load("run4.png").convert_alpha())
        self.sprites[0] = pygame.transform.scale(self.sprites[0], (100, 100))
        self.sprites[1] = pygame.transform.scale(self.sprites[1], (100, 100))
        self.sprites[2] = pygame.transform.scale(self.sprites[2], (100, 100))
        self.sprites[3] = pygame.transform.scale(self.sprites[3], (100, 100))
        self.current_sprite =0
        self.image = self.sprites[self.current_sprite]
        self.is_animating = False
        
        # below are general attributes like speed, health, etc
        self.hp = 100       
        self.y_speed = y_speed
        self.x_speed = x_speed
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.right = False
        self.left = False
        self.flipped = pygame.transform.flip(self.image, False, False)
        self.is_flipped = False
        self.standing = True
        self.direction = 1
        
        #below is setup code for the collision: creating masks, rects (hitboxes), + mana + hp
        self.rect = pygame.Rect(self.x_pos+ 30, self.y_pos + 30, 45, 60)
        self.mana = 100
        self.hp_bar = pygame.Rect(self.x_pos + 5, self.y_pos + 5, self.hp, 10)
        self.mask = pygame.mask.from_surface(self.image.convert_alpha())
        self.mask_image = self.mask.to_surface()
        
    def update(self):
        #the update method contains the code for animation, boundaries, and if the sprite should be flipped or not
        
        #boundary code is below
        if self.x_pos > 1230:
            self.x_pos = 1230
        elif self.x_pos < 0:
            self.x_pos = 0
            
        if self.y_pos > 900:
            self.y_pos = 900
        elif self.y_pos < 0:
            self.y_pos = 0
            
        # the next two lines of code are for updating the position of the hp bar and collision rectangle     
        self.hp_bar = pygame.Rect(self.x_pos + 5, self.y_pos +5, self.hp, 10)   
        self.rect = pygame.Rect(self.x_pos+ 30, self.y_pos + 30, 45, 60)
        
        # below is code for animating the player sprite
        if self.is_animating ==True:
            self.current_sprite += 0.1
            
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_animating = False
                
            self.image = self.sprites[int(self.current_sprite)]
        
    def controls(self):
        
        
        # Below is the code for movement (it uses WASD keys)
        key = pygame.key.get_pressed()
        speed = 7 # distance moved in 1 frame
        
        if key[pygame.K_s]: # down key
            self.is_flipped = True
            self.is_animating = True
            self.y_pos += speed # move down
            self.flipped = pygame.transform.flip(self.image, False, False)
        elif key[pygame.K_w]: # up key
            self.is_flipped = True
            self.is_animating = True
            self.y_pos -= speed # move up
            self.flipped = pygame.transform.flip(self.image, False, False)
        if key[pygame.K_d]: # right key
            self.is_animating = True
            self.x_pos += speed # move right
            self.is_flipped = True
            self.flipped = pygame.transform.flip(self.image, False, False)
            self.right = True
            self.direction = 1
        elif key[pygame.K_a]: # left key
            self.is_animating = True
            self.x_pos -= speed # move left
            self.is_flipped = True
            self.flipped = pygame.transform.flip(self.image, True, False)
            self.left = True
            self.direction = -1
            
    def draw(self, surface):
        #the next line of code is for drawing the hp bar
        pygame.draw.rect(screen, (0,255,0), self.hp_bar)
        
        #below is the code for drawing the player sprite
        # the if statement also checks if the sprite should be flipped or not
        if self.is_flipped == True:
            
            surface.blit(self.flipped, (self.x_pos, self.y_pos))
        else:
            surface.blit(self.image, (self.x_pos, self.y_pos))

class Ice(): # GO TO ITCH.IO AND SEARCH pimen, lots of good projectiles sprites!
    #Ice is a parent class, used for the ICE shard presented in game
    def __init__(self, x_pos, y_pos):
        #the init function requires the x_pos, and y_pos parameters for the attributes below
        
        # below is code that uses a list to store images, and also scales those images to a certain size
        self.sprites = []
        self.sprites.append(pygame.image.load("VFX_1_repeatable1.png").convert_alpha())
        self.sprites.append(pygame.image.load("VFX_1_repeatable2.png").convert_alpha())
        self.sprites.append(pygame.image.load("VFX_1_repeatable3.png").convert_alpha())
        self.sprites.append(pygame.image.load("VFX_1_repeatable3.png").convert_alpha())
        self.sprites.append(pygame.image.load("VFX_1_repeatable4.png").convert_alpha())
        self.sprites.append(pygame.image.load("VFX_1_repeatable5.png").convert_alpha())
        self.sprites.append(pygame.image.load("VFX_1_repeatable6.png").convert_alpha())
        self.sprites.append(pygame.image.load("VFX_1_repeatable7.png").convert_alpha())
        self.sprites.append(pygame.image.load("VFX_1_repeatable8.png").convert_alpha())
        self.sprites.append(pygame.image.load("VFX_1_repeatable9.png").convert_alpha())
        self.sprites[0] = pygame.transform.scale(self.sprites[0], (180,120))
        self.sprites[1] = pygame.transform.scale(self.sprites[1], (180,120))
        self.sprites[2] = pygame.transform.scale(self.sprites[2], (180,120))
        self.sprites[3] = pygame.transform.scale(self.sprites[3], (180,120))
        self.sprites[4] = pygame.transform.scale(self.sprites[4], (180,120))
        self.sprites[5] = pygame.transform.scale(self.sprites[5], (180,120))
        self.sprites[6] = pygame.transform.scale(self.sprites[6], (180,120))
        self.sprites[7] = pygame.transform.scale(self.sprites[7], (180,120))
        self.sprites[8] = pygame.transform.scale(self.sprites[8], (180,120))
        self.sprites[9] = pygame.transform.scale(self.sprites[9], (180,120))
        
        # some animation code
        self.current_sprite =0
        self.image = self.sprites[self.current_sprite]
        
        self.is_animating = True
        self.is_flipped = False
        
        #next chunk of code is for the sprites locations,and angle its shot at (code was borrowed) + hitboxes + acceleration for fun
        self.rect_copy = self.image.get_rect()
        
        self.pos = (x_pos, y_pos)
        #self.pos = pygame.mouse.get_pos()
        mx, my = pygame.mouse.get_pos()
        self.dir = (mx - x_pos, my - y_pos)
        length = math.hypot(*self.dir)
        if length == 0.0:
            self.dir = (0, -1)
        else:
            self.dir = (self.dir[0]/length, self.dir[1]/length) 
        self.angle = math.degrees(math.atan2(-self.dir[1], self.dir[0]))
        self.image_rotate = pygame.transform.rotate(self.image, self.angle)
        self.image_rect = self.image_rotate.get_rect(center = self.pos)
        self.speed = 7
        self.mask = pygame.mask.from_surface(self.image_rotate.convert_alpha())
        self.rect = self.image.get_rect()
        self.mask_image = self.mask.to_surface()
        self.accel = 1
        
    def update(self):
        #update method containing the animation code, and updates the hitbox of the projectile
        self.speed += self.accel
        
        self.pos = (self.pos[0]+self.dir[0]*self.speed, 
                    self.pos[1]+self.dir[1]*self.speed)
            
        self.image_rect = pygame.Rect(self.image_rect[0]+self.dir[0]*self.speed, self.image_rect[1] + self.dir[1]*self.speed, 20, 10)

        if self.is_animating == True:
            self.current_sprite += 0.3
            
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                
                
            self.image = self.sprites[int(self.current_sprite)]
        self.image_rotate = pygame.transform.rotate(self.image, self.angle)
        
    def draw(self, surface):
        #the draw method draws the image of the sprite on the desired surface (surface parameter)

        surface.blit(self.image_rotate, self.image_rect)

class Enemy(pygame.sprite.Sprite):
    #enemy is a parent class that is used for creating the enemies
    def __init__(self, x_pos, y_pos, x_speed, y_speed):
        # init function has x_pos, y_pos, x_speed, y_speed parameters used in attributes
        #below is a couple of setup code for attacj animation and position
        self.attack_bool = False
        self.attack_animation = False
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.x_speed = int(random.randrange(1,3))
        self.y_speed = int(random.randrange(1,3))
        
        # below is the animation code for the enemy (floating npc)
        self.sprites = []       
        self.sprites.append(pygame.image.load("NPC1.png").convert_alpha())
        self.sprites.append(pygame.image.load("NPC2.png").convert_alpha())
        self.sprites.append(pygame.image.load("NPC3.png").convert_alpha())
        self.sprites.append(pygame.image.load("NPC4.png").convert_alpha())
        
        self.sprites[0] = pygame.transform.scale(self.sprites[0], (72,96))
        self.sprites[1] = pygame.transform.scale(self.sprites[1], (72,96))
        self.sprites[2] = pygame.transform.scale(self.sprites[2], (72,96))
        self.sprites[3] = pygame.transform.scale(self.sprites[3], (72,96))
        
        self.current_sprite = 0
        self.direction = 1
        self.image = self.sprites[self.current_sprite]
        self.is_animating = True
        self.is_flipped = False
        
        #below is code for position, hitboxes, attack animation timing, and speed
        self.hp = 70
        self.is_alive = True
        self.hp_bar = pygame.Rect(self.x_pos + 5, self.y_pos - 10, self.hp, 10)
        self.hp_x = 5
        self.hp_y = -10
        self.gui_on = True
        self.image_rect = self.image.get_rect(center = (self.x_pos, self.y_pos))     
        self.speed = 5
        self.mask = pygame.mask.from_surface(self.image.convert_alpha())        
        self.rect = pygame.Rect(self.x_pos+ 30, self.y_pos + 30, 60, 80)
        self.mask_image = self.mask.to_surface()
        self.attack_sprite = 0
        self.attack_sprite_start = 3
        
    def update(self):
        # update method
        
        #this if statement is for checking if the attack animation should start or not
        if self.attack_bool == True:
            self.attack_animation = True       
        else:  
            self.attack_animation = False
            
        # below is code for setting the boundary of the enemies
        if self.x_pos > 1210:
            self.x_pos = 1210
        elif self.x_pos < 0:
            self.x_pos = 0
            
        if self.y_pos > 866:
            self.y_pos = 866
        elif self.y_pos < 0:
            self.y_pos = 0
            
        #this if statement is used to determine if the health bar for the enemy should be drawn or not
        if self.gui_on == True:  
            self.hp_bar = pygame.Rect(self.x_pos + self.hp_x, self.y_pos - self.hp_y, self.hp, 10)
        
        #if statement is used for determingin which direction the enemy should face in (supposed to point towards the player)
        if self.x_pos < player.x_pos:
            self.is_flipped = False
            self.direction = 1
        else:
            self.is_flipped = True
            self.direction = -1
        
        #below is code for updating the positions of the hitboxes
        self.rect = (self.x_pos + 5, self.y_pos + 5, 60, 80)
        self.image_rect = pygame.Rect(self.x_pos + self.speed, self.y_pos + self.speed, self.image_rect[2], self.image_rect[3])
        
        # below is the hefty animation code
        if self.is_animating == True and self.attack_animation == False:
            self.x_speed = int(random.randrange(1,3))
            self.y_speed = int(random.randrange(1,3))
            self.current_sprite += 0.1
            
            if self.current_sprite > self.attack_sprite_start:
                self.current_sprite = 0
                
            self.image = self.sprites[int(self.current_sprite)]
            self.flipped = pygame.transform.flip(self.image, True, False)
         
        # this is code for the attack animation
        if self.attack_animation == True:
            self.x_speed = 0
            self.y_speed = 0

            self.attack_sprite += 0.1   
            if self.attack_sprite >= len(self.sprites) or self.attack_sprite < self.attack_sprite_start:
                self.attack_sprite = 9
                self.attack_bool = 0
                self.attack_animation = False
            
            self.image = self.sprites[int(self.attack_sprite)]
            self.flipped = pygame.transform.flip(self.image, True, False)
                       
    def draw(self, surface):
        #draw method is used for drawing the enemy, contains a few conditional statements to determine direction of sprite, and whether health bar should be drawn.
        
        if self.gui_on == True:
            pygame.draw.rect(screen, (0, 255, 0), self.hp_bar)
        if self.is_flipped == True:
            
            surface.blit(self.flipped, (self.x_pos, self.y_pos))
        else:
            surface.blit(self.image, (self.x_pos, self.y_pos))
            

 
class Elf(Enemy): # elf sprites gotten from chierit from itch.io
    #Elf is a child class of Enemy, and inherits its methods, but overwrites the init() function
    def __init__(self, x_pos, y_pos, x_speed, y_speed, ):
        # init function with some basic position and speed parameters
        
        #next chunk of code below is used for animation setup
        self.attack_bool = False
        self.attack_animation = False
        self.sprites = []
        self.sprites.append(pygame.image.load("run_1.png").convert_alpha())
        self.sprites.append(pygame.image.load("run_2.png").convert_alpha())
        self.sprites.append(pygame.image.load("run_3.png").convert_alpha())
        self.sprites.append(pygame.image.load("run_4.png").convert_alpha())
        self.sprites.append(pygame.image.load("run_5.png").convert_alpha())
        self.sprites.append(pygame.image.load("run_6.png").convert_alpha())
        self.sprites.append(pygame.image.load("run_7.png").convert_alpha())
        self.sprites.append(pygame.image.load("run_8.png").convert_alpha())
        self.sprites.append(pygame.image.load("run_9.png").convert_alpha())
        
        self.sprites[0] = pygame.transform.scale(self.sprites[0], (600, 300))
        self.sprites[1] = pygame.transform.scale(self.sprites[1], (600, 300))
        self.sprites[2] = pygame.transform.scale(self.sprites[2], (600, 300))
        self.sprites[3] = pygame.transform.scale(self.sprites[3], (600, 300))
        self.sprites[4] = pygame.transform.scale(self.sprites[4], (600, 300))
        self.sprites[5] = pygame.transform.scale(self.sprites[5], (600, 300))
        self.sprites[6] = pygame.transform.scale(self.sprites[6], (600, 300))
        self.sprites[7] = pygame.transform.scale(self.sprites[7], (600, 300))
        self.sprites[8] = pygame.transform.scale(self.sprites[8], (600, 300))
        
        self.sprites.append(pygame.image.load("2_atk_1.png").convert_alpha())
        self.sprites.append(pygame.image.load("2_atk_2.png").convert_alpha())
        self.sprites.append(pygame.image.load("2_atk_3.png").convert_alpha())
        self.sprites.append(pygame.image.load("2_atk_4.png").convert_alpha())
        self.sprites.append(pygame.image.load("2_atk_5.png").convert_alpha())
        self.sprites.append(pygame.image.load("2_atk_6.png").convert_alpha())
        self.sprites.append(pygame.image.load("2_atk_7.png").convert_alpha())
        self.sprites.append(pygame.image.load("2_atk_8.png").convert_alpha())
        self.sprites.append(pygame.image.load("2_atk_9.png").convert_alpha())
        self.sprites.append(pygame.image.load("2_atk_10.png").convert_alpha())
        self.sprites.append(pygame.image.load("2_atk_11.png").convert_alpha())
        self.sprites.append(pygame.image.load("2_atk_12.png").convert_alpha())
        self.sprites.append(pygame.image.load("2_atk_13.png").convert_alpha())
        self.sprites.append(pygame.image.load("2_atk_14.png").convert_alpha())
        self.sprites.append(pygame.image.load("2_atk_15.png").convert_alpha())
        
        self.sprites[9] = pygame.transform.scale(self.sprites[9], (600, 300))
        self.sprites[10] = pygame.transform.scale(self.sprites[10], (600, 300))
        self.sprites[11] = pygame.transform.scale(self.sprites[11], (600, 300))
        self.sprites[12] = pygame.transform.scale(self.sprites[12], (600, 300))
        self.sprites[13] = pygame.transform.scale(self.sprites[13], (600, 300))
        self.sprites[14] = pygame.transform.scale(self.sprites[14], (600, 300))
        self.sprites[15] = pygame.transform.scale(self.sprites[15], (600, 300))
        self.sprites[16] = pygame.transform.scale(self.sprites[16], (600, 300))
        self.sprites[17] = pygame.transform.scale(self.sprites[17], (600, 300))
        self.sprites[18] = pygame.transform.scale(self.sprites[18], (600, 300))
        self.sprites[19] = pygame.transform.scale(self.sprites[19], (600, 300))
        self.sprites[20] = pygame.transform.scale(self.sprites[20], (600, 300))
        self.sprites[21] = pygame.transform.scale(self.sprites[21], (600, 300))
        self.sprites[22] = pygame.transform.scale(self.sprites[22], (600, 300))
        self.sprites[23] = pygame.transform.scale(self.sprites[23], (600, 300))

        # next chunk of code is used fir basic things like position, some booleans, random speed, and some animation setup + health bar setup
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.x_speed = int(random.randrange(1,3))
        self.y_speed = int(random.randrange(1,3))
        self.current_sprite = 0
        self.direction = 1
        self.image = self.sprites[self.current_sprite]    
        self.is_animating = True
        self.is_flipped = False
        self.hp = 30
        self.hp_x = 5
        self.hp_y = -10
        self.is_alive = True
        self.gui_on = False
        
        #below is code for setting up the timing for attack animation + collision setup
        self.image_rect = self.image.get_rect(center = (self.x_pos, self.y_pos))
        self.hp_bar = pygame.Rect(self.x_pos , self.y_pos , self.hp, 10)
        self.speed = 5
        self.mask = pygame.mask.from_surface(self.image.convert_alpha())
        
        self.rect = pygame.Rect(self.x_pos+ 30, self.y_pos + 30, 60, 80)

        self.mask_image = self.mask.to_surface()
        self.attack_sprite = 9
        self.attack_sprite_start = 9
        self.attack_sprite_end = 23
        
    def draw(self, surface):
        #draw method that draws the Elf onto the screen, contains a few conditional statements to determine direction of sprite, and whether health bar should be drawn.
        
        if self.gui_on == True:
            pygame.draw.rect(screen, (0, 255, 0), self.hp_bar)
            
        if self.is_flipped == True:
            
            surface.blit(self.flipped, (self.x_pos, self.y_pos))
        else:
            surface.blit(self.image, (self.x_pos, self.y_pos))
            
class Thunder(Ice):
    #Thunder is a child class of Ice, because technically the thunder is also a projectile
    def __init__(self, x_pos, y_pos, x_speed, y_speed):
        # init function with some basic position and speed parameters
        
        #next chunk of code is for setting up the sprites, and scaling them
        self.sprites = []
        self.sprites.append(pygame.image.load("Layer 1.png").convert_alpha())
        self.sprites.append(pygame.image.load("Layer 2.png").convert_alpha())
        self.sprites.append(pygame.image.load("Layer 3.png").convert_alpha())
        self.sprites.append(pygame.image.load("Layer 4.png").convert_alpha())
        self.sprites.append(pygame.image.load("Layer 5.png").convert_alpha())
        self.sprites.append(pygame.image.load("Layer 6.png").convert_alpha())
        self.sprites.append(pygame.image.load("Layer 7.png").convert_alpha())
        self.sprites.append(pygame.image.load("Layer 8.png").convert_alpha())
        self.sprites.append(pygame.image.load("Layer 9.png").convert_alpha())
        self.sprites.append(pygame.image.load("Layer 10.png").convert_alpha())
        self.sprites.append(pygame.image.load("Layer 11.png").convert_alpha())
        self.sprites.append(pygame.image.load("Layer 12.png").convert_alpha())
        self.sprites[0] = pygame.transform.scale(self.sprites[0], (200,200))
        self.sprites[1] = pygame.transform.scale(self.sprites[1], (200,200))
        self.sprites[2] = pygame.transform.scale(self.sprites[2], (200,200))
        self.sprites[3] = pygame.transform.scale(self.sprites[3], (200,200))
        self.sprites[4] = pygame.transform.scale(self.sprites[4], (200,200))
        self.sprites[5] = pygame.transform.scale(self.sprites[5], (200,200))
        self.sprites[6] = pygame.transform.scale(self.sprites[6], (200,200))
        self.sprites[7] = pygame.transform.scale(self.sprites[7], (200,200))
        self.sprites[8] = pygame.transform.scale(self.sprites[8], (200,200))
        self.sprites[9] = pygame.transform.scale(self.sprites[9], (200,200))
        self.sprites[10] = pygame.transform.scale(self.sprites[10], (200,200))
        self.sprites[11] = pygame.transform.scale(self.sprites[11], (200,200))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.is_animating = True
        
        #below is some code for position, hitbox, and a counter for each strike
        self.x_pos = (player.x_pos + random.randrange(-100, 100))
        self.y_pos = (player.y_pos + random.randrange(-100, 100)) 
        self.rect = pygame.Rect(self.x_pos+ 50, self.y_pos + 85, 110, 110)
        self.counter = 0
        
    def draw(self, screen):
        #draw method that draws the thunder onto the screen, this is overwritten from the Ice class
        

        # blit yourself at your current position
        screen.blit(self.image, (self.x_pos , self.y_pos))
    
    def update(self):
        #update method is overwritten from the Ice class
        
        # below contains the animation code + hitbox updating
        if self.is_animating == True:
            self.current_sprite += 0.3        
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.counter += 1
                self.x_pos = (player.x_pos + random.randrange(-100, 100)) 
                self.y_pos = (player.y_pos + random.randrange(-100, 100))
                
            self.image = self.sprites[int(self.current_sprite)]
            
        self.rect = pygame.Rect(self.x_pos+ 50, self.y_pos + 85, 110, 110)
    
class Arrow(Ice):
    #arrow is a child class of Ice, since it is also a projectile, meaning arrow inherits Ice class attributes
    def __init__(self, x_pos, y_pos):
        # init function with some basic position and speed parameters        
        
        #next chunk of code is for animation setup
        self.sprites = []
        self.sprites.append(pygame.image.load("arrow_.png").convert_alpha())
        self.sprites[0] = pygame.transform.scale(self.sprites[0], (400,400))
        self.current_sprite =0
        self.image = self.sprites[self.current_sprite]
        self.is_animating = True
        self.is_flipped = False
        
        #next chunk of coode is for setting up trajectory, and position
        self.pos = (x_pos, y_pos)
        mx, my = player.x_pos, player.y_pos
        self.dir = (mx - x_pos, my - y_pos)
        length = math.hypot(*self.dir)
        if length == 0.0:
            self.dir = (0, -1)
        else:
            self.dir = (self.dir[0]/length, self.dir[1]/length)
        self.angle = math.degrees(math.atan2(-self.dir[1], self.dir[0]))
        
        # below contains the code for hitboxes, speed, masks, and acceleration
        self.image_rotate = pygame.transform.rotate(self.image, self.angle)
        self.image_rect = self.image_rotate.get_rect(center = self.pos)
        self.speed = 5
        self.mask = pygame.mask.from_surface(self.image_rotate.convert_alpha())
        self.accel = 1
        self.rect = self.image.get_rect()
        self.mask_image = self.mask.to_surface()



# basic pygame setup, color setup        
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
clock = pygame.time.Clock()
screen_width = 1280
screen_height = 960
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Surival")
WHITE = (255, 255, 255)
BLACK = (0,0,0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
bg_color = pygame.Color("grey12")
light_grey = (200, 200, 200)

#below is the creation of player, using the Player class
player = Player(1, 1, screen_width/2, screen_height/2, 1)

#ice projectile is created with the needed parameter
ice = Ice(player.x_pos,player.y_pos)

    
async def main():
   
    MENU, PLAYING, GAME_OVER = "MENU", "PLAYING", "GAME_OVER"

# Game state variable
    game_state = MENU

    #below is the creation of player, using the Player class
    player = Player(1, 1, screen_width/2, screen_height/2, 1)

    #ice projectile is created with the needed parameter
    ice = Ice(player.x_pos,player.y_pos)

    #next chunk of code is setup for enemies, shooting loop, and now empty projectile lists
    enemy_list = []
    elf_list = []
    thunder_strikes = []    
    bullets = []
    elf_arrows = []
    enemy_attack = []
    shoot_loop = 0
    skill_loop = 0
    pygame.mouse.set_visible(True)
    x_coord = 0
    y_coord = 0
    enemy_number = 10

    #below is setup code for the font
    game_font = pygame.font.Font("Ailerons-Typeface.otf", 40)


    # here is the code for the binary search, and its usage (changing locations based on player name)
    #names = open("super_villains.txt") # opens the super_villains.txt file
    names = ""
    key = "Player"
    name_list = [] # creates empty list called name_list
    
    lower_bound = 0 # set lower_bound variable to 0
    upper_bound = len(name_list) - 1
    
    #binary_search.recursive_binary_search(name_list, key, lower_bound, upper_bound)
    player_name = key

    if player_name.lower() == "genos" or player_name.lower()  == "saitama": # if statement that decides whether or not the background will change
        bg_image = pygame.image.load("moon.png").convert_alpha()
     
    else:
        bg_image = pygame.image.load("green.png").convert_alpha()
        
    bg_image_scaled = pygame.transform.scale(bg_image, (1280, 960))

    # name_pos is the variable used for centering the name on the player
    name_pos =0

    for i in range(len(player_name)):
            name_pos += 1

    #below is some code for the animation, enemies killed counter, and player immunity start
    done = True
    start_animating = False
    enemy_killed = 0
    player_start_immunity = 0

    #this while loop is what runs the game
    while done:
        
        #some code for the player immunity
        player_safe_time = int((600 - player_start_immunity) / 60)
        player_start_immunity += 1
        
        #this if statement is for determing whether the player is alive or not
        if player.hp <= 0:
            done = False
        
            pygame.quit()
            sys.exit()
        
        # this chunk of code is for progressive difficulty by adding more enemies 
        if len(enemy_list) == 0 and len(elf_list) == 0:
            
            for i in range(enemy_number):
        
                enemy = Enemy(random.randrange(1, 1000), random.randrange(1, 800), 2, 2)
                if i // 9:
                    
                    elfs = Elf(random.randrange(1, 1000), random.randrange(1, 800), 2, 2)
                    elf_list.append(elfs)
                enemy_list.append(enemy)
            enemy_number += 3
        
        #the next 4 if statements are loops to make sure the bullets don't infinitely shoot
        if shoot_loop > 0:
            shoot_loop += 1
        if shoot_loop > 25:
            shoot_loop = 0
        
        if skill_loop > 0:
            skill_loop += 1
        if skill_loop > 1000:
            skill_loop = 0
        
        #pygame setup
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                screen.fill((0, 0, 0))  # Fill the screen with black
                game_over_text = game_font.render("Game Over", True, (255, 0, 0))  # Red text
                text_rect = game_over_text.get_rect(center=(400, 300))
                screen.blit(game_over_text, text_rect)
                pygame.display.flip()
                
                
                pygame.quit()
                sys.exit
        
        #this for loop contains the code to check collision detection, whether the enemy was hit, whether the bullet is stil on screen, or if the bullet should be removed from the list
        for bullet in bullets:
        
            if (bullet.pos[0] < screen_width and bullet.pos[0] > 0) and (bullet.pos[1] < screen_height and bullet.pos[1] > 0):
                
                bullet.update()

                for i in enemy_list:
                    offset_bullet = (bullet.image_rect.x - i.x_pos), (bullet.image_rect.y - i.y_pos)
                    if i.mask.overlap(bullet.mask, offset_bullet):
                        i.hp -= 2
                        
                        
                for e in elf_list:
                    offset_elf = (bullet.image_rect.x - e.x_pos), (bullet.image_rect.y - e.y_pos)
                    if e.mask.overlap(bullet.mask, offset_elf):
                        e.hp -= 2   
            else:

                bullets.pop(bullets.index(bullet))
        
        #the next 3 lines of code are for setting up the keys, mouse position
        keys = pygame.key.get_pressed()
        mouse = pygame.mouse.get_pressed()
        pygame.mouse.get_pos()

        # this if statement checks whether the Ice shard should be created or not
        if keys[pygame.K_SPACE] and shoot_loop == 0 and player.mana >5:
            x_coord = pygame.mouse.get_pos()[0]
            y_coord = pygame.mouse.get_pos()[1]

            if len(bullets) < 2:
                player.mana -= 5
                bullets.append(Ice((player.x_pos + 30), (player.y_pos + 70 //2)))                 
            shoot_loop += 1
        
        # this next if statement is for determing whether there is no cooldown left for the thunder, and if not, then starts the thunder skill
        if (keys[pygame.K_q]) and (skill_loop == 0) and (player.mana > 10):
            
            if len(thunder_strikes) < 4:
                player.mana -= 10
                thunder_strikes.append(Thunder((screen_width/2), (screen_height/2), 10, 10))

            skill_loop += 1
        
        #this for loop contains the code to check collision detection, whether the enemy was hit, whether the thunder is stil on screen, or if the thunder should be removed from the list
        for t in thunder_strikes:
            if t.x_pos < screen_width and t.x_pos > 0:

                t.update()

                for i in enemy_list:
                    if t.rect.colliderect(i.image_rect):
                        i.hp -= 1          
            else:
                thunder_strikes.pop(thunder_strikes.index(t))
        
        #this for loop contains the code to check collision detection, whether the player was hit by the arrow, whether the arrow is stil on screen, or if the arrow should be removed from the list
        for a_arrow in elf_arrows:
           
            if a_arrow.pos[0] < screen_width and a_arrow.pos[0] > 0:
                
                a_arrow.update()
                    
                offset_arrow = (a_arrow.image_rect.x - player.x_pos), (a_arrow.image_rect.y - player.y_pos)

                if player.mask.overlap(a_arrow.mask, offset_arrow):
                    
                    if player_safe_time <= 0:
                        player.hp -= 0.2
                        elf_arrows.pop(elf_arrows.index(a_arrow))
                        
            else:
                elf_arrows.pop(elf_arrows.index(a_arrow))
        
        
        screen.blit(bg_image_scaled, (0,0)) # draws the background image onto screen

        player.controls() # calls the controls method from the Player class
        
        #below is the code for the enemy ai, check for whether it is alive or not, and the player invincibility check
        for bad in enemy_list:
            
            if bad.x_pos <= player.x_pos:
                bad.x_pos += bad.x_speed
            
            elif bad.x_pos > player.x_pos:
                bad.x_pos -= bad.x_speed
            
            if bad.y_pos <= player.y_pos -30:
                bad.y_pos += bad.y_speed
            
            elif bad.y_pos > player.y_pos -30:
                bad.y_pos -= bad.y_speed
                
            if bad.hp <= 0:
                enemy_list.pop(enemy_list.index(bad))
                enemy_killed += 1
                
            elif bad.hp > 0:
            
                bad.update()
                #pygame.draw.rect(screen, (0, 0, 130), bad.image_rect)
                #screen.blit(bad.mask_image, bad.image_rect)
                bad.draw(screen)
                
            if player_safe_time <= 0:            
                if bad.image_rect.colliderect(player.rect):
                    player.hp -= 0.1
         
        # this is similar to the enemy ai, but has a small offset, and also has a chance to shoot an arrow
        for brown_elf in elf_list:
            
            attack_chance = random.randrange(1, 1000)
                
            if brown_elf.x_pos <= player.x_pos - 250 :
                brown_elf.x_pos += brown_elf.x_speed
            
            elif brown_elf.x_pos > player.x_pos- 250:
                brown_elf.x_pos -= brown_elf.x_speed
            
            if brown_elf.y_pos <= player.y_pos - 160:
                brown_elf.y_pos += brown_elf.y_speed
            
            elif brown_elf.y_pos > player.y_pos - 160:
                brown_elf.y_pos -= brown_elf.y_speed
            
            if brown_elf.hp <= 0:
                elf_list.pop(elf_list.index(brown_elf))
                enemy_killed += 1
                
            elif brown_elf.hp > 0:
            
                brown_elf.update()

                #screen.blit(brown_elf.mask_image, brown_elf.image_rect)
                #pygame.draw.rect(screen, (0, 0, 130), brown_elf.image_rect)
                brown_elf.draw(screen)
            
            if attack_chance < 40:
                
                brown_elf.attack_bool = True
                if brown_elf.attack_sprite > 16:
                    elf_arrows.append(Arrow((brown_elf.x_pos + 275), (brown_elf.y_pos + 200)))
            
                # x 275, y 200          
        
        #code for drawing the bullets
        for bullet in bullets: 
            bullet.draw(screen)
            #screen.blit(bullet.mask_image, bullet.pos)
        
        #code for drawing the elf arrows
        for arrow in elf_arrows:            
            #pygame.draw.rect(screen, (0,0,255), arrow.mask_rect)

            arrow.draw(screen)
         
            
                
        player.update() # calls the update method from the Player class
        #pygame.draw.rect(screen, (0,0, 130), player.rect)
        #screen.blit(player.mask_image, (player.x_pos, player.y_pos))
        player.draw(screen) # draws player onto the screen
        
        #draws the thunder, and also checks how many strikes have been shot
        for t in thunder_strikes:
            if t.counter > 8:
                thunder_strikes.pop(thunder_strikes.index(t))
            elif t.counter > 0:
                t.draw(screen)
        
        # the next chunk of code is for drawing the text on the game screen, which tells user about how much mana they have, skill cooldown, and enemy kill score
        player.mana += 0.050 # adds mana to player.mana
        
        player_text = game_font.render(f"{player_name}", True, light_grey)
        
        screen.blit(player_text, (player.x_pos - name_pos*7, player.y_pos - 50))
        
        skill_cd_number = int((1000 - skill_loop) / 60)
        
        skill_cd_text = game_font.render("Thunder Cooldown:" + f"{skill_cd_number}" + " Seconds", True, (255, 236, 89))
        
        screen.blit(skill_cd_text, (100, 100))
        
        mana = int(player.mana)
        mana_text = game_font.render("Mana amount:" + f"{mana}", True, (89, 189, 255))
        
        screen.blit(mana_text, (100, 50))
        
        
        shoot_text = game_font.render("frames until u can shoot: " + f"{shoot_loop}", True, (124,0,124))
        
        screen.blit(shoot_text, (100, 150))
         
        enemy_kill_score = game_font.render("enemies killed: " + f"{enemy_killed}", True, (0,255,255))
        
        screen.blit(enemy_kill_score, (600, 50))
        
        pygame.display.flip()
        clock.tick(60) # makes game run at 60 fps
        await asyncio.sleep(0)

        
if __name__ == "__main__":
    asyncio.run(main())


