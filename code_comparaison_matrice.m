clear
clc
close all


%%% Recuperation des matrices de rotation %%%

IMU=load('NEW1_1_IMU.mat');
Q=load('NEW1_1_Qualisys.mat');

M_IMU=IMU.M_IMU_fin_new;
M_Q=Q.M_fin_Q;


%%% Initialisation %%%

n=length(M_Q);
ecart=zeros(3,3);
compteur_mauvais=0;
compteur_bon=0;

esp=0.1; %ecart maximal accepte


%%% Comparaison des matrices %%%

for k=1:n
    for i=1:3
        for j=1:3
            ecart(i,j)=abs(M_IMU(i,j,k)-M_Q(i,j,k));
            if ecart(i,j)>esp
                compteur_mauvais=compteur_mauvais+1;
            else
                compteur_bon=compteur_bon+1;
            end
        end
    end
    ecart;
end

erreur=compteur_mauvais*100/(n*9) %pourcentage de valeurs hors tolerance
bon=compteur_bon*100/(n*9) %pourcentage de valeurs considerees egales



