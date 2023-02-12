class Device:
	def __init__(self, model, year_release):
		self.model = model
		self.year_release = year_release
	def __repr__(self):
		return f'{model} has the {year_release} year release'

class Smartphone(Device):
	def __init__(self, battery, price):
	super().__init__(self, rate, feedback)
	self.camera = True
	self.nfc = True

class Watch(Device):
	def __init__(self, battery, price):
	super().__init__(self, rate, feedback)
	self.camera = False
	self.nfc = True
	
class Speaker(Device):
	def__init__(self, battery, price):
	super().__init__(self, rate, feedback)
	self.bluetooth = True
	self.sync = False

	
