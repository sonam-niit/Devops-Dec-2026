# Working with Volume

- Docker container is not having any persistent volume
- once container stopped or removed data will be lost
- to manage data after deleting container we can use docker volume

```bash
sudo docker volume ls
sudo docker volume create storage
sudo docker run -d --name app1 -v storage:/usr/share/nginx/html -p 80:80 nginx
# volume bind with container
sudo docker exec -it app1 bash
# update code
echo "<h1> Hello From Docker volume</h1>" > /usr/share/nginx/html/index.html
# exit

# check localhost you can see updated content

sudo docker rm -f app1
# to check data persist or not you can create another container
sudo docker run -d --name app1 -v storage:/usr/share/nginx/html -p 80:80 nginx
sudo docker inspect app1 # see mounted volume
# again access in browser you can see the same output

# incase if you want to read persist data you can create temp container
sudo docker run --name test1 -v storage:/data -it busybox
ls /data
cat /data/index.html # you can see same content
exit 
# its temp container it exits when you exit from bash
```

## Bind Mounts

- Bind mounts direct;y map your host system folder into container
- whetever chnages on host -> instant chnages in container
- when you change something from container -> then also its appear on host
- perfect for development

```bash
cd ~
mkdir myapp
cd myapp
nano index.html # add below shown content save & exit

sudo docker run -d --name myapp -v ~/myapp:/usr/share/nginx/html -p 80:80 nginx
sudo docker ps 
sudo docker inspect myapp

# make some chnages to html and refresh browser
# you can see the changes without restarting container
```
- Html code for reference to add
```html
<!DOCTYPE html>
<html>
<head>
<title>Sonam Soni</title>
</head>
<body>

<h1>Sonam Soni</h1>
<p>DevOps Expert as well as instructor</p>
</body>
</html>
```
- update the code with below list
```html
<!DOCTYPE html>
<html>
<head>
<title>Sonam Soni</title>
</head>
<body>

<h1>Sonam Soni</h1>
<p>DevOps Expert as well as instructor</p>
<ul>
        <li>Ansible</li>
        <li>Docker</li>
</ul>
</body>
</html>
```