import csv
import numpy as np
import pandas as pd

##################################################################################
### fonction creant le fichier texte pour sauvegarder les donnees quaternions  ###
##################################################################################

def CSVfilecreation_Rot() :
	with open('RotFile_Qualisys.txt','w') as csvdoc:
		write = csv.writer(csvdoc)
		csvdoc.close
		
		
##########################################################################		
###fonction permettant de compter les lignes d'un fichier texte ou tsv ###
##########################################################################
		
def Comptagedeligne(fichier) : 
	with open(fichier,'r') as f:
		obj=csv.reader(f)
		compteur=0
		for ligne in obj :
			compteur=compteur+1
	return(compteur)
	
############################################################################		
### fonction permettant d'ecrire dans le fichier contenant les rotations ###
############################################################################
	
def CSVWriter_RotFile(rot0,rot1,rot2,rot3,rot4,rot5,rot6,rot7,rot8) :
	rows = [rot0,rot1,rot2,rot3,rot4,rot5,rot6,rot7,rot8]
	with open('RotFile_Qualisys.txt','a') as csvdoc:
		write = csv.writer(csvdoc)
		write.writerow(rows)
		csvdoc.close
		
###########################################################		
### Recuperation des donnees des matrices de rotations  ###
###########################################################
		
		
def TSVFile2RotFile(NomFichierTSV, DataFrameFile,NumLigneDebut, NumLigneFin) : 
	
	compteur=Comptagedeligne(NomFichierTSV)
	
	reste = (compteur-NumLigneDebut-(compteur-NumLigneFin)+1)%25
	taille= (compteur-NumLigneDebut-(compteur-NumLigneFin)+1-reste)/25
	taille=int(taille)+1

	rot0=np.zeros(taille)
	rot1=np.zeros(taille)
	rot2=np.zeros(taille)
	rot3=np.zeros(taille)
	rot4=np.zeros(taille)
	rot5=np.zeros(taille)
	rot6=np.zeros(taille)
	rot7=np.zeros(taille)
	rot8=np.zeros(taille)
	i=0
	for j in range(compteur-1):
		if j >= NumLigneDebut and j<=NumLigneFin:
			if j%25 == 0 : 
			
				rot0[i]=float(DataFrameFile.iat[j,9])
				rot1[i]=float(DataFrameFile.iat[j,10])
				rot2[i]=float(DataFrameFile.iat[j,11])
				rot3[i]=float(DataFrameFile.iat[j,12])
				rot4[i]=float(DataFrameFile.iat[j,13])
				rot5[i]=float(DataFrameFile.iat[j,14])
				rot6[i]=float(DataFrameFile.iat[j,15])
				rot7[i]=float(DataFrameFile.iat[j,16])
				rot8[i]=float(DataFrameFile.iat[j,17])
				i=i+1
	
	for i in range (len(rot0)) :
		CSVWriter_RotFile(rot0[i],rot1[i],rot2[i],rot3[i],
		rot4[i],rot5[i],rot6[i],rot7[i],rot8[i])
	
###################################
######### Fonction Main ###########
###################################

def main():

##  demande a l'utilisateur le nom du fichier texte contenant les ###
##	    donnees du phidget et la ligne correspondant au t0	###

	print('Entrer le nom du fichier contenant les donnees Rot Qualisys:')
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
	
### Ecriture des rot dans le fichier ###

	TSVFile2RotFile(NomFichier,Fichier, NumLigneDebut, NumLigneFin)

	
##################################################################################
##################################################################################	
	
CSVfilecreation_Rot()
main()
