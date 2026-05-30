# What is Pod?

- Pod is smallest unit in Kubernetes
- Pod: one container or somethimes few tightly coupled multiple containers running under one pod - who can share storage, volume, network, Ip etc.
- If pod die, kuberners does not automatically bring it back.

- who will take care of running pods? (self healing)

1. ReplicaSet
2. Deployments

1. Replica Set

- ensures the specified no of identical pods which are always running
- if 1 pod got crash/deleted or not healthy then it will recreate new one.

**How to create**

- create a file named replicaset.yml

```bash
kubectl apply -f replicaset.yml
kubectl get rs
kubectl get pods
#  you can see 3 pods running
# lets delete one copy any pod name from the output
kubectl delete pod pod-name
# you can see its deleted
kubectl get pods 
# you can see new pod created and showing 3 pods running only
kubectl delete rs nginx-rs 
#  delete Resources
```
- update the file with service code as well
- added service code in same file
- again run command
- see pods, service and access service
