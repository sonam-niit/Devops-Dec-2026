# What Problem Does Ingress Solve?

- Let's Say we have 2 applications
    - frontend: React App
    - Backend: Node Js API

- when we trying to access this application:
    - http://IP:300001 -> Backend
    - http://IP:300002 -> Frontend

- Users need to remember port numbers without ingress

**With Ingress**

- http://myapp.local -> frontend
- http://myapp.local/api -> backend

- Single domain clear routing

![Ingress](images/ingress.png)

**Let's Implement using Minikube**

```bash
# Minikube start
minikube start
kubectl cluster-info
kubectl get nodes 
# enable ingress controller
minikube addons enable ingress

# Verify
kubectl get pods -n ingress-nginx
# see some controller name with ingress-nginx-controller (Running)
```

![Step1](images/step1.png)

## Let's Create Deployment, service and Ingress

- nginx-deployment.yml
- nginx-service.yml
- ingress.yml

```bash
kubectl apply -f nginx-deployment.yml
kubectl get pods
kubectl apply -f nginx-service.yml
kubectl get svc
kubectl apply -f ingress.yml
kubectl get ingress # you can see host name myapp.local
kubectl describe ingress webapp-ingress
```

## Add Host History

- if you are using linux edit /etc/hosts file you need to 
- add host details

- minikube ip (this ip needs to be added as host)
- sudo nano /etc/hosts
- ip    myapp.local (save and exit)

- If you are using linux (wsl) with windows then
- open cmd as administrator
- notepad C:\Windows\System32\drivers\etc\hosts
- edit 192.168.49.2      myapp.local

- check in wsl: curl http://myapp.local (work)
- you can see default page of NGINX code

- try to access http://myapp.local/ in browser (it will not work)
- as minikube is running locally


## Clear Resources
```bash
kubectl delete deployment webapp
kubectl delete service webapp-service
kubectl delete ingress webapp-ingress
```