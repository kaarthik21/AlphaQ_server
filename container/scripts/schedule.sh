#! /bin/bash


s=$(date -I) 

if grep "$s" /server/future.txt; then 
	echo “DATE    TIME”> /home/Jay_Jay/schedule.txt
	grep -hnr “$s” /server/future.txt > /home/Jay_Jay/schedule.txt
	for i in {01..30}; do
		echo "date    time" > /home/sysAd_$i/schedule.txt
		echo "date    time" > /home/webDev_$i/schedule.txt
		echo "date    time" > /home/appDev_$i/schedule.txt
		grep -hnr "$s" /server/future.txt > /home/sysAd_$i/schedule.txt 
		grep -hnr "$s" /server/future.txt > /home/webDev_$i/schedule.txt 
		grep -hnr "$s" /server/future.txt > /home/appDev_$i/schedule.txt
	done

else
	echo “DATE    TIME” > /home/Jay_Jay/schedule.txt
	for j in {01..30}; do
		echo "$j"
	  	echo "date    time" > /home/sysAd_"$j"/schedule.txt
		echo "date    time" > /home/webDev_"$j"/schedule.txt
  		echo "date    time" > /home/appDev_"$j"/schedule.txt
  	done
fi

echo "Schedule for meetings updated"




