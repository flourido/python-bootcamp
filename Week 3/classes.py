class wheel:
	def __init__(self, diameter, wtype="all-weather"): #methods-part of a class
			self.size = diameter #attributes
			self.type = wtype

class engine:
	def __init__(self,horsepower,n_cylinders):
		self.horsepower = horsepower
		self.n_cylinders = n_cylinders

		self.is_healthy= True
		self.need_oil_change= False
		self.trip_counter = 0
		self.mileage = 0 
		self.max_mileage = 0

	def check_health(self):
		if self.mileage > self.max_mileage:
			self.is_healthy= False 
			print("Our engine is breaking ")

		if self.trip_counter >= 3000:
			self.is_healthy = False
			print(" Change your oil! ")

	def change_oil(self):
		if self.trip_counter == 0:
			self.need_oil_change = False
			self.is_healthy = True
			print("Thanks for changing your oil ")

class body:
	def __init__(self, color, num_doors=4):
		self.num_doors= num_doors
		self.color= color

		if self.num_doors == 0:
			self.trunk_size = "tiny"
		if self.num_doors == 2:
			self.trunk_size = "small"
		if self.num_doors == 4:
			self.trunk_size = "med"
		if self.num_doors == 5:
			self.trunk_size = "large"
