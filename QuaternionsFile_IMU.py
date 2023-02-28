import csv
import numpy as np

######################################################################
### fonction creant le fichier texte pour sauvegarder les donnees  ###
######################################################################

def CSVfilecreation() :
	with open('QuaternionFile_IMU.txt','w') as csvdoc:
		write = csv.writer(csvdoc)
		csvdoc.close
		
###########################################################################		
### fonction permettant de compter les lignes d'un fichier texte ou tsv ###
###########################################################################
		
def Comptagedeligne(fichier) : 
	with open(fichier,'r') as f:
		obj=csv.reader(f)
		compteur=0
		for ligne in obj :
			compteur=compteur+1
	return(compteur)

##########################################################		
### fonction permettant d'ecrire dans le fichier texte ###
##########################################################

def CSVWriter(qx,qy,qz,qw) :
	rows = [qx,qy,qz,qw]
	with open('QuaternionFile_IMU.txt','a') as csvdoc:
		write = csv.writer(csvdoc)
		write.writerow(rows)
		csvdoc.close
		
######################################################
######################## Main ########################
######################################################
		
CSVfilecreation()

#####  demande a l'utilisateur le nom du fichier texte contenant ###
#####  les donnees du phidget et la ligne correspondant au t0    ###

print('Entrer le nom du fichier contenant les donnees quaternions IMU :')
NomFichier = input()
print('Entrer le numero de la ligne correspondant a t0:')

NumLigneDebut = input()
NumLigneDebut = int(NumLigneDebut)
NumLigneDebut = NumLigneDebut-1

### ouverture du fichier en mode lecture pour creation ###
###        differents vecteurs et remplissage          ###

with open(NomFichier,'r') as f:
	obj=csv.reader(f)
	compteur=Comptagedeligne(NomFichier)

	QuaternionX=np.zeros(compteur-NumLigneDebut)
	QuaternionY=np.zeros(compteur-NumLigneDebut)
	QuaternionZ=np.zeros(compteur-NumLigneDebut)
	QuaternionW=np.zeros(compteur-NumLigneDebut)
	i=0
	for ligne in obj:
		if i >= NumLigneDebut:
			QuaternionX[i-NumLigneDebut]=float(ligne[4])
			QuaternionY[i-NumLigneDebut]=float(ligne[5])
			QuaternionZ[i-NumLigneDebut]=float(ligne[6])
			QuaternionW[i-NumLigneDebut]=float(ligne[7])
		i=i+1

### Ecriture dans un fichier des donnees phidgets recuperees ###

for i in range (len(QuaternionX)) :
	CSVWriter(QuaternionX[i],QuaternionY[i],QuaternionZ[i],QuaternionW[i])
	
