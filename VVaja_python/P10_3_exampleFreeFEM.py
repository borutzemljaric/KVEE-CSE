# P10_3_exampleFreeFEM.py
# single cable, finite element method, FreeFEM tool


from pyfreefem import FreeFemRunner
from pymedit import P1Function

# only in virtual network Poetry
import os
# Set PATH to include FreeFEM++ installation directory
ff_path = r"C:\Program Files (x86)\FreeFem++"
os.environ["PATH"] += os.pathsep + ff_path

# Optional: Check if FreeFem++ is now discoverable
#import shutil
#print("FreeFem++ location:", shutil.which("FreeFem++"))


#macro files can be saved in the pyfreefem/edp directory and can be imported using the IMPORT preprocessing instruction:
# INPUT if it is in the same directory

#primer sestave skripte
script = '''
IMPORT "io.edp"
//podatki jarka (dimenzije so v metrih)
real ddy=0.75; // globina kabla
real ax=0.25; // širina polovice jarka
real cy=1; // globina jarka

// podatki vodnika
real r=0.017; // radij zile vodnika 800mm2
real ri=0.038; // radij izolacije vodnika 800 mm2
real Itg=-16800; //temperaturni vir 645A// Cu 800 mm2

// podatki temperature
real Tzrak=35; // temperatura zraka zgoraj
real Tamb=20; // temperatura ambienta spodaj

// podatki toplotne prevodnosti
real lamAlum=400; //podatek za Cu
real lamIzol=0.28;
real lamZemlja=.75;

// +++++ Definiranje mreže končnih elementov +++++
// oznake meja definicijskega območja
int D1=99; int D2=98;

// vodnik, opredelitev žile in izolacije
border C1(t=0,2*pi){x=r*cos(t);y=r*sin(t)-ddy;};
border C11(t=0,2*pi){x=ri*cos(t);y=ri*sin(t)-ddy;};
// opredelitev jareka
border D11(t=0,1){x=ax-t*2*ax;y=0;label=D1;};
border D12(t=0,1){x=-ax;y=-cy*t;};
border D13(t=0,1){x=-ax+t*2*ax;y=-cy;label=D2;};
border D14(t=0,1){x=ax;y=-cy+cy*t;};

int n=10; // število diskretitacije roba elementa
// kreiranje mreže končnih elementov
mesh Th=buildmesh (C1(n)+C11(n)
+D11(2+n)+D12(2*n)+D13(2*n)+D14(2*n) // povečano število delitev faktor 2
);

// izris mreže konćnih elementov
plot (Th,wait=1,ps="mrezaprimerT.jpg");

// zaradi različnih toplotnih prevodnosti se opredeli
// lokacije posameznih območij
int con1 = Th(0,-ddy).region; //območje žile vodnika
int con1i = Th(r+(ri/2-r/2),-ddy).region; //območje izolacije
int conz = Th(0,-.2).region; //območje jarka

// +++++ IZRAČUN PROBLEMA +++++
fespace Vh(Th,P1); // temperature končni element P1
Vh u,v;

fespace V0(Th,P0); // regije končni element P0
V0 reg=region; //defined the P0 function associated to region number

// pripis vrednosti območju toplotne prevodnosti
V0 lambda=0+lamAlum*(region==con1)+lamIzol*(region==con1i)
+lamZemlja*(region==conz);

// pripis vrednosti območju toplotnega vira
V0 ith=0+Itg*(region==con1);
// Reševanje sistema enačb (Laplace in robni pogoji)
solve T(u, v)
= int2d(Th)(
lambda*(
dx(u)*dx(v)
+dy(u)*dy(v)
))
+int2d(Th)(ith*v)
+on ( D1,u=Tzrak)
+on ( D2,u=Tamb);

// izris rezultatov
plot(u,wait=true, value=true, fill=true, ps="primerT.jpg");

'''

runner = FreeFemRunner(script, debug=True)
results = runner.execute(plot=True)




