EC-LAB SETTING FILE

Number of linked techniques : 4

EC-LAB for windows v11.46 (software)
Internet server v11.40 (firmware)
Command interpretor v11.40 (firmware)

Filename : C:\Users\kmf\Desktop\Biologic Data\Gottfrid\SUMMER-JOB-2024\2024-07-02_S24-S25\2024-07-02_S25_TPcell_t1800_C0500_J01.mps

Device : VMP3
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
Electrode surface area : 0.001 cm²
Characteristic mass : 0.001 g
Equivalent Weight : 0.000 g/eq.
Density : 0.000 g/cm3
Volume (V) : 0.001 cm³
Record Ece
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
rec1_value_unit     µA                  
rec2_type           Time                
rec2_value          10.000              
rec2_value_unit     s                   
E range min (V)     -1.000              
E range max (V)     3.500               
I Range             Auto                
I Range min         10 µA               
I Range max         1 A                 
I Range init        10 µA               
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
Is                  -196.000            
unit Is             µA                  
vs.                 <None>              
ts (h:m:s)          0:30:0.0000         
EM (V)              pass                
dQM                 98.000              
unit dQM            µA.h                
record              Ewe                 
dEs (mV)            1.00                
dts (s)             10.0000             
E range min (V)     -1.000              
E range max (V)     3.500               
I Range             100 µA              
Bandwidth           5                   
goto Ns'            0                   
nc cycles           0                   
