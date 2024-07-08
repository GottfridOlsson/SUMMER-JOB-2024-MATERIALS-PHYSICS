EC-LAB SETTING FILE

Number of linked techniques : 4

EC-LAB for windows v11.52 (software)
Internet server v11.52 (firmware)
Command interpretor v11.50 (firmware)

Filename : C:\Users\kmf\Documents\EC-Lab\Data\Gottfrid\SUMMER-JOB-2024\2024-07-04_S26-S27-S28-S29\2024-07-04_S29_Icell_t1800_C0010_J01_deltaX-109,9mm_12mmLi-polished.mps

Device : MPG-2
CE vs. WE compliance from -10 V to 10 V
Electrode connection : standard
Potential control : Ewe
Ewe ctrl range : min = -1.00 V, max = 3.50 V
Safety Limits :
	Do not start on E overload
Electrode material : 
Initial state : 
Electrolyte : 
Comments : 
Electrode surface area : 0.196 cm�
Characteristic mass : 0.001 g
Equivalent Weight : 0.000 g/eq.
Density : 0.000 g/cm3
Volume (V) : 0.001 cm�
Record Ece
Record Power
Cycle Definition : Charge/Discharge alternance
Do not turn to OCV between techniques

Technique : 1
Open Circuit Voltage
tR (h:m:s)          0:01:0.0000         
dER/dt (mV/h)       0.0                 
record              <Ewe>               
dER (mV)            0.00                
dtR (s)             10.0000             
E range min (V)     -1.000              
E range max (V)     3.500               

Technique : 2
Modulo Bat
ctrl_type           CV                  
Apply I/C           I                   
current/potential   current             
ctrl1_val           0.010               
ctrl1_val_unit      V                   
ctrl1_val_vs        Ref                 
ctrl2_val           0.000               
ctrl2_val_unit                          
ctrl2_val_vs                            
ctrl3_val           0.000               
ctrl3_val_unit                          
ctrl3_val_vs                            
N                   0.00                
charge/discharge    Charge              
charge/discharge_1  Charge              
Apply I/C_1         I                   
N1                  0.00                
ctrl4_val           0.000               
ctrl4_val_unit                          
ctrl5_val           0.000               
ctrl5_val_unit                          
ctrl_tM             0                   
ctrl_seq            0                   
ctrl_repeat         0                   
ctrl_trigger        Falling Edge        
ctrl_TO_t           0.000               
ctrl_TO_t_unit      d                   
ctrl_Nd             6                   
ctrl_Na             2                   
ctrl_corr           0                   
lim_nb              1                   
lim1_type           Time                
lim1_comp           >                   
lim1_Q              Q limit             
lim1_value          1800.000            
lim1_value_unit     s                   
lim1_action         Next sequence       
lim1_seq            1                   
rec_nb              2                   
rec1_type           I                   
rec1_value          50.000              
rec1_value_unit     �A                  
rec2_type           Time                
rec2_value          10.000              
rec2_value_unit     s                   
E range min (V)     -1.000              
E range max (V)     3.500               
I Range             Auto                
I Range min         10 �A               
I Range max         10 mA               
I Range init        10 �A               
auto rest           1                   
Bandwidth           5                   

Technique : 3
Open Circuit Voltage
tR (h:m:s)          0:00:0.1000         
dER/dt (mV/h)       1.0                 
record              <Ewe>               
dER (mV)            0.00                
dtR (s)             0.0500              
E range min (V)     -1.000              
E range max (V)     3.500               

Technique : 4
Chronopotentiometry
Is                  -1.131              
unit Is             mA                  
vs.                 <None>              
ts (h:m:s)          0:00:36.0000        
EM (V)              pass                
dQM                 11.310              
unit dQM            �A.h                
record              Ewe                 
dEs (mV)            1.00                
dts (s)             10.0000             
E range min (V)     -1.000              
E range max (V)     3.500               
I Range             1 mA                
Bandwidth           5                   
goto Ns'            0                   
nc cycles           0                   
