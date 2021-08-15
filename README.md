# alphaQ_server
### Inside alphaq_server container
#
####  mv crontab-schedule.txt /var/spool/crontabs/crontab-schedule.txt
#### ./schedule.sh
#### ./attendance.sh (with both y and n options)
#### ./genMoM_1.sh
#### ./getMoM_2.sh
#
### In the host shell
#### docker cp alphaq_server:/home/Jay_Jay/MoM.txt /tmp/MoM.txt
#### docker cp /tmp/MoM.txt mysql_docker:/var/lib/mysql-files/MoM.txt
