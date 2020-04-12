from BinaryGate import BinaryGate

class NandGate(BinaryGate):

	def __init__(self, label):
		super(NandGate, self).__init__(label)

	def performGateLogic(self):
		a = self.getPinA()
		b = self.getPinB()
		return not(a and b)