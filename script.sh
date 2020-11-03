#!/bin/sh

Text_To_Display()
{
echo "###############################################################################"
echo " 										   "
echo "			Choose the option for the necessary Operation"
echo " 										   "
echo "			1. BORDER SECURITY   "
echo " 										   "
echo "			2. BOMB DETECTION       "
echo " 										   "
echo "			3. COLOR DETECTION              "
echo " 										   "
echo "			4. SOLDIER HELATH MONITORING "
echo " 										   "
echo " 									           "
echo "#############################################################################"
}
while :
do
 Text_To_Display
 #echo "Choose option to enter : "
 read INPUT_STRING
 case $INPUT_STRING in 
	1)
		echo "BORDER SECURITY"
		python /home/pi/Desktop/WORKING_CAMOUFLAGE/face_recognition.py
		;;
	2)
	 	echo "BOMB DETECTION"
		python /home/pi/Desktop/WORKING_CAMOUFLAGE/metal.py
		;;
	3)
	 	echo "COLOR DETECTION"
		python /home/pi/Desktop/WORKING_CAMOUFLAGE/color1.py
		;;
	4)
	 	echo "SOLDIER HEALTH MONITORING"
		python /home/pi/Desktop/WORKING_CAMOUFLAGE/health.py
		;;
	q)
	 	echo "Programm is terminated"
		;;
 esac
done 
echo "complete"
