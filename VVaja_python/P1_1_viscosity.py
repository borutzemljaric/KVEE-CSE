# P1_1_viscosity.py
# calculate pulling force

# input data
d=0.2 # m distance between fixed plates
x=0.05 #m  distance moving plate
mi=46*1e-3 # dynamic viscosity
v= 1 # m/s  plate velocity
A=1 # m2 area

#solution (first question)
tau_1=mi*v/(d-x)
tau_2=mi*v/(x)
F=(tau_1+tau_2)*A

print ('F', F )  #result



