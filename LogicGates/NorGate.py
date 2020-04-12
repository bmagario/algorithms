from BinaryGate import BinaryGate

class NorGate(BinaryGate):

	def __init__(self, label):
		super(NorGate, self).__init__(label)

	def performGateLogic(self):
		a = self.getPinA()
		b = self.getPinB()
		return not(a or b)