clear all
clc


%Chargement des fichiers contenant les donnees Euler IMU et Qualisys

RotMatrix_Qualisys=load("NEW1_4_Qualisys.mat");
RotMatrix_Qualisys=RotMatrix_Qualisys.M_fin_Q;

RotMatrix_IMU=load("NEW1_4_IMU.mat");
RotMatrix_IMU=RotMatrix_IMU.M_IMU_fin_new;

% Coordonnees des differents points de A a H de la modelisation du phidget

A_Q = [0 ; 0 ; 0];
B_Q = [1 ; 0 ; 0];
C_Q = [1 ; 1 ; 0];
D_Q = [0 ; 1 ; 0];
E_Q = [0 ; 0 ; 1];
F_Q = [1 ; 0 ; 1];
G_Q = [1 ; 1 ; 1];
H_Q = [0 ; 1 ; 1];

A_IMU = [0 ; 0 ; 0];
B_IMU = [1 ; 0 ; 0];
C_IMU = [1 ; 1 ; 0];
D_IMU = [0 ; 1 ; 0];
E_IMU = [0 ; 0 ; 1];
F_IMU = [1 ; 0 ; 1];
G_IMU = [1 ; 1 ; 1];
H_IMU = [0 ; 1 ; 1];

At_Q=transpose(A_Q);
Bt_Q=transpose(B_Q);
Ct_Q=transpose(C_Q);
Dt_Q=transpose(D_Q);
Et_Q=transpose(E_Q);
Ft_Q=transpose(F_Q);
Gt_Q=transpose(G_Q);
Ht_Q=transpose(H_Q);

At_IMU=transpose(A_IMU);
Bt_IMU=transpose(B_IMU);
Ct_IMU=transpose(C_IMU);
Dt_IMU=transpose(D_IMU);
Et_IMU=transpose(E_IMU);
Ft_IMU=transpose(F_IMU);
Gt_IMU=transpose(G_IMU);
Ht_IMU=transpose(H_IMU);

% Matrices contenant les points et les numeros des points permettant
% de construire chaque face

Points_IMU = [At_IMU;Bt_IMU;Ct_IMU;Dt_IMU;Et_IMU;Ft_IMU;Gt_IMU;Ht_IMU];
Points_Qualisys=[At_Q;Bt_Q;Ct_Q;Dt_Q;Et_Q;Ft_Q;Gt_Q;Ht_Q];
Faces_IMU = [1 2 6 5; 2 3 7 6; 3 4 8 7; 4 1 5 8 ; 1 2 3 4; 5 6 7 8];
Faces_Qualisys = [1 2 6 5; 2 3 7 6; 3 4 8 7; 4 1 5 8 ; 1 2 3 4; 5 6 7 8];


nbIm = min(length(RotMatrix_IMU),length(RotMatrix_Quaternion));

%%%%%%% Calcul pour toutes les matrices de rotations dont on dispose %%%%%%

for i =1:nbIm

    idx=int2str(i);
    MatRot_Qualisys=RotMatrix_Qualisys(:,:,i);
    MatRot_IMU=RotMatrix_IMU(:,:,i);

%%%%%%%% Calcul de la rotation au nouvel instant du pdv Qualisys %%%%%%%%%%

    A_Q=MatRot_Qualisys*A_Q;
    B_Q=MatRot_Qualisys*B_Q;
    C_Q=MatRot_Qualisys*C_Q;
    D_Q=MatRot_Qualisys*D_Q;
    E_Q=MatRot_Qualisys*E_Q;
    F_Q=MatRot_Qualisys*F_Q;
    G_Q=MatRot_Qualisys*G_Q;
    H_Q=MatRot_Qualisys*H_Q;

    At_Q=transpose(A_Q);
    Bt_Q=transpose(B_Q);
    Ct_Q=transpose(C_Q);
    Dt_Q=transpose(D_Q);
    Et_Q=transpose(E_Q);
    Ft_Q=transpose(F_Q);
    Gt_Q=transpose(G_Q);
    Ht_Q=transpose(H_Q);

    Points_Qualisys =[At_Q;Bt_Q;Ct_Q;Dt_Q;Et_Q;Ft_Q;Gt_Q;Ht_Q];

