import PropMath
import math

class propellant:

    def __init__(self,density,conductivity,dielectricConstant,surfaceTension):
        self.rho = density
        self.sigma = conductivity
        self.dielectricK = dielectricConstant
        self.surfaceTension = surfaceTension

    def vStart(self,Radius, Distance):
        return (math.sqrt((self.surfaceTension * Radius) / PropMath.esp0) * math.log((4 * Distance) / Radius, math.e))

    def jetCurrent(self,FlowRate_m3s):
        return (17 * math.sqrt((self.surfaceTension * self.sigma * FlowRate_m3s) / self.dielectricK))

