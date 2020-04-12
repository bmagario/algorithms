from BinaryGate import BinaryGate

class XorGate(BinaryGate):

	def __init__(self, label):
		super(XorGate, self).__init__(label)

	def performGateLogic(self):
		a = self.getPinA()
		b = self.getPinB()
		if(a == b):
			return 0
		else:
			return 1