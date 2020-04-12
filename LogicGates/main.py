from AndGate import AndGate
from OrGate import OrGate
from NotGate import NotGate
from NorGate import NorGate
from XorGate import XorGate
from NandGate import NandGate
from Connector import Connector

g1 = AndGate("G1")
g2 = AndGate("G2")
g3 = OrGate("G3")
g4 = NotGate("G4")
g5 = NorGate("G5")
g6 = XorGate("G6")
g7 = NandGate("G7")
g8 = OrGate("G8")
c1 = Connector(g1, g3)
c2 = Connector(g2, g3)
c3 = Connector(g3, g4)
c4 = Connector(g5, g7)
c5 = Connector(g6, g7)
c6 = Connector(g4, g8)
c7 = Connector(g7, g8)
print(g8.getOutput())