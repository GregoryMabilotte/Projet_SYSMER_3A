import csv
import numpy as np
import pandas as pd

#################################################################################
### fonction creant le fichier texte pour sauvegarder les donnees quaternions ###
#################################################################################

def CSVfilecreation_Quaternion() :
	with open('QuaternionFile_Qualisys.txt','w') as csvdoc:
		write = csv.writer(csvdoc)
		csvdoc.close
		
#################################################################
### fonction creant le fichier texte intermediaire permettant ###
###                 de faire le tri des donnees               ###
#################################################################
		
def CSVfilecreation_EulerTri() :
	with open('QuaternionFile_EulerTri.txt','w') as csvdoc:
		write = csv.writer(csvdoc)
		csvdoc.close
		
########################################################################		
### fonction permettant de compter les lignes d'un fichier texte/tsv ###
########################################################################
		
def Comptagedeligne(fichier) : 
	with open(fichier,'r') as f:
		obj=csv.reader(f)
		compteur=0
		for ligne in obj :
			compteur=compteur+1
	return(compteur)
	
#############################################################################
### fonction permettant d'ecrire dans le fichier contenant les quaternions###
#############################################################################
	
def CSVWriter_QuaternionFile(qx,qy,qz,qw) :
	rows = [qx,qy,qz,qw]
	with open('QuaternionFile_Qualisys.txt','a') as csvdoc:
		write = csv.writer(csvdoc)
		write.writerow(rows)
		csvdoc.close
		
##############################################################		
### fonction permettant d'ecrire dans le fichier contenant ###
###               les donnees Euler triees                 ###
##############################################################
		
def CSVWriter_EulerTri(roll,pitch,yaw) :
	rows = [roll,pitch,yaw]
	with open('QuaternionFile_EulerTri.txt','a') as csvdoc:
		write = csv.writer(csvdoc)
		write.writerow(rows)
		csvdoc.close
		
################################################################################		
### fonction permettant de trier les donnees Euler : Passage de 100 Hz a 4Hz ###
################################################################################
		
		
def TSVFile2EulerTriFile(NomFichierTSV, DataFrameFile,NumLigneDebut, NumLigneFin) : 
	compteur=Comptagedeligne(NomFichierTSV)
	
	reste = (compteur-NumLigneDebut-(compteur-NumLigneFin)+1)%25
	taille= (compteur-NumLigneDebut-(compteur-NumLigneFin)+1-reste)/25
	taille=int(taille)+1

	roll=np.zeros(taille)
	pitch=np.zeros(taille)
	yaw=np.zeros(taille)
	i=0
	for j in range(compteur-1):
		if j >= NumLigneDebut and j<=NumLigneFin:
			if j%25 == 0 : 
			
				roll[i]=float(DataFrameFile.iat[j,5])
				pitch[i]=float(DataFrameFile.iat[j,6])
				yaw[i]=float(DataFrameFile.iat[j,7])
				i=i+1
	
	for i in range (len(roll)) :
		CSVWriter_EulerTri(roll[i],pitch[i],yaw[i])
		
###########################################################################		
###  fonction permettant de passer des angles d'Euler aux quaternions   ###
### Ecriture dans le fichier contenant les donnees Quaternions Qualisys ###
###########################################################################
		
def Euler2Quaternion(roll, pitch, yaw):
	
	Qx = np.sin(roll/2)*np.cos(pitch/2)*np.cos(yaw/2) - np.cos(roll/2)*
		np.sin(pitch/2)*np.sin(yaw/2)
	Qy = np.cos(roll/2)*np.sin(pitch/2)*np.cos(yaw/2) + np.sin(roll/2)*
		np.cos(pitch/2)*np.sin(yaw/2)
	Qz = np.cos(roll/2)*np.cos(pitch/2)*np.sin(yaw/2) - np.sin(roll/2)*
		np.sin(pitch/2)*np.cos(yaw/2)
	Qw = np.cos(roll/2)*np.cos(pitch/2)*np.cos(yaw/2) + np.sin(roll/2)*
		np.sin(pitch/2)*np.sin(yaw/2)
	
	
	CSVWriter_QuaternionFile(Qx,Qy,Qz,Qw)
	
##############################################################		
### fonction permettant de convertir des degres en radians ###
##############################################################
	
def Deg2Rad(Deg_angle):
	Rad_angle=Deg_angle*np.pi/180.00
	return(Rad_angle)
	
#################################################
################### Fonction Main ###############
#################################################

def main():

###  demande a l'utilisateur le nom du fichier texte contenant ###
###   les donnees du phidget et la ligne correspondant au t0   ###

	print('Entrer le nom du fichier contenant les donnees Euler Qualisys:')
	NomFichier = input()
	Fichier=pd.read_csv(NomFichier, sep="\t")
	print('Entrer le numero de la ligne correspondant a t0:')
	NumLigneDebut = input()
	NumLigneDebut = int(NumLigneDebut)
	NumLigneDebut = NumLigneDebut-1
	
	print('Entrer le numero de la ligne correspondant a tf:')
	NumLigneFin = input()
	NumLigneFin = int(NumLigneFin)
	NumLigneFin = NumLigneFin-1
	
### Passe d'un echantillonage 100 Hz a un echantillonage 4Hz ###

	TSVFile2EulerTriFile(NomFichier,Fichier, NumLigneDebut, NumLigneFin)
	
### ouverture du fichier en mode lecture pour creation ###
###          differents vecteurs et remplissage        ###
	
	with open('QuaternionFile_EulerTri.txt','r') as f:
		obj=csv.reader(f)
		compteur1=Comptagedeligne('QuaternionFile_EulerTri.txt')
		print(compteur1)
		
		pitch_1=np.zeros(compteur1)
		roll_1=np.zeros(compteur1)
		yaw_1=np.zeros(compteur1)
		
		i=0
		for ligne in obj:
			roll_1[i]=float(ligne[0])
			pitch_1[i]=float(ligne[1])
			yaw_1[i]=float(ligne[2])
			i=i+1

### passage des angles d'euler aux quaternions et ecriture dans le fichier ###
			
	for i in range (len(roll_1)) :
		Rad_Roll=Deg2Rad(roll_1[i])
		Rad_Pitch=Deg2Rad(pitch_1[i])
		Rad_Yaw=Deg2Rad(yaw_1[i])
	
		Euler2Quaternion(Rad_Roll, Rad_Pitch, Rad_Yaw)
	
##############################################################################
##############################################################################	
	
CSVfilecreation_Quaternion()
CSVfilecreation_EulerTri()
main()
