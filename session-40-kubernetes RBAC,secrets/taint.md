# Taint and Tokeration

- A Taint is applied to a node and it repels pods that do not have a maching tolerance.
- Effect for taints:
    - NoSchedule: Pod will not schedule on that machine
    - PreferNoSchedule: kubernetes try to avoid that machine
    - NoExecute: pod is Evicted if running + new pod won't schedule

```bash
# create taint
kubectl taint nodes minikube name=sonam:NoExecute
# you can see running pods terminated and you can't create new pod
kubect get pods
kubectl apply -f secrets/pod.yml 
# it will show pod created but check status must be showing pending
kubect get pods
#  now remove taint using same command with -
kubectl taint nodes minikube name=sonam:NoExecute-
# once its removed check the status of previously created pod
#  you can see its running
```

### Tolerance
- this needs to be added on pod
- means your perticular pod is allowed to run on node.

```bash
# create one taint
kubectl taint nodes minikube app=backend:NoSchedule
# only the pod with tolerance for app=backend can run on this node
# except other with not schedule it will show status pending
```

- create file tolerance-pod.yml
```yml
apiVersion: v1
kind: Pod
metadata:
  name: tolerated-pod
spec:
  containers:
  - name: nginx
    image: nginx
  tolerations:
    - key: "app"
      operator: "Equal"
      value: "backend"
      effect: "NoSchedule"
```

```bash
kubectl apply -f tolerance-pod.yml
kubectl get pods # see status running
kubectl apply -f secrets/pod.yml
#  this must be pending because no toleration added
kubectl taint nodes minikube app=backend:NoSchedule
# now chec status must be running

kubectl delete pod <pod_name>
```