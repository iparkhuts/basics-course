class Device:
	def __init__(self, model, year_release):
		self.model = model
		self.year_release = year_release
		
	def __repr__(self):
		return f'{self.model} was released in {self.year_release}'

class Smartphone(Device):
	def __init__(self, model, year_release, battery, price):
		super().__init__(model, year_release)
		self.battery = battery
		self.price = price
		self.camera = True
		self.nfc = True

class Watch(Device):
	def __init__(self, model, year_release, battery, price):
		super().__init__(model, year_release)
		self.battery = battery
		self.price = price
		self.camera = True
		self.nfc = True
	
class Speaker(Device):
	def __init__(self, model, year_release, battery, price):
		super().__init__(model, year_release)
		self.battery = battery
		self.price = price
		self.bluetooth = True
		self.sync = False
