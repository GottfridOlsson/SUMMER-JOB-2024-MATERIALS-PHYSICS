EC-LAB SETTING FILE

Number of linked techniques : 4

EC-LAB for windows v11.52 (software)
Internet server v11.52 (firmware)
Command interpretor v11.50 (firmware)

Filename : C:\Users\kmf\Documents\EC-Lab\Data\Gottfrid\2024-04-26_JP-measurements_M-cell\2024-04-26_JP-measurements_sample-A6-02_M-cell_Cu-Li-Cellgard2400-separator_25muL-LiFSI-in-DME_outside-glovebox_sigma-0.02_added-OCV-0.1s_Deltax110.1mm.mps

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
Electrode surface area : 0.196 cm²
Characteristic mass : 0.001 g
Equivalent Weight : 0.000 g/eq.
Density : 0.000 g/cm3
Volume (V) : 0.001 cm³
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
Ns                  0                   1                   
ctrl_type           CV                  CV                  
Apply I/C           I                   I                   
current/potential   current             current             
ctrl1_val           0.010               0.010               
ctrl1_val_unit      V                   V                   
ctrl1_val_vs        Ref                 Ref                 
ctrl2_val           0.000               0.000               
ctrl2_val_unit                                              
ctrl2_val_vs                                                
ctrl3_val           0.000               0.000               
ctrl3_val_unit                                              
ctrl3_val_vs                                                
N                   0.00                0.00                
charge/discharge    Charge              Charge              
charge/discharge_1  Charge              Charge              
Apply I/C_1         I                   I                   
N1                  0.00                0.00                
ctrl4_val           0.000               0.000               
ctrl4_val_unit                                              
ctrl5_val           0.000               0.000               
ctrl5_val_unit                                              
ctrl_tM             0                   0                   
ctrl_seq            0                   0                   
ctrl_repeat         0                   0                   
ctrl_trigger        Falling Edge        Falling Edge        
ctrl_TO_t           0.000               0.000               
ctrl_TO_t_unit      d                   d                   
ctrl_Nd             6                   6                   
ctrl_Na             2                   2                   
ctrl_corr           0                   0                   
lim_nb              1                   2                   
lim1_type           Time                |I|                 
lim1_comp           >                   <                   
lim1_Q              Q limit             I limit             
lim1_value          5.000               39.200              
lim1_value_unit     s                   µA                  
lim1_action         Next sequence       Next sequence       
lim1_seq            1                   2                   
lim2_type           Time                Time                
lim2_comp           >                   >                   
lim2_Q              Q limit             Q limit             
lim2_value          16.000              2.000               
lim2_value_unit     h                   d                   
lim2_action         Next sequence       Next sequence       
lim2_seq            1                   2                   
rec_nb              2                   2                   
rec1_type           I                   I                   
rec1_value          50.000              50.000              
rec1_value_unit     µA                  µA                  
rec2_type           Time                Time                
rec2_value          10.000              10.000              
rec2_value_unit     s                   s                   
E range min (V)     -1.000              -1.000              
E range max (V)     3.500               3.500               
I Range             Auto                Auto                
I Range min         10 µA               10 µA               
I Range max         10 mA               10 mA               
I Range init        10 µA               10 µA               
auto rest           1                   1                   
Bandwidth           5                   5                   

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
Is                  -1.960              
unit Is             mA                  
vs.                 <None>              
ts (h:m:s)          0:03:0.0000         
EM (V)              pass                
dQM                 98.000              
unit dQM            µA.h                
record              Ewe                 
dEs (mV)            1.00                
dts (s)             5.0000              
E range min (V)     -1.000              
E range max (V)     3.500               
I Range             1 mA                
Bandwidth           5                   
goto Ns'            0                   
nc cycles           0                   
