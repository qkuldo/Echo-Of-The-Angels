import pygame
import copy
class Particle:
	"""A class to define individual particles"""
	def __init__(self, pos=[0,0], velocity_x=1, velocity_y=1, lifetime=400):
		self.pos = pos
		self.velocity_x = velocity_x
		self.velocity_y = velocity_y
		self.lifetime = lifetime
	def move(self, clock):
		self.pos[0] += self.velocity_x
		self.pos[1] += self.velocity_y
		self.lifetime -= clock.get_time()
class ParticleGroup:
	"""A class to define groups of particles"""
	def __init__(self, texture, pos, velocity_x, velocity_y, lifetime):
		self.particlelist = []
		self.texture = texture
		self.pos = pos
		self.velocity_x = velocity_x
		self.velocity_y = velocity_y
		self.lifetime = lifetime
	def spawn_particle(self):
		self.particlelist.append(Particle(self.pos,self.velocity_x,self.velocity_y,self.lifetime))
	def update_group(self, clock):
		for particle in self.particlelist:
			particle.move(clock)
			if (particle.lifetime <= 0):
				self.particlelist.remove(particle)
	def draw(self, screen):
		for particle in self.particlelist:
			screen.blit(self.texture, particle.pos)
	def setup(self, screen, clock):
		self.update_group(clock)
		self.draw(screen)