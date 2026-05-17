# working with containers

1. Run mysql image
[Mysql Image](https://hub.docker.com/_/mysql?xk=ShowRecommendedBadge&xt=Enabled)

```bash
sudo docker run --name mysqldb -e MYSQL_ROOT_PASSWORD=123456 -d mysql
# mysql is the name of the image
# -e MYSQL_ROOT_PASSWORD=123456 (set root password as environment var)
# --name mysqldb name of the container
# -d for detached mode
# if image not available locally it will pull from DockerHub
# check logs of container
sudo docker logs mysqldb
# I want to do inside this container to work with DB
sudo docker exec -it mysqldb bash
# -it for interactive terminal
#  you will be inside bash terminal of container
# inside terminal 
mysql --version # you can see mysql version
mysql -u root -p # connect with DB
# enter root password which you have set as an environment variable
# now you will be connected with DB
create database pw;
show databases; # you can see some inbuilt and your created DB
use pw;
create table student (id int, name varchar(20)); # create table
insert into student (id,name) values (1,'Sonam Soni'); # insert Data
select * from student; # retrieve Data
exit # this exits from DB connection
exit # this exits from container
```
### Quck Task
- create Jenkins Container

```bash
sudo docker run -d --name jenkinsapp -p 8082:8080 jenkins/jenkins
# access localhost:8082
# check logs to get password and setup jenkins
sudo docker logs jenkinsapp
# copy password
# enter browser and continue installation
sudo docker rm jenkinsapp
```

## Image creation

- let's say I wnat to run my application as container
- means I need an image of my application to run
- for that we have to create an image
- for image creation we need to write Dockerfile
- this file helps to create an image