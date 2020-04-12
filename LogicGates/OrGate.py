from BinaryGate import BinaryGate

class OrGate(BinaryGate):

	def __init__(self, label):
		super(OrGate, self).__init__(label)

	def performGateLogic(self):
		a = self.getPinA()
		b = self.getPinB()
		return a or b