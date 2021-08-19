# alphaQ_server

### TO BUILD THE IMAGES: docker-compose build
### TO RUN THE CONTAINERS: docker-compose up -d
### TO GET IN alphaq_server CONTAINER WITH INTERACTIVE TERMINAL: docker exec -it alphaq_server bash
### TO GET IN mysql_docker CONTAINER WITH INTERACTIVE TERMINAL: docker exec -it mysql_docker bash
#
#
### Inside alphaq_server container
####  mv crontab-schedule.txt /var/spool/cron/crontabs/crontab-schedule.txt
#### ./schedule.sh
#### ./attendance.sh (with both y and n options)
#### ./genMoM_1.sh
#### ./getMoM_2.sh
#
### In the host shell
#### docker cp alphaq_server:/home/Jay_Jay/MoM.txt /tmp/MoM.txt
#### docker cp /tmp/MoM.txt mysql_docker:/var/lib/mysql-files/MoM.txt
#
### Inside mysql in mysql_docker container, run below commands if permission is denied 
#### CREATE USER 'root'@'localhost' IDENTIFIED BY 'root';
#### GRANT ALL PRIVILEGES ON **.* TO 'root'@'localhost' WITH GRANT OPTION;
#### CREATE USER 'root'@'%' IDENTIFIED BY 'root';
#### GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' WITH GRANT OPTION;
#### FLUSH PRIVILEGES;
#
### Inside alphaq_server container
#### python3 db.py
#### pip install cryptography
#### mv moms.local.conf /etc/apache2/sites-available/moms.local.conf
#### cd /etc/apache2/sites-available/
#### a2dissite 000-default.conf
#### a2ensite moms.local.conf
#### service apache2 start
#
#### Browse [IP_ADDR of docker]:[port of the container]/config.php to get the MoM login page
