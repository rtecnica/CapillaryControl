import math

rho = 1110  #kg / m3 Ethylene Glycol density
ulmToKgs = ((1 / 60) * 1e-9 * rho)


def ExV(FlowRate, Power):
    MassFlowRate = FlowRate * ulmToKgs
    return(math.sqrt(2*Power/MassFlowRate))

def Thrust(FlowRate,Power):
    MassFlowRate = FlowRate* ulmToKgs
    Ve = ExV(FlowRate, Power)
    return Ve*MassFlowRate


