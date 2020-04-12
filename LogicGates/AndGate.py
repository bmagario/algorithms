from BinaryGate import BinaryGate

class AndGate(BinaryGate):

	def __init__(self, label):
		super(AndGate, self).__init__(label)

	def performGateLogic(self):
		a = self.getPinA()
		b = self.getPinB()
		return a and b