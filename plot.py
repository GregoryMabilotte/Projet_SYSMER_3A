import csv
import numpy as np
import matplotlib as mp
import matplotlib.pyplot as plt

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
	
##########################################################################
############################  Fonction Main ##############################
##########################################################################

def main() :

### demande a l'utilisateur le nom du fichier texte contenant ###
###                 les donnees pour les courbes              ###

	print('Entrer le nom du fichier :')
	NomFichier = input()
	
### ouverture du fichier en mode lecture pour creation ###
###       differents vecteurs et leur remplissage      ###

	with open(NomFichier,'r') as f:
		obj=csv.reader(f)
		compteur=Comptagedeligne(NomFichier)
		timestamp=np.zeros(compteur-1)
		pitch=np.zeros(compteur-1)
		roll=np.zeros(compteur-1)
		yaw=np.zeros(compteur-1)
		QuaternionX=np.zeros(compteur-1)
		QuaternionY=np.zeros(compteur-1)
		QuaternionZ=np.zeros(compteur-1)
		QuaternionW=np.zeros(compteur-1)
		i=0
		for ligne in obj:
			if i !=0:
				
				#tps en secondes
				timestamp[i-1]=float(ligne[0])/1000 
				
				# recuperation des donnees
				
				pitch[i-1]=float(ligne[1])
				roll[i-1]=float(ligne[2])
				yaw[i-1]=float(ligne[3])
				#QuaternionX[i-1]=float(ligne[4])
				#QuaternionY[i-1]=float(ligne[5])
				#QuaternionZ[i-1]=float(ligne[6])
				#QuaternionW[i-1]=float(ligne[7])
			i=i+1
	
	# trace des differentes courbes
	
	plt.plot(timestamp,pitch)
	plt.xlabel("time(s)")
	plt.ylabel("pitch(deg)")
	plt.title("Pitch")
	plt.savefig("Pitch.png")
	plt.show()
	
	plt.plot(timestamp,roll)
	plt.xlabel("time(s)")
	plt.ylabel("roll(deg)")
	plt.title("Roll")
	plt.savefig("Roll.png")
	plt.show()
	
	plt.plot(timestamp,yaw)
	plt.xlabel("time(s)")
	plt.ylabel("yaw(deg)")
	plt.title("Yaw")
	plt.savefig("Yaw.png")
	plt.show()

##################################################################
##################################################################
##################################################################
		
main()