%%%%%%%% Calcul de la rotation au nouvel instant du pdv Phidget %%%%%%%%%%%

    A_IMU=MatRot_IMU*A_IMU;
    B_IMU=MatRot_IMU*B_IMU;
    C_IMU=MatRot_IMU*C_IMU;
    D_IMU=MatRot_IMU*D_IMU;
    E_IMU=MatRot_IMU*E_IMU;
    F_IMU=MatRot_IMU*F_IMU;
    G_IMU=MatRot_IMU*G_IMU;
    H_IMU=MatRot_IMU*H_IMU;

    At_IMU=transpose(A_IMU);
    Bt_IMU=transpose(B_IMU);
    Ct_IMU=transpose(C_IMU);
    Dt_IMU=transpose(D_IMU);
    Et_IMU=transpose(E_IMU);
    Ft_IMU=transpose(F_IMU);
    Gt_IMU=transpose(G_IMU);
    Ht_IMU=transpose(H_IMU);

    Points_IMU =[At_IMU;Bt_IMU;Ct_IMU;Dt_IMU;Et_IMU;Ft_IMU;Gt_IMU;Ht_IMU];

%%%%%%%%%%%% Deplacement du phidget du point de vue Phidget %%%%%%%%%%%%%%%

    f_IMU=figure();
    plot3(Points_IMU(:,1),Points_IMU(:,2),Points_IMU(:,3),'black')
    hold on
    scatter3(Points_IMU(1,1),Points_IMU(1,2),Points_IMU(1,3),...
        'black','filled') 
    hold on
    scatter3(Points_IMU(4,1),Points_IMU(4,2),Points_IMU(4,3),'b','filled') 
    hold on
    scatter3(Points_IMU(2,1),Points_IMU(2,2),Points_IMU(2,3),'g','filled') 
    hold on
    
    patch('Vertices',Points_IMU,'Faces',Faces_IMU,...
        'FaceVertexCData',hsv(6),'FaceColor','flat')
    hold off
    
    axis([ -2  2    -2  2    -2  2])
    xlabel('x','FontSize',10)
    ylabel('y','FontSize',10)
    zlabel('z','FontSize',10)
    grid on

    saveas(f_IMU,"imageIMU3_"+idx,'png')

    close(f_IMU)

%%%%%%%%%%%% Deplacement du phidget du point de vue Qualisys %%%%%%%%%%%%%%

    f_Qualisys=figure();
    plot3(Points_Qualisys(:,1),Points_Qualisys(:,2),...
        Points_Qualisys(:,3),'black')
    hold on
    scatter3(Points_Qualisys(1,1),Points_Qualisys(1,2),...
        Points_Qualisys(1,3),'black','filled') 
    hold on
    scatter3(Points_Qualisys(4,1),Points_Qualisys(4,2),...
        Points_Qualisys(4,3),'b','filled') 
    hold on
    scatter3(Points_Qualisys(2,1),Points_Qualisys(2,2),...
        Points_Qualisys(2,3),'g','filled') 
    hold on
    
    patch('Vertices',Points_Qualisys,'Faces',Faces_Qualisys,...
        'FaceVertexCData',hsv(6),'FaceColor','flat')
    hold off
    
    axis([ -2  2    -2  2    -2  2])
    xlabel('x','FontSize',10)
    ylabel('y','FontSize',10)
    zlabel('z','FontSize',10)
    grid on

    saveas(f_Qualisys,"imageQualisys3_"+idx,'png')

    close(f_Qualisys)

end

%%%%%%%%%%%%%%%%%%%%%%%%%%% Creation de la video %%%%%%%%%%%%%%%%%%%%%%%%%%

filename = 'Video_4_3.gif';


f = figure();
for idx = 1:nbIm
    

    im = imread("imageIMU3_"+idx+".png");
    subplot(121)
    imshow(im)
    title("IMU")
    
    im = imread("imageQualisys3_"+idx+".png");
    subplot(122)
    imshow(im)
    title("Qualisys")

    frame = getframe(f);
    frame = frame2im(frame);

    pause(1)

    [A,map] = rgb2ind(frame,256);
    if idx == 1
        imwrite(A,map,filename,'gif','LoopCount',Inf,'DelayTime',1);
        imwrite(A,map,filename,'gif','WriteMode','append','DelayTime',1);
    else
        imwrite(A,map,filename,'gif','WriteMode','append','DelayTime',1);
    end
end

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%