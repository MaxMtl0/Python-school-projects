import pyfirmata # Importer pyFirmata
import time # Importer le temps

port = 'COM14'# Windows
#port = '/dev/ttyACM3' # Linux
#port = '/dev/tty.usbmodem11401'# Mac

HIGH = True# Crée un état haut qui correspond à la led allumée
LOW = False # Crée un état bas qui correspond à la led éteinte
board = pyfirmata.Arduino(port) # Initialise la communication avec la carte
LED_pin = board.get_pin('d:13:o') # Initialise la broche (d => digital, 13 => N° broche, o => output)

for i in range(10): # Permet de faire clignoter la micro-led dix fois
    LED_pin.write(HIGH) # Allume la led
    time.sleep(0.5) # Pause de 0.5 seconde
    LED_pin.write(LOW) # Eteint la led
    time.sleep(0.5) # Nouvelle pause de 0.5 seconde

board.exit() # Clôture la communication avec la carte


import pyfirmata # Importer pyFirmata
import time # Importer le temps

port = 'COM14'# Windows
#port = '/dev/ttyACM3' # Linux
#port = '/dev/tty.usbmodem11401' # Mac

HIGH = True# Crée un état haut qui correspond à la Led allumé
LOW = False # Pareil pour l’état bas

board = pyfirmata.Arduino(port) # Initialise la communication avec la carte
LED_pin = board.get_pin('d:12:o') # Initialise la broche (d => digital, 8 => N° broche, o => output)

for i in range(10): # Permet de faire clignoter la micro-led dix fois
    LED_pin.write(HIGH)# Allume la led
    time.sleep(0.2) # Pause de 2 secondes
    LED_pin.write(LOW) # Eteint la led
    time.sleep(0.2) # Nouvelle pause de 2 secondes

board.exit() # Clôture la communication avec la carte







import pyfirmata

import time

port = 'COM14' # Windows à adapter par rapport à votre ordinateur

board = pyfirmata.Arduino(port) # Permet d’ouvrir le port associé

Sensor_pin = board.get_pin('a:13:o') # Permet d’initialiser la broche utilisée

iterator = pyfirmata.util.Iterator(board) # Permet d’initialiser la liaison entre Python et Arduino

iterator.start() # Démarrage de la connexion

Sensor_pin.enable_reporting() # Lecture des valeurs de la broche choisie

while Sensor_pin.read() == None: #None # Tant qu’il n’y a pas de valeurs
    try:
        while True:
            print ("La valeur est : ",Sensor_pin.read()) # Lit et affiche les valeurs de la broche
            time.sleep(1) # Pause entre deux mesures
    except:
            Sensor_pin.disable_reporting() # Arrête la lecture de la broche
            board.exit()

