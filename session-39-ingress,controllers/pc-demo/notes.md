# Execute How Pv and PVC works

- create pv.yml

```bash
kubectl apply -f pv.yml
kubectl get pv
kubectl describe pv demo-pv
```
- create pvc.yml

```bash
kubectl apply -f pvc.yml
kubectl get pvc
kubectl describe pvc demo-pvc
```

- create pod.yml

```bash
kubectl apply -f pod.yml
kubectl get pods
kubectl describe pod pvc-demo-pod
# see mounted volume
# let's Get into this pod and create some data
kubectl exec -it pvc-demo-pod -- bash
# inside bash
echo "Hello from PV" > /usr/share/nginx/html/index.html
exit

# delete pod
kubectl delete pod pvc-demo-pod
# create aggain and try to access data
kubectl apply -f pod.yml
kubectl exec -it pvc-demo-pod -- bash
cat /usr/share/nginx/html/index.html
exit 
#  exit form pod
```

## Clear all resources

```bash
kubectl delete pod pvc-demo-pod
kubectl delete pvc demo-pvc
kubectl delete pv demo-pv
```