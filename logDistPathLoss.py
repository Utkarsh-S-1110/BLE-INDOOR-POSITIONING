import math

class LogDistPathLoss:
	def __init__(self):
		self. pathLossIndex = 3.3
		self.free_space_path_loss = -4.04
		#self.rssi_ref = -34.52279052921755
		self.dist_ref = 1.0
		

	def calc_loss(self,dist):
		return (-4.04 + ((self.pathLossIndex*10)*math.log10(dist/self.dist_ref)))
		

