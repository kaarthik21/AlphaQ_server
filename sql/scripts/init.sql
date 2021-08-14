ALTER USER 'root'@'localhost' IDENTIFIED WITH caching_sha2_password BY 'root';
flush privileges;
CREATE DATABASE IF NOT EXISTS Minutesofmeeting;
use Minutesofmeeting;
