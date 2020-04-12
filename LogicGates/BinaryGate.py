from LogicGate import LogicGate

class BinaryGate(LogicGate):

	def __init__(self, label):
		super(BinaryGate, self).__init__(label)

		self.pinA = None
		self.pinB = None
	
	def getPinA(self):
		if self.pinA == None:
			return int(input("Enter Pin A input for gate " + self.getLabel()+"-->"))
		else:
			return self.pinA.getFromGate().getOutput()

	def getPinB(self):
		if self.pinB == None:
			return int(input("Enter Pin B input for gate "+ self.getLabel()+"-->"))
		else:
			return self.pinB.getFromGate().getOutput()

	def setNextPin(self, source):
		if self.pinA == None:
			self.pinA = source
		else:
			if self.pinB == None:
				self.pinB = source
			else:
				raise RuntimeError("Error: NO EMPTY PINS %s" % self.getLabel())