import math

class Kalman_Filter:
	def __init__(self,x_real):
		self.R = 0.008
		self.x_real = x_real
		self.prev_certainity = 1

	def find_real(self,new_val,):
		x_pred = self.x_real
		certainity = self.prev_certainity + self.R
		Q = (6.52* math.exp(-0.0183*self.x_real))
		kalman_gain = certainity/(certainity+Q)
		self.x_real = x_pred + (kalman_gain*(new_val-x_pred))
		self.prev_certainity = certainity*(1-kalman_gain)
		return self.x_real

