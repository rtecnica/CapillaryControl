import math

ulmTom3s = ((1 / 60) * 1e-9)
esp0 = 8.854187817 * pow(10,-12)

def ExV(FlowRate_kgs, Power):
    return(math.sqrt(2*Power/FlowRate_kgs))

def Thrust(FlowRate_kgs,Power):
    Ve = ExV(FlowRate_kgs, Power)
    return Ve*FlowRate_kgs

def Isp(FlowRate_kgs,Power):
    return(ExV(FlowRate_kgs,Power)/9.81)

