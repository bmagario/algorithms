class Connector:

	def __init__(self, fromGate, toGate):
		self.fromGate = fromGate
		self.toGate = toGate

		toGate.setNextPin(self)

	def getFromGate(self):
		return self.fromGate

	def getToGate(self):
		return self.toGate