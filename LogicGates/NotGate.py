from UnaryGate import UnaryGate

class NotGate(UnaryGate):

	def __init__(self, label):
		super(NotGate, self).__init__(label)

	def performGateLogic(self):
		a = self.getPin()
		return not a