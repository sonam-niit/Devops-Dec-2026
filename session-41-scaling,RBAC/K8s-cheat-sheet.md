# Kuberenets Fundamentals

- container orchestration Platform
- automate deployment, scaling and manage take care of containers

## Why?
- Self- healing
- Auto-scaling
- HA (High Avaialibility)
- Rolling Updates

## Kubernetes Cluster
- Master Node (Control Plane) - API Server, Schedules, Controller Manager, ETCD
- Worker Node (Kubelet, Kube Proxy, container Runtime)

## Concepts

1. Pods: smallest deployable Unit, inside that we can run 1 or more containers

```bash
kubectl run nginx --image=nginx
kubectl get pods
kubectl describe pod nginx
kubectl logs nginx
kubectl exec -it nginx -- bash
kubectl delete pod nginx
```

*Question: Why not run containers directly? why use Pod?*

2. Deployments:
    - manage replica sets and pods
    - enabling rolling updates (version update and rollback)

```bash
kubectl create deployment nginx --image=nginx
kubectl get deployment
kubectl scale deployment nginx --replicas=5 # increase from 1 to 5
kubectl rollout status deployment nginx
```

*Deployment vs Pod?*
*Rolling Updates vs Recreate?*

3. ReplicaSet

- maintain desired no of pods

*Deployment vs ReplicaSet?*

4. Service
- Types: ClusterIP, NodePort, Loadbalancer

```bash
kubectl expose deployment nginx --port=80
kubectl get svc
```
*ClusterIP vs NodePort vs Loadbalancer*

5. NameSpace

- to work with multiple services, depkloyment in seperate workspace

*Why nameSpace?*

6. ConfigMaps- Store non-sensitive Configuration
7. Secret- Store sensitive Configuration

*configmap vs secrets*

8. Volumes and PV and PVC

- Volume
- PV 
- PVC
- Storage Class

*Stateful vs stateless App?*

9. StatefulSets
- used databases, kafka, elsticsearch

*StatefulSets vs Deployment?*

10. DaemonSets
- use for collecting logs, monitoring agents

11. Scheduling
- Taints
- Tolerations
- Node Selector & Node Affinity
- Pod Selector & Pod Affinity

*Diffrentiate Affinity vs Taints*

12. Resource Management

- while creating pod give required resources
- Requests
- limits

13. Scaling
- HPA
- VPA
- Cluster AutoScaler (increase no of nodes as per requirement)

14. Ingress
- HTTP/HTTPS routing
- Path based Routing

14. Networking
- Pod Network
- DNS (access service by not its IP but its service name)

15. RBAC
- Role, RoleBinding, ClusterRole, ClusterRoleBinding

16. Security
- Security Context ( add in Pod yml)
- Pod security
- Network Policies
- Image Scanning (Clair , Trivy )

17. montironing and Logging
- Monitoring: Prometheus and Grafana (will practice this later)
- Logging (ELK Stack)

*How do you monitor your cluster?*

18. Kubernetes Package Manager: Helm

```bash
helm repo add
helm install
helm upgrade
helm rollback
```