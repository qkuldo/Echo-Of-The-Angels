import pygame
import copy
from random import randint
class Particle:
	"""A class to define individual particles"""
	def __init__(self, texture,pos=[0,0], velocity_x=1, velocity_y=1, lifetime=400):
		self.pos = pos
		self.velocity_x = velocity_x
		self.velocity_y = velocity_y
		self.lifetime = lifetime
		self.texture = texture
	def move(self, clock):
		self.pos[0] += self.velocity_x
		self.pos[1] += self.velocity_y
		self.lifetime -= clock.get_time()
class ParticleGroup:
	"""A class to define groups of particles"""
	def __init__(self, texture, pos, velocity_x, velocity_y, lifetime,fade=False,spin=False):
		self.particlelist = []
		self.texture = texture
		self.pos = pos
		self.velocity_x = velocity_x
		self.velocity_y = velocity_y
		self.lifetime = lifetime
		self.spin = spin
	def spawn_particle(self):
		self.particlelist.append(Particle(copy.copy(self.texture),self.pos,copy.deepcopy(self.velocity_x),copy.deepcopy(self.velocity_y),self.lifetime))
	def update_group(self, clock):
		for particle in self.particlelist:
			particle.move(clock)
			if (particle.lifetime <= 0):
				self.particlelist.remove(particle)
	def draw(self, screen):
		for particle in self.particlelist:
			if (self.spin):
			    draw_txt = pygame.transform.rotate(particle.texture, randint(-5,5))
			    draw_txt.set_colorkey((255,255,255))
			else:
				draw_txt = particle.texture.copy()
			dropshadow = draw_txt.copy()
			dropshadow.set_alpha(80)
			screen.blit(dropshadow,(particle.pos[0],particle.pos[1]+5))
			screen.blit(draw_txt, particle.pos)
	def setup(self, screen, clock):
		self.update_group(clock)
		self.draw(screen)