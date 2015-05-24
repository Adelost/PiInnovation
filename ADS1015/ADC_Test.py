from ADS1015 import ADS1015
import time

# Konfiguration fuer den ADC
# Jeder Eintrag steht fuer einen Konfigurationsparameter
# Config[0] = MUX
# Config[1] = PGA
# Config[2] = MODE
# Config[3] = DR
# Config[4] = COMP_MODE
# Config[5] = COMP_POL
# Config[6] = COMP_LAT
# Config[7] = COMP_QUE
Config = [0, 2, 0, 0, 0, 0, 0, 3]

# Adresspin
Addr = 0	

# Modul instantiieren
ADC = ADS1015(Addr)

while True:
	
	# ADC konfigurieren
	ADC.Config(Config)
	
	# ADC auslesen
	print ADC.Read()

	time.sleep(1)