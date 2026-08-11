# P12_4_tablesPyxsteam
# demo how to calculate thermodynamic state variables
# using python libraries Pyxsteam
# https://pyxsteam.readthedocs.io/en/latest/index.html

from pyXSteam.XSteam import XSteam

steam_table = XSteam(XSteam.UNIT_SYSTEM_MKS) # m/kg/sec/°C/bar/W
p=1 # (bar) pressure
print ('p (bar): ', p , ' or in (MPa): ', 0.1*p) # (°C) Pressure
print ('tsat_p (°C): ', steam_table.tsat_p(p)) #  Saturation temperature
print ('h_l (kJ/kg): ', steam_table.hL_p(p)) #  Saturated liquid enthalpy
print ('h_v (kJ/kg): ', steam_table.hV_p(p)) #  Saturated vapor enthalpy
print ('v_l (m3/kg): ', steam_table.vL_p(p)) # Saturated vapor volume
print ('v_v (m3/kg): ', steam_table.vV_p(p)) #  Saturated liquid volume

#Specific isobaric heat capacity
print ('CpL_p (kJ/kg K): ', steam_table.CpL_p(p)) # Saturated liquid heat capacity

# specific evaporating heat for water at given pressure
print ('h_i (kJ/kg): ', steam_table.hV_p(p)-steam_table.hL_p(p)) #

# p (bar):  1  or in (MPa):  0.1
# tsat_p (°C):  99.60591861133764
# h_l (kJ/kg):  417.4364858162317
# h_v (kJ/kg):  2674.949640832146
# v_l (m3/kg):  0.0010431478391551838
# v_v (m3/kg):  1.6940225229026846
# CpL_p (kJ/kg K):  4.216149430838748
# h_i (kJ/kg):  2257.5131550159144






