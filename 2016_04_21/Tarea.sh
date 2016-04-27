#!/bin/bash
#EL PROGRAMA! :D
clear
echo "##################################"
echo "#                                #"
echo "#    ZAFS - Zip A Folder Shell   #"
echo "#                                #"
echo "##################################"

# Formato de fecha
# date +"%Y_%m_%d" (YYYY_MM_DD)
fecha_hoy=$(date +"%Y_%m_%d")
#echo "$fecha_hoy"

echo -n "# Carpeta a respaldar: "
read res_fold
echo -n "# Carpeta de destino: "
read des_fold
zip -r $des_fold/"$fecha_hoy".zip $res_fold