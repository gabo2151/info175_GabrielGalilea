#!/bin/bash
#EL PROGRAMA! :D
clear
echo "##################################"
echo "#                                #"
echo "#    ZAFS - Zip A Folder Shell   #"
echo "#                                #"
echo "##################################"

echo -n "# Carpeta a respaldar: "
read res_fold
echo -n "# Carpeta de destino: "
read des_fold
zip -r $des_fold/file_name.zip $res_fold