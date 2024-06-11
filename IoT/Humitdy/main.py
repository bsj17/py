from iot_package.sensors import Sensors
import time

# Za ovaj zadatak koristite Simulator koji
# se nalazi u mapi "simulator" - simulator.py.
# Također, kako bi čitali podatke sa senzora potrebno je
# koristiti klasu `Sensors` koja je već uključena u ovoj datoteci.

# Napišite skriptu koja svake sekunde (1s) sa senzora pročita
# temperaturu i vlagu.
# Na temelju pročitanih vrijednosti skripta treba na
# zaslon (display) ispisati pripadajuću poruku.
# Idealna temperatura je u rasponu od 18-24,
# a idealna vlaga u rasponu od 40-60.
# Ako su temperatura i vlaga u idealnom rasponu treba na zaslon ispisati:
#   - "IDEALNO".
# Ako je temperatura izvan raspona treba ispisati:
#   - "GRIJEM" ako je ispod ili "HLADIM" ako je iznad.
# Ako je vlaga izvan raspona treba ispisati:
#   - "OVLAZUJEM" ako je ispod ili "SUSIM" ako je iznad.
# Ako su i temperatura i vlaga izvan raspona potrebno je ispisati obje poruke.
sensors = Sensors()

while True:
    # TODO implementirajte ponašanje IoT uređaja
    if 40 < sensors.get_humidity() < 60:
        print ("Idealno")
    elif (60 < sensors.get_humidity()):
        print('GRIJEM')
    else:
        print('OVLAZUJEM')
    print (str(sensors.get_humidity()))
    time.sleep(1)
