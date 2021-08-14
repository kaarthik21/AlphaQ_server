FROM ubuntu

RUN apt-get update && DEBIAN_FRONTEND="noninteractive" TZ="Asia/India" apt-get install -y tzdata 
RUN apt-get install cron -y && apt-get install vim -y
RUN apt-get install acl -y && apt-get install python3 -y && apt-get install mysql-server -y
RUN apt install -y python3-pip && pip3 install pymysql && apt-get install apache2 -y  


WORKDIR /server
COPY scripts /server/
#COPY bashrc_server /server/
#COPY attendance.log future.txt /server/
#COPY crontab-schedule.txt /var/spool/crontabs/crontab-schedule.txt
#COPY db.py /server/
#COPY moms.php /var/www/html/moms.local/moms.php
#COPY config.php /var/www/html/moms.local/config.php
#COPY cookie.php /var/www/html/moms.local/cookie.php

RUN chmod 644 /server/bashrc_server
RUN cat bashrc_server >> /root/.bashrc
#RUN chmod +x  /var/spool/crontabs/crontab-schedule.txt

RUN chmod +x /server/*
RUN mkdir /var/www/html/moms.local/
RUN mv /server/moms.php /var/www/html/moms.local/moms.php
RUN mv /server/config.php /var/www/html/moms.local/config.php
RUN mv /server/cookie.php /var/www/html/moms.local/cookie.php
RUN mv /server/insert.php /var/www/html/moms.local/insert.php

RUN service mysql start
#RUN echo 'ALTER USER 'root'@'localhost' IDENTIFIED WITH caching_sha2_password BY 'root';' | mysql
#RUN service mysql restart && echo "CREATE DATABASE Minutesofmeeting;" | mysql -u root -proot

RUN bash /server/initialsetup.sh
#RUN /var/spool/crontabs/crontab-schedule.txt
#RUN /server/schedule.sh
#RUN /server/attendance.sh



