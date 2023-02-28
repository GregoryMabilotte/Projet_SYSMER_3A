from Phidget22.Phidget import *
from Phidget22.Devices.Spatial import *
from Phidget22.Devices.TemperatureSensor import *
from Phidget22.Devices.Magnetometer import *
import time
import csv

########################################################################
### fonction creant le fichier texte pour sauvegarder les donnees en ### 
###                     temps reel du phidget 1                      ###
########################################################################

def CSVfilecreation() :
	fields = ['timestamp','pitch', 'roll', 'yaw','QuaternionX',
		'QuaternionY','QuaternionZ','QuaternionW']
	with open('CSVfiletest','w') as csvdoc:
		write = csv.writer(csvdoc)
		write.writerow(fields)
		csvdoc.close
		
		
########################################################################
### fonction creant le fichier texte pour sauvegarder les donnees en ### 
###                     temps reel du phidget 2                      ###
########################################################################
		
def CSVfilecreation1() :
	fields = ['timestamp','pitch', 'roll', 'yaw','QuaternionX',
		'QuaternionY','QuaternionZ','QuaternionW']
	with open('CSVfiletest1','w') as csvdoc:
		write = csv.writer(csvdoc)
		write.writerow(fields)
		csvdoc.close
		
#######################################################################		
### fonction permettant d'ecrire dans le fichier texte du phidget 1 ###
#######################################################################

def CSVWriter(timestamp, pitch, roll, yaw,qx,qy,qz,qw) :
	rows = [timestamp, pitch, roll, yaw,qx,qy,qz,qw]
	with open('CSVfiletest','a') as csvdoc:
		write = csv.writer(csvdoc)
		write.writerow(rows)
		csvdoc.close
		
#######################################################################		
### fonction permettant d'ecrire dans le fichier texte du phidget 2 ###
#######################################################################

def CSVWriter1(timestamp, pitch, roll, yaw,qx,qy,qz,qw) :
	rows = [timestamp, pitch, roll, yaw,qx,qy,qz,qw]
	with open('CSVfiletest1','a') as csvdoc:
		write = csv.writer(csvdoc)
		write.writerow(rows)
		csvdoc.close
		

###########################################################################	
### fonction permettant d'afficher et d'ecrire les donnees du phidget 1 ###
###########################################################################

def onAlgorithmData(self, quaternion, timestamp):
	#print("Timestamp: " + str(timestamp))

	eulerAngles = self.getEulerAngles()

	#print("EulerAngles: ")
	print("\tpitch: " + str(eulerAngles.pitch))
	print("\troll: " + str(eulerAngles.roll))
	print("\theading: " + str(eulerAngles.heading))

	quaternion = self.getQuaternion()
	#print("Quaternion: ")
	#print("\tx: " + str(quaternion.x))
	#print("\ty: " + str(quaternion.y))
	#print("\tz: " + str(quaternion.z))
	#print("\tw: " + str(quaternion.w))
	#print("----------")
	
	
	
	CSVWriter(timestamp,eulerAngles.pitch,eulerAngles.roll,
		eulerAngles.heading,quaternion.x,quaternion.y,
		quaternion.z,quaternion.w)
		
###########################################################################	
### fonction permettant d'afficher et d'ecrire les donnees du phidget 2 ###
###########################################################################	
		
def onAlgorithmData1(self, quaternion, timestamp):
	#print("Timestamp: " + str(timestamp))

	eulerAngles = self.getEulerAngles()

	#print("EulerAngles: ")
	#print("\tpitch: " + str(eulerAngles.pitch))
	#print("\troll1: " + str(eulerAngles.roll))
	#print("\theading: " + str(eulerAngles.heading))

	quaternion = self.getQuaternion()
	#print("Quaternion: ")
	#print("\tx: " + str(quaternion.x))
	#print("\ty: " + str(quaternion.y))
	#print("\tz: " + str(quaternion.z))
	#print("\tw: " + str(quaternion.w))
	#print("----------")
	
	
	
	CSVWriter1(timestamp,eulerAngles.pitch,eulerAngles.roll,
		eulerAngles.heading,quaternion.x,
		quaternion.y,quaternion.z,quaternion.w)
		
############################################################################
############################### Fonction Main ##############################
############################################################################
		
def main():

### Initialisation et association au phidget 1 par son numero de serie ###

	spatial0 = Spatial()
	temperature0=TemperatureSensor()
	magnetometer0=Magnetometer()
	spatial0.setDeviceSerialNumber(373654)
	temperature0.setDeviceSerialNumber(373654)
	magnetometer0.setDeviceSerialNumber(373654)
	
### Initialisation et association au phidget 2 par son numero de serie ###

	spatial1 = Spatial()
	temperature1=TemperatureSensor()
	magnetometer1=Magnetometer()
	spatial1.setDeviceSerialNumber(373141)
	temperature1.setDeviceSerialNumber(373141)
	magnetometer1.setDeviceSerialNumber(373141)
	
### Affichage et ecriture des donnees des phidgets
	
	spatial0.setOnAlgorithmDataHandler(onAlgorithmData)
	spatial1.setOnAlgorithmDataHandler(onAlgorithmData1)
	
### ouverture des channels ###
	
	temperature0.open()
	magnetometer0.open()
	temperature1.open()
	magnetometer1.open()
	spatial0.openWaitForAttachment(1000)
	spatial1.openWaitForAttachment(1000)

### Fixe le Change Trigger pour les magnetos et thermometres ###
###                    des 2 phidgets                        ###

	temperature0.setTemperatureChangeTrigger(0)
	magnetometer0.setMagneticFieldChangeTrigger(0)
	temperature1.setTemperatureChangeTrigger(0)
	magnetometer1.setMagneticFieldChangeTrigger(0)
	
 ### Fixe intervalle d'echantillonage a 100 Hz ###

	spatial0.setDataRate(100)
	spatial1.setDataRate(100)
	#spatial0.setDataInterval(10) # en ms 
	
	

###  Desactive l'utilisation du magnetometre pour        ###
###  simuler un environnment ou le magneto est interdit  ###
	
	spatial0.setAlgorithmMagnetometerGain(0.0000005)
	spatial1.setAlgorithmMagnetometerGain(0.0000005)
	
	
### Ajout d'une fonction appui sur une touche ###
###      pour mettre fin au programme         ###

	try:
		input("Press Enter to Stop\n")
	except (Exception, KeyboardInterrupt):
		pass

### fermeture des channels ###

	temperature0.close()
	magnetometer0.close()
	temperature1.close()
	magnetometer1.close()
	spatial0.close()
	spatial1.close()
	
####################################################################
####################################################################
####################################################################	
	

CSVfilecreation()
CSVfilecreation1()
print("Lancement effectue")
main()

