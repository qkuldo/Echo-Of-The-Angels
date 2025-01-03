import pygame
import classes.enemy
import random
class Room:
    """A class to define rooms"""
    def __init__(self, spawners, exits=None, walls = [],pots=[], toxic_pools = []):
        self.spawners = spawners
        self.exits = exits
        self.walls = walls
        self.pots =pots
        self.toxic_pools = toxic_pools
    def load_room(self, enemy_list, sprite_dict, wall_list, pot_list, toxic_pool_list, spawn_enemy=True, spawn_pot = True):
        for i in self.spawners:
            if (i.enemy_id == [0,1] and spawn_enemy):
                 enemy_list.append(classes.enemy.Enemy(sprite_dict["slime"], i.pos, ID = classes.enemy.enemy_ids["slime"], knockback = 25, hp = 15, anim_frames=(sprite_dict["slime"], sprite_dict["slime 2"],),key_item=i.key_item,dmg=5))
                 enemy_list[-1].modify_drop = {"max hp":0,"speed":0.2,"damage":0,"special mult":0,"dash_mult":0}
            elif (i.enemy_id == [0,2] and spawn_enemy):
                 enemy_list.append(classes.enemy.Enemy(sprite_dict["corrupted golem 1"], i.pos, ID = classes.enemy.enemy_ids["corrupted golem"], knockback = 25, hp = 25, anim_frames=(sprite_dict["corrupted golem 1"], sprite_dict["corrupted golem 2"]), speed=1, point_drop=5, dmg=10, corpse="corrupted golem corpse", key_item=i.key_item))
                 enemy_list[-1].modify_drop = {"max hp":0.3,"speed":0,"damage":0.2,"special mult":0,"dash_mult":0}
        for i in self.walls:
            wall_list.append(i)
        if (spawn_pot == True):
            for i in self.pots:
                pot_list.append(i)
        for i in self.toxic_pools:
            toxic_pool_list.append(i)

class Spawner:
    """A class to define spawners"""
    def __init__(self, enemy_id, pos, key_item=None):
        self.enemy_id = enemy_id
        self.pos = pos
        self.key_item = key_item
class Wall:
    """A class to define walls"""
    def __init__(self, pos=[0,0], texture=None):
        self.pos = pos
        self.texture = texture
        self.hitbox = self.texture.get_rect(x=pos[0], y=pos[1])
        self.edges = {
         "up":pygame.Rect(self.hitbox.x,self.hitbox.y,self.hitbox.width,self.hitbox.height/5),
         "down":pygame.Rect(self.hitbox.bottomleft[0],self.hitbox.bottomleft[1]-self.hitbox.height/5,self.hitbox.width,self.hitbox.height/5),
         "left":pygame.Rect(self.hitbox.topleft[0],self.hitbox.topleft[1],self.hitbox.width/5,self.hitbox.height),
         "right":pygame.Rect(self.hitbox.topright[0]-self.hitbox.width/5,self.hitbox.topright[1],self.hitbox.width/5,self.hitbox.height)
        }
class Lock:
    """A class to define locks"""
    def __init__(self, locked_room, key_item="key"):
        self.locked_room = locked_room
        self.key_item = key_item
class Pot:
    """A class to define pots that can be broken"""
    def __init__(self, pos=[0,0], drops=[("coins",5),None], texture=None):
        self.pos = pos
        self.drops = drops
        self.texture = texture
        self.hitbox = self.texture.get_rect(x=self.pos[0],y=self.pos[1])
        self.edges = {
         "up":pygame.Rect(self.hitbox.x,self.hitbox.y,self.hitbox.width,self.hitbox.height/5),
         "down":pygame.Rect(self.hitbox.bottomleft[0],self.hitbox.bottomleft[1]-self.hitbox.height/5,self.hitbox.width,self.hitbox.height/5),
         "left":pygame.Rect(self.hitbox.topleft[0],self.hitbox.topleft[1],self.hitbox.width/5,self.hitbox.height),
         "right":pygame.Rect(self.hitbox.topright[0]-self.hitbox.width/5,self.hitbox.topright[1],self.hitbox.width/5,self.hitbox.height)
        }
class Foliage:
    """A class to define foliage that appears randomly."""
    def __init__(self, texture,pos=[0,0]):
        self.pos = pos
        self.texture = texture
        self.blit_texture = texture
        self.spin = 0
    def move(self,clock):
        self.spin += clock.get_time()
        if (self.spin >= 500):
            self.blit_texture = pygame.transform.rotate(self.texture,random.randint(-5,5))
            self.blit_texture.set_colorkey((255,255,255))
            self.spin = 0
    def draw(self,screen):
        screen.blit(self.blit_texture,self.pos)
class Toxic_Pool:
    def __init__(self,texture,pos=[0,0],dmg=1):
        self.pos = pos
        self.texture = texture
        self.dmg = 1
        self.hitbox = self.texture.get_rect(x=self.pos[0],y=self.pos[1])
        
        
        