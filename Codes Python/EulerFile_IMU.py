import csv
import numpy as np

####################################################################
## fonction creant le fichier texte pour sauvegarder les donnees  ##
####################################################################

def CSVfilecreation() :
	with open('EulerFile_IMU.txt','w') as csvdoc:
		write = csv.writer(csvdoc)
		csvdoc.close
		
####################################################################		
###### fonction qui compte les lignes d'un fichier texte/tsv #######
####################################################################
		
def Comptagedeligne(fichier) : 
	with open(fichier,'r') as f:
		obj=csv.reader(f)
		compteur=0
		for ligne in obj :
			compteur=compteur+1
	return(compteur)

#####################################################################		
######## fonction permettant d'ecrire dans le fichier texte #########
#####################################################################

def CSVWriter(roll,pitch,yaw) :
	rows = [roll,pitch,yaw]
	with open('EulerFile_IMU.txt','a') as csvdoc:
		write = csv.writer(csvdoc)
		write.writerow(rows)
		csvdoc.close
		
######################################################################
############################# Main ###################################
######################################################################
	
CSVfilecreation()

###### demande a l'utilisateur le nom du fichier texte contenant ##### 
######   les donnees du phidget et la ligne correspondant au t0  #####

print('Entrer le nom du fichier contenant les donnees Euler IMU :')
NomFichier = input()
print('Entrer le numero de la ligne correspondant a t0:')
NumLigneDebut = input()
NumLigneDebut = int(NumLigneDebut)
NumLigneDebut = NumLigneDebut-1

print('Entrer le numero de la ligne correspondant a tf:')
NumLigneFin = input()
NumLigneFin = int(NumLigneFin)
NumLigneFin = NumLigneFin

###### ouverture du fichier en mode lecture pour creation differents #####
######                   vecteurs et remplissage                     #####

with open(NomFichier,'r') as f:
	obj=csv.reader(f)
	compteur=Comptagedeligne(NomFichier)

	roll=np.zeros(compteur-NumLigneDebut-(compteur-NumLigneFin)+1)
	pitch=np.zeros(compteur-NumLigneDebut-(compteur-NumLigneFin)+1)
	yaw=np.zeros(compteur-NumLigneDebut-(compteur-NumLigneFin)+1)
	i=0
	for ligne in obj:
		if i >= NumLigneDebut and i<= NumLigneFin:
			roll[i-NumLigneDebut]=float(ligne[1])
			pitch[i-NumLigneDebut]=float(ligne[2])
			yaw[i-NumLigneDebut]=float(ligne[3])
		i=i+1

### Ecriture dans un fichier des donnees phidgets recuperees ###

for i in range (len(roll)) :
	CSVWriter(roll[i],pitch[i],yaw[i])
