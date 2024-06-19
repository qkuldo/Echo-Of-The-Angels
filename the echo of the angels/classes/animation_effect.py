class Effect:
	"""An animation that appears temporarily"""
	def __init__(self, frames, lifetime, pos):
		self.frames = frames
		self.frame_index = 0
		self.current_frame = self.frames[self.frame_index]
		self.frame_timer = 100
		self.lifetime = lifetime
		self.pos = pos
	def draw(self, screen):
		screen.blit(self.current_frame, self.pos)
	def update(self, clock):
		self.frame_timer -= clock.get_time()
		if (self.frame_timer <= 0):
			self.frame_index += 1
			if (self.frame_index > len(self.frames)-1):
				self.frame_index = 0
			self.frame_timer = 100
		self.current_frame = self.frames[self.frame_index]
		self.lifetime -= clock.get_time()