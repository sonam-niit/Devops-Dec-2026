# Kubernetes Interview Questions

### Kubernetes Basics
1. What is Kubernetes?
2. Why was Kubernetes created?
3. What problems does Kubernetes solve?
4. What is container orchestration?
5. What are the main features of Kubernetes?
6. What is a Kubernetes cluster?
7. What is the difference between Docker and Kubernetes?
8. Can Kubernetes run without Docker?
9. What are the different Kubernetes distributions?
10. What is the latest stable Kubernetes version you have worked with?

### Kubernetes Architecture
1. Explain the Kubernetes architecture.
2. What are the components of the Control Plane?
3. What are the components of a Worker Node?
4. What is the role of the API Server?
5. What is ETCD?
6. What is the Scheduler?
7. What is the Controller Manager?
8. What is Cloud Controller Manager?
9. What is Kubelet?
10. What is Kube Proxy?
11. What is a Container Runtime?
12. How does Kubernetes communicate between components?

### Pods
1. What is a Pod?
2. Why is Pod the smallest deployable unit?
3. Can a Pod contain multiple containers?
4. What are sidecar containers?
5. How does Pod networking work?
6. What is Pod lifecycle?
7. What are Pod phases?
8. Why shouldn't Pods be created directly in production?
9. How do you restart a Pod?
10. What happens when a Pod crashes?

### ReplicaSet & Deployment
1. What is a ReplicaSet?
2. What is a Deployment?
3. Difference between Deployment and ReplicaSet?
4. What is the desired state in Kubernetes?
5. What is Rolling Update?
6. What is Recreate Deployment?
7. How do Rollbacks work?
8. How do you pause and resume a Deployment?
9. How do you scale a Deployment?
10. What is maxUnavailable?
11. What is maxSurge?

### StatefulSet
1. What is StatefulSet?
2. When should StatefulSet be used?
3. Difference between Deployment and StatefulSet?
4. Why does StatefulSet provide stable identities?
5. What is Headless Service?

### DaemonSet
1. What is DaemonSet?
2. When do we use DaemonSets?
3. Give real-world examples of DaemonSets.
4. Difference between DaemonSet and Deployment?

### Jobs & CronJobs
1. What is a Job?
2. What is a CronJob?
3. Difference between Job and Deployment?
4. What happens if a Job fails?

### Services
1. What is a Kubernetes Service?
2. Why do we need Services?
3. What is ClusterIP?
4. What is NodePort?
5. What is LoadBalancer?
6. What is ExternalName Service?
7. Difference between NodePort and LoadBalancer?
8. How does Service discovery work?
9. What is CoreDNS?

### Ingress
1. What is Ingress?
2. Why use Ingress instead of LoadBalancer?
3. What is an Ingress Controller?
4. Name some Ingress Controllers.
5. What is SSL termination?

### ConfigMap & Secret
1. What is ConfigMap?
2. What is Secret?
3. Difference between ConfigMap and Secret?
4. How do you mount ConfigMaps?
5. How do you mount Secrets?
6. Are Kubernetes Secrets encrypted?
7. How do you secure Secrets?

### Autoscaling
1. What is Horizontal Pod Autoscaler (HPA)?
2. What is Vertical Pod Autoscaler (VPA)?
3. What is Cluster Autoscaler?
4. Difference between HPA, VPA, and Cluster Autoscaler?

### Monitoring & Logging
1. How do you monitor Kubernetes?
2. What is Prometheus?
3. What is Grafana?
4. What is Metrics Server?
5. How do you collect logs?
6. What is ELK Stack?

### Helm
1. What is Helm? Why use Helm?
2. What is a Helm Chart?
3. What is values.yaml?
4. Difference between Helm install and upgrade?
5. How do you rollback a Helm release?