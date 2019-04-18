#python 3.6
# This programme calculates the composition jump and solubility range of Cu6Sn5 IMC between FCC(Cu) and Liq(Sn)
# Physics : Kidson's Equation (Kidson1961-JONM, Guan2015-JAC)
# E.g. x_imccu (mole fraction) is the value of common tangent between FCC and Cu6Sn5 at equilibrium composition #for the IMC phase
#import numpy as np
import numpy as np
import math 
class Composition:
   def __init__(self, diffusivity, x_cuimc, x_imccu, x_imcsn, x_snimc):
      self.diffusivity = diffusivity
      self.x_cuimc = x_cuimc
      self.x_imccu = x_imccu
      self.x_imcsn = x_imcsn
      self.x_snimc = x_snimc
   
   #solubility range
   def get_solrange(self):
       return self.x_imcsn-self.x_imccu

   #Composition jump
   def get_compjump_imccu(self):
       return self.x_imccu-self.x_cuimc
       #return self.x_cuimc-self.x_imccu

   def get_compjump_imcsn(self):
       return self.x_snimc-self.x_imcsn

   #growth rate coefficient (m s^(-0.5))
   def calculate_growthratecoeff(self):
       numerator=2.0*self.diffusivity*self.get_solrange()
       denominator=self.get_compjump_imccu()+ self.get_compjump_imcsn()
       return math.sqrt(numerator/denominator)
filename_imc="kidson_parameters.dat"
# (Source: Y. Guan and N. Moelans,2015-JAC (635) pp.289-299,Hektor et al, 2016-ActaMater(108)pp.98-109)
data_kidson=np.loadtxt(filename_imc, delimiter=",", skiprows=1, 
                  usecols=[0,1,2,3,4])
diffusivity=data_kidson[0]
x_cuimc=data_kidson[1]
x_imccu=data_kidson[2]
x_imcsn=data_kidson[3]
x_snimc=data_kidson[4]
#
r=Composition(diffusivity, x_cuimc, x_imccu, x_imcsn, x_snimc)
print("Solubility range of Cu6Sn5: %s [unitless]" %(r.get_solrange()))
print("Composition jump at Cu/Imc interface:  %s [unitless]" %(r.get_compjump_imccu()))
print("Composition jump at Sn/Imc interface:  %s [unitless]" %(r.get_compjump_imcsn()))
print("Growth rate coefficient of Cu6Sn5 at T K:  %s [m s^(-0.5)]" %(r.calculate_growthratecoeff()))



