import pygame
import random
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
		self.line_of_sight = pygame.Rect(self.hitbox.center[0], self.hitbox.center[1], 250,250)
		self.old_pos = self.pos
		self.anim_frames = anim_frames
		self.anim_index = 0
		self.anim_pause = 200
		self.point_drop = point_drop
		self.spin_walk_cooldown = 0
		self.corpse = corpse
		self.key_item = key_item
	def draw(self, screen):
		screen.blit(self.texture, self.pos)
	def update(self, clock):
		self.anim_pause -= clock.get_time()
		if (self.spin_walk_cooldown > 0):
			self.spin_walk_cooldown -= clock.get_time()
		if (self.anim_pause <= 0):
			self.anim_index += 1
			if (self.anim_index > len(self.anim_frames)-1):
				self.anim_index = 0
			self.anim_pause = 200
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