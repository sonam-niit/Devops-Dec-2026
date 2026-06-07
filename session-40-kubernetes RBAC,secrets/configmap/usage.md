# Working with COnfig Map

- create config.yml file
- create pod.yml (pod using config file as configuration)

```bash
kubectl apply -f config.yml
kubectl apply -f pod.yml

kubectl get pods
kubectl exec -it configmap-demo-pod -- bash
echo $APP_COLOR
echo $APP_MODE
# you can see values
exit # to exit from Pod

kubectl delete pod configmap-demo-pod

```