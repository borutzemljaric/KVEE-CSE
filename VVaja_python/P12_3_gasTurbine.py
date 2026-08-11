#P12_3_gasTurbine.py
# work and consumption of gas turbine with compressor

# input data
p2=100*1000 # (Pa) turbine outlet/exhaust pressure
T2=564+273 # (K) turbine exhaust temperature

p3=p2 # (K) compressor inlet temperature (environment)
T3=20+273 # (K) environment  temperature

p1overp2=22 # (Pa) pressure ration p1/p2 is given

mdot=73 # (kg/s) mass exhaust flow

# specific heat ratio
kappa_air=1.4
kappa_mixture=1.34
#Specific heat at constant volume
cv_air=0.71*1000 # (J/Kg K) specific heat at constant volume
cv_mixture=0.86*1000 # (J/Kg K)

cp_mixture=1.15*1000 # (J/Kg K) specific heat at constant pressure

hgas=36e6 # (J/m3) gas colorific value for Natural Gas (Typical) 35.4 – 39.1 MJ/m3


#Adiabatic consideration
def temperature(Tt2,p1overp2, kappa):
    Tt1=Tt2*p1overp2**((kappa-1)/kappa)
    return Tt1

def workTechnical(kappa,c,mass, Tt2, Tt1):
    work=kappa*mass*c*(Tt1-Tt2)
    return work

#++++++++++calculations TURBINE Section+++++++++++++++++++++++++
p1=22*p2 #presurre at turbine inlet
print('p1 (kPa): ',p1)

T1=temperature(T2,p1overp2,kappa_mixture)
print('T1 (K): ',T1)

# tehnical work per second (because mass flow is given)
Wt=workTechnical(kappa_mixture,cv_mixture,mdot, T2, T1)
print('Pt= dot(Wt) (J/s): ',Wt)

#+++++++++calculations COMPRESSOR Section+++++++++++++++++++++
# air temperature after compressor
# #assuming that in combustion chamber the proces is isobaric
T4=temperature(T3,p1overp2,kappa_air)
print('T4 (K): ',T4)

# tehnical work per second (because mass flow is given)
Wc=workTechnical(kappa_air,cv_air,mdot, T4, T3)
print('Pc= dot(Wc) (J/s): ',Wc)

#required heat transfer ratio dot(Q)=mdot*cp*(T1-T4), to heat
# air from T4 to T1
dotQ=mdot*cp_mixture*(T1-T4)
print('dotQ= (J/s): ',Wt)

#consumption of gas
dotV=dotQ/hgas # consumption per second
print('dotV= (m3/s): ',dotV)
print('V (t=1h)= (m3): ',dotV*3600)  # in one hour

# p1 (kPa):  2200000
# T1 (K):  1833.7501739668965
# Pt= dot(Wt) (J/s):  83851807.73499997
# T4 (K):  708.6257958192048
# Pc= dot(Wc) (J/s):  -30158638.99623313
# dotQ= (J/s):  83851807.73499997
# dotV= (m3/s):  2.62372754293052
# V (t=1h)= (m3):  9445.41915454987



