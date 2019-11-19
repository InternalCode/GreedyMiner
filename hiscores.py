import shelve, os


class Hiscores():
	def __init__(self):
		
		self.hiscores = 0
		self.scores = 0
		
		if os.path.isfile('score.dat'):
			score_file = shelve.open('score')
			self.hiscores = score_file['hiscores']
			score_file.close()

	def check_hiscores_reset_old(self):
		if self.scores > self.hiscores:
			self.hiscores = self.scores
			
			score_file = shelve.open('score')
			score_file['hiscores'] = self.hiscores
			score_file.close()

		self.scores = 0
