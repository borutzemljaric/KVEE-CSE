# P15_1_enthalpy_pT.py
# enthalpy calculation
# https://pyxsteam.readthedocs.io/en/latest/index.html

from pyXSteam.XSteam import XSteam

steam_table = XSteam(XSteam.UNIT_SYSTEM_MKS) # m/kg/sec/°C/bar/W
p=1 # (bar) pressure
T_river=15 #(°C) temperature
T_condenser=27 #(°C) temperature


print ('h_l (kJ/kg): ', steam_table.hL_p(p)) #  Saturated liquid enthalpy
print ('h_v (kJ/kg): ', steam_table.hV_p(p)) #  Saturated vapor enthalpy
# enthalpy required to change 1kg of steam into liquid
print ('delta_h (kJ/kg):', steam_table.hV_p(p)-steam_table.hL_p(p)) # (°C) Pressure

# reminder for some ather options
# function h_pt 	Enthalpy as a function of pressure and temperature
# function h_tx 	Enthalpy as a function of temperature and vapor fraction

# h_l (kJ/kg):  417.4364858162317
# h_v (kJ/kg):  2674.949640832146
# delta_h (kJ/kg): 2257.5131550159144







