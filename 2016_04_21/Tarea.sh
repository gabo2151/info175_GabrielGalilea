#!/bin/sh
#EL PROGRAMA! :D

# Formato de fecha
# date +"%Y_%m_%d" (YYYY_MM_DD)
fecha_hoy=$(date +"%Y_%m_%d")
#echo "$fecha_hoy"

menu(){
	clear
	echo "##################################"
	echo "#                                #"
	echo "#    ZAFS - Zip A Folder Shell   #"
	echo "#                                #"
	echo "##################################"
	echo "#"
	echo "#    Menu de opciones"
	echo "#"
	echo "#  1) Comprimir carpeta"
	echo "#  0) Salir"
	echo "#"
	echo "#                      $(date +"%d/%m/%Y")"
	echo "##################################"
	echo -n "Elija una opcion: "
	read num
	case $num in
		1) clear; execute_program;;
		0) clear; exit;;
		*) echo "La opcion $num no es valida"; sleep 3; clear; menu;
	esac
}

execute_program(){
	echo -n "Carpeta a respaldar: "
	read res_fold
	echo -n "Carpeta de destino: "
	read des_fold
	zip -r $des_fold/"$fecha_hoy".zip $res_fold
	menu;
}

# Ejecuta menu
while :
do
	menu
done
