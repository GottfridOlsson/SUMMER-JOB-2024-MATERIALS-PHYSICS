EC-LAB SETTING FILE

Number of linked techniques : 7

EC-LAB for windows v11.52 (software)
Internet server v11.52 (firmware)
Command interpretor v11.50 (firmware)

Filename : C:\Users\kmf\Documents\EC-Lab\Data\Gottfrid\SUMMER-JOB-2024\2024-07-03_S20-S21-S22-S23\2024-07-03_S20_Icell_t1800_C0010_J01_deltaX-110,2mm_plating-stripping.mps

Device : MPG-2
CE vs. WE compliance from -10 V to 10 V
Electrode connection : standard
Potential control : Ewe
Ewe ctrl range : min = 0.00 V, max = 5.00 V
Safety Limits :
	Do not start on E overload
Electrode material : 
Initial state : 
Electrolyte : 
Comments : 
Mass of active material : 7000.000 mg
 at x = 1.000
Molecular weight of active material (at x = 0) : 90.930 g/mol
Atomic weight of intercalated ion : 6.940 g/mol
Acquisition started at : xo = 0.900
Number of e- transfered per intercalated ion : 1
for DX = 1, DQ = 1916.936 mA.h
Battery capacity : 0.000 A.h
Electrode surface area : 0.001 cm�
Characteristic mass : 0.001 g
Volume (V) : 0.001 cm�
Record Power
Cycle Definition : Charge/Discharge alternance
Turn to OCV between techniques

Technique : 1
Open Circuit Voltage
tR (h:m:s)          0:01:0.0000         
dER/dt (mV/h)       0.0                 
record              <Ewe>               
dER (mV)            0.00                
dtR (s)             10.0000             
E range min (V)     0.000               
E range max (V)     5.000               

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
E range min (V)     0.000               
E range max (V)     5.000               
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
E range min (V)     0.000               
E range max (V)     5.000               

Technique : 4
Chronopotentiometry
Is                  -196.000            
unit Is             �A                  
vs.                 <None>              
ts (h:m:s)          0:00:36.0000        
EM (V)              pass                
dQM                 1.960               
unit dQM            �A.h                
record              Ewe                 
dEs (mV)            1.00                
dts (s)             10.0000             
E range min (V)     0.000               
E range max (V)     5.000               
I Range             100 �A              
Bandwidth           5                   
goto Ns'            0                   
nc cycles           0                   

Technique : 5
Modulo Bat
ctrl_type           CC                  
Apply I/C           I                   
current/potential   current             
ctrl1_val           196.000             
ctrl1_val_unit      �A                  
ctrl1_val_vs        <None>              
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
lim_nb              2                   
lim1_type           Ewe                 
lim1_comp           >                   
lim1_Q              Q limit             
lim1_value          1.000               
lim1_value_unit     V                   
lim1_action         Next sequence       
lim1_seq            1                   
lim2_type           Time                
lim2_comp           >                   
lim2_Q              Q limit             
lim2_value          15.000              
lim2_value_unit     mn                  
lim2_action         Next sequence       
lim2_seq            1                   
rec_nb              2                   
rec1_type           Ewe                 
rec1_value          1.000               
rec1_value_unit     mV                  
rec2_type           Time                
rec2_value          10.000              
rec2_value_unit     s                   
E range min (V)     0.000               
E range max (V)     5.000               
I Range             100 �A              
I Range min         Unset               
I Range max         Unset               
I Range init        Unset               
auto rest           1                   
Bandwidth           5                   

Technique : 6
Loop
goto Ne             4                   
nt times            10                  

Technique : 7
Chronopotentiometry
Is                  -196.000            
unit Is             �A                  
vs.                 <None>              
ts (h:m:s)          0:00:36.0000        
EM (V)              pass                
dQM                 1.960               
unit dQM            �A.h                
record              Ewe                 
dEs (mV)            1.00                
dts (s)             10.0000             
E range min (V)     0.000               
E range max (V)     5.000               
I Range             100 �A              
Bandwidth           5                   
goto Ns'            0                   
nc cycles           0                   
