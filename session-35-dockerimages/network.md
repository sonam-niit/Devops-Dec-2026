# Working with Networks

- using network containers can communicate with each other
- container can communicate with host machine
- container can communicate with internet

- Bridge network is by default network

```bash
sudo docker network ls
# let's create one custom bridge network
sudo docker network create sonamnet
sudo docker network ls

# Run 2 containers under the same network
sudo docker run -d --name app1 --network sonamnet nginx # run in detached mode
sudo docker run -it --name app2 --network sonamnet busybox # run interactively

#  once you are inside the bash run ping command
ping app1
# you can see response coming from 1st container

sudo docker stop app1
sudo docker rm app1
sudo docker rm app2

# now try the same without using network
sudo docker run -d --name app1 nginx
sudo docker run -it --name app2 busybox
ping app1 # now you can see bad address no response 

```