clear
clc
close all


%%% Chargement des donnees %%%

%--IMU--% Chargement des quaternions IMU
data_IMU=load("IMU_PlanSol_Baton_Lent_4.txt");
n=length(data_IMU(:,1));
%--Qualisys--% Chargement des matrices de rotation Qualisys
data_Q=load("RotFile_Qualisys_4.txt");
m=length(data_Q(:,1));


%%% Matrices de rotation initiales %%%

%--IMU--%
quat0_IMU=data_IMU(1,:);
w_i0=quat0_IMU(4);
x_i0=quat0_IMU(1);
y_i0=quat0_IMU(2);
z_i0=quat0_IMU(3);

M0_IMU = [w_i0*w_i0+x_i0*x_i0-y_i0*y_i0-z_i0*z_i0 2*x_i0*y_i0-2*w_i0*z_i0 ...
    2*w_i0*y_i0+2*x_i0*z_i0;
     2*w_i0*z_i0+2*x_i0*y_i0 w_i0*w_i0-x_i0*x_i0+y_i0*y_i0-z_i0*z_i0 ...
     2*y_i0*z_i0-2*w_i0*x_i0;
     2*x_i0*z_i0-2*w_i0*y_i0 2*w_i0*x_i0+2*y_i0*z_i0 ...
     w_i0*w_i0-x_i0*x_i0-y_i0*y_i0+z_i0*z_i0];

M0_IMU=transpose(M0_IMU); 
        %il faut transposer pour avoir wi R i0

%--Qualisys--%
M0_Q=[data_Q(1,1) data_Q(1,4) data_Q(1,7);
         data_Q(1,2) data_Q(1,5) data_Q(1,8);  
         data_Q(1,3) data_Q(1,6) data_Q(1,9)]; 
        %pas besoin de transposee car on a deja wq R q0


%%% Matrices de rotation courantes %%%

%--IMU--%
M_IMU=zeros(3,3,n-1); %on ne prend pas la 1e valeur car c'est M0_IMU

for i=2:n
    w_i=data_IMU(i,4);
    x_i=data_IMU(i,1);
    y_i=data_IMU(i,2);
    z_i=data_IMU(i,3);

    R_IMU = [w_i*w_i+x_i*x_i-y_i*y_i-z_i*z_i 2*x_i*y_i-2*w_i*z_i ...
        2*w_i*y_i+2*x_i*z_i;
         2*w_i*z_i+2*x_i*y_i w_i*w_i-x_i*x_i+y_i*y_i-z_i*z_i ...
         2*y_i*z_i-2*w_i*x_i;
         2*x_i*z_i-2*w_i*y_i 2*w_i*x_i+2*y_i*z_i ...
         w_i*w_i-x_i*x_i-y_i*y_i+z_i*z_i];
    
    M_IMU(:,:,i-1)=R_IMU; %i R wi
end

%--Qualisys--%
M_Q=zeros(3,3,m-1); %on ne prend pas la 1e valeur car c'est M0_Q
 
 for i=2:m
     R_Q=[data_Q(i,1) data_Q(i,2) data_Q(i,3);
         data_Q(i,4) data_Q(i,5) data_Q(i,6); 
         data_Q(i,7) data_Q(i,8) data_Q(i,9)]; 
          %on prend la transposee pour avoir q R wq

     M_Q(:,:,i-1)=R_Q;
 end


%%% Multiplications des matrices %%%

M_fin_IMU=zeros(3,3,n-1);
for i=1:n-1
    M_fin_IMU(:,:,i)=M_IMU(:,:,i)*M0_IMU(:,:);
end

M_fin_Q=zeros(3,3,m-1);
for i=1:m-1
    M_fin_Q(:,:,i)=M_Q(:,:,i)*M0_Q(:,:);
end

%%% Suppression des donnees en trop %%%

if n<m  % si il y a plus de données Qualisys
    M_Q_fin_new=zeros(3,3,n-1);
    for i=1:n-1
        M_Q_fin_new(:,:,i)=M_fin_Q(:,:,i);
    end
    num_val=n;
    save("NEW1_4_IMU.mat","M_fin_IMU")
    save("NEW1_4_Qualisys.mat","M_Q_fin_new")

else    % si il y a plus de donnees IMU
    M_IMU_fin_new=zeros(3,3,m-1);
    for i=1:m-1
        M_IMU_fin_new(:,:,i)=M_fin_IMU(:,:,i);
    end
    num_val=m;
     save("NEW1_4_IMU.mat","M_IMU_fin_new")
     save("NEW1_4_Qualisys.mat","M_fin_Q")
end
