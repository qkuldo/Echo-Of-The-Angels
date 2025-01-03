import pygame
import random
import copy
enemy_ids = {
             "slime":[0,1],
             "corrupted golem":[0,2]
            }
class Enemy:
	def __init__(self, texture, pos=[0,0], dmg=1, speed = 1, ID = [0, 0], knockback = 1, hp=1, anim_frames=None, point_drop=1,corpse="slime corpse", key_item=None):
		self.pos = pos
		self.dmg = dmg
		self.texture = texture
		self.hitbox = self.texture.get_rect(x=pos[0], y=pos[1])
		self.speed = speed
		self.ID = ID
		self.knockback = knockback
		self.hp = hp
		self.cooldown = 0
		self.direction = 0
		self.inv_frames = 0
		self.move_wall = [True, True, True, True]
		self.state = "patrol"
		self.line_of_sight = pygame.Rect(self.hitbox.center[0], self.hitbox.center[1], 300,300)
		self.old_pos = self.pos
		self.anim_frames = anim_frames
		self.anim_index = 0
		self.anim_pause = 200
		self.point_drop = point_drop
		self.spin_walk_cooldown = 0
		self.corpse = corpse
		self.key_item = key_item
		self.runaway = 0
		self.death_attack_hp = copy.deepcopy(self.hp) // 2
		self.attack_hitbox_spawned = 0
		self.modify_drop = {"max hp":0,"speed":0,"damage":0,"special mult":0,"dash_mult":0}
	def draw(self, screen):
		screen.blit(self.texture, self.pos)
	def update(self, clock, speed=200):
		self.anim_pause -= clock.get_time()
		if (self.spin_walk_cooldown > 0):
			self.spin_walk_cooldown -= clock.get_time()
		if (self.anim_pause <= 0):
			self.anim_index += 1
			if (self.anim_index > len(self.anim_frames)-1):
				self.anim_index = 0
			self.anim_pause = speed
		if (self.spin_walk_cooldown <= 0):
		     self.texture = pygame.transform.rotate(self.anim_frames[self.anim_index], random.randint(-5, 5))
		     self.texture.set_colorkey((255,255,255))
		     self.spin_walk_cooldown = 100
class Projectile:
	def __init__(self, texture, velocity_x, velocity_y, dmg, lifetime, pos):
		self.velocity_x = velocity_x
		self.velocity_y = velocity_y
		self.dmg = dmg
		self.lifetime = lifetime
		self.texture = texture
		self.pos = pos
		self.hitbox = self.texture.get_rect(x=pos[0], y=pos[1])
	def draw(self, screen):
		screen.blit(self.texture, self.pos)