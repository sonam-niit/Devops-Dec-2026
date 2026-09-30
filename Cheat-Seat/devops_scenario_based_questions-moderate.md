# DevOps Scenario-Based Assessment Questions

## Experienced / Moderate Level

This question bank is designed for **moderate to experienced DevOps candidates**. The questions focus on troubleshooting, production scenarios, CI/CD, cloud infrastructure, containers, Kubernetes, Terraform, monitoring, and incident response.

---

## 1. Jenkins + Docker Permission Issue

Jenkins successfully checks out the code and starts the build. However, during the Docker image build stage, the pipeline fails with:

```text
permission denied while trying to connect to the Docker daemon socket
```

### Questions
- What could be the root cause?
- What changes would you make for the Jenkins user?
- How would you verify that the issue has been resolved?
- What security considerations should you keep in mind when giving Jenkins access to Docker?

---

## 2. Kubernetes CrashLoopBackOff

An application has been deployed to Kubernetes. The deployment succeeds, but the pod continuously enters:

```text
CrashLoopBackOff
```

### Questions
- Which commands would you run first?
- What would you check in the pod logs?
- How would you determine whether the problem is related to the application or Kubernetes configuration?
- What could cause an application that works locally to fail inside Kubernetes?

---

## 3. Kubernetes Service Has No Endpoints

A backend application pod is running successfully.

```text
Pod: Running
Service: Running
Endpoints: Empty
```

However, other pods cannot access the backend.

### Questions
- What could be wrong?
- How would you troubleshoot the Service?
- What is the relationship between Service selectors and Pod labels?
- What command would you use to verify the endpoints?

Consider:

```yaml
# Service
selector:
  app: backend
```

and:

```yaml
# Pod
labels:
  app: backend-api
```

---

## 4. CI/CD Pipeline Deployment Failure

A developer pushes code to GitHub. Jenkins automatically starts the pipeline.

The pipeline contains:

```text
Checkout
Build
Test
Docker Build
Push Image
Deploy
```

The build and tests pass, and the Docker image is pushed successfully, but production deployment fails.

### Questions
- Where would you start debugging?
- How would you determine whether the problem is with the Docker image or Kubernetes?
- Which logs and commands would you check?
- How would you roll back to the previous version?

---

## 5. Docker Container Running but Application Inaccessible

A Docker container runs successfully on a developer machine:

```bash
docker run -p 8080:8080 myapp
```

The same container is deployed on an EC2 instance. The container is running, but the application cannot be accessed from the internet.

### Questions
- What would you check?
- How would Docker port mapping affect this?
- What would you check in the EC2 Security Group?
- What is the difference between an application listening on `localhost` and `0.0.0.0`?
- What other components could block the request?

---

# AWS Scenario-Based Questions

## 6. EC2 Application Cannot Be Accessed Externally

A Spring Boot application is running on an EC2 instance on port `8080`.

Running this command on the EC2 instance works:

```bash
curl localhost:8080
```

But accessing:

```text
http://<EC2_PUBLIC_IP>:8080
```

from your browser does not work.

### Questions
- If the application works locally on the EC2 server, what would you investigate?
- What Security Group configuration would you check?
- What OS-level firewall configuration might matter?
- How would you verify that the application is listening on the expected interface and port?

---

## 7. S3 AccessDenied in Jenkins

A Jenkins pipeline needs to upload a deployment artifact to an S3 bucket.

The pipeline fails with:

```text
AccessDenied: Access Denied
```

The AWS credentials are valid.

### Questions
- What AWS permissions would you check?
- What is the difference between an IAM identity policy and an S3 bucket policy?
- Could an explicit Deny cause this problem?
- What role could KMS permissions play if the bucket uses encryption?
- How would you troubleshoot the issue without making the bucket public?

---

## 8. Terraform State Drift

A team manages infrastructure using Terraform. Someone manually modifies an AWS resource through the AWS Console.

Now:

```bash
terraform plan
```

shows unexpected changes.

### Questions
- What is Terraform state?
- What is infrastructure drift?
- How does Terraform detect the difference?
- How would you safely handle the situation?
- When would `terraform import` be appropriate?
- What precautions should be taken before applying the plan?

---

# Monitoring and Production Scenarios

## 9. EC2 CPU Suddenly Reaches 100%

A production EC2 instance suddenly reaches 100% CPU utilization.

### Questions
- What would you check first?
- Which CloudWatch metrics would you inspect?
- How would you identify the process consuming CPU?
- How would you determine whether the spike is caused by increased traffic, a recent deployment, or an application issue?
- What immediate mitigation could be considered?
- What would you include in the Root Cause Analysis?

---

## 10. Application Is Slow but CPU Is Normal

A production API becomes very slow.

Metrics show:

```text
CPU:       35%
Memory:    50%
Disk:      Normal
Network:   Normal
```

However, API response time increased:

```text
200 ms → 5 seconds
```

### Questions
- Why can an application be slow even when CPU and memory are normal?
- What would you investigate?
- How could database latency cause this?
- What is connection-pool exhaustion?
- Could an external API dependency cause the problem?
- What application-level metrics would you check?

Consider:

```text
Database latency
Connection pool
Thread pool
Garbage Collection
External APIs
Network latency
Locks/contention
Kafka consumer lag
```

---

# Kafka Scenario-Based Questions

## 11. Kafka Producer Works but Consumer Receives Nothing

The producer successfully publishes messages to Kafka.

```text
Producer → Kafka → Consumer
             ✓        ✗
```

The consumer application is running but does not receive messages.

### Questions
- What would you check first?
- How would you verify that the topic exists?
- How would you check the consumer group?
- What is consumer lag?
- How do offsets affect message consumption?
- What could cause partition-assignment problems?
- Could serialization/deserialization cause this issue?
- What Kafka commands would you use?

---

# Jenkins and SonarQube Scenarios

## 12. SonarQube Analysis Passes but Quality Gate Fails

A Jenkins pipeline contains:

```text
Checkout
Build
Unit Test
SonarQube Analysis
Quality Gate
Deploy
```

SonarQube analysis completes successfully, but the pipeline stops before deployment.

SonarQube reports:

```text
Analysis: Successful
Quality Gate: Failed
Coverage: 78%
```

### Questions
- What is the difference between SonarQube analysis and a Quality Gate?
- Why can analysis succeed while the Quality Gate fails?
- How does Jenkins receive the Quality Gate result?
- What SonarQube conditions would you investigate?
- What should happen to the deployment when the Quality Gate fails?

---

# Kubernetes Advanced Scenarios

## 13. Zero-Downtime Deployment

You need to deploy a new version of a production application.

Current:

```text
v1 → Production
```

New version:

```text
v2 → Ready
```

Requirements:

- No downtime
- Ability to quickly roll back
- Safe production release

### Questions
- Which Kubernetes deployment strategies could you consider?
- Explain Rolling Deployment.
- Explain Blue-Green Deployment.
- Explain Canary Deployment.
- How would you choose between these strategies?
- How would you perform a rollback?

---

## 14. Kubernetes Pods Stuck in Pending

A Kubernetes Deployment is configured with:

```yaml
replicas: 5
```

After deployment:

```text
2 Pods → Running
3 Pods → Pending
```

### Questions
- What would you investigate?
- Which commands would you run?
- How can CPU and memory resource requests affect scheduling?
- What are Kubernetes taints and tolerations?
- How can node selectors or affinity prevent scheduling?
- Could a PersistentVolumeClaim cause the pod to remain pending?

Useful commands:

```bash
kubectl get pods
kubectl describe pod <pod-name>
kubectl get nodes
kubectl describe node <node-name>
```

---

# Production Incident Scenario

## 15. Production Deployment Causes Errors

You deploy version `v2.5` to production.

Five minutes later:

```text
Error Rate:       0.5% → 15%
Latency:          200ms → 3 seconds
CPU:              40% → 80%
```

The product team asks you to fix production immediately.

### Questions
1. What would you do first?
2. Would you investigate or roll back?
3. Which metrics would you check?
4. Which logs would you inspect?
5. How would you determine whether the deployment caused the issue?
6. How would you perform a rollback?
7. How would you verify that the rollback fixed the issue?
8. How would you identify the root cause later?
9. What preventive measures would you introduce?

---

# Additional Moderate-Level DevOps Scenarios

## 16. Git Merge Conflict in CI/CD

A Jenkins pipeline suddenly starts failing after multiple developers merge changes into the main branch.

### Questions
- How would you determine whether the failure is caused by a merge conflict or application code?
- How would you reproduce the failure locally?
- What Git commands would you use?
- How would you prevent unstable code from reaching the main branch?

---

## 17. Docker Image Size Is Extremely Large

A Docker image for a Node.js application is 1.8 GB.

### Questions
- Why might the image be so large?
- How would you identify what is consuming space?
- How would you optimize the Dockerfile?
- What is a multi-stage Docker build?
- Why should unnecessary development dependencies be excluded from a production image?

---

## 18. Docker Container Exits Immediately

You run:

```bash
docker run myapp
```

The container starts and immediately exits.

### Questions
- What would you check?
- What is the relationship between the container's main process and container lifecycle?
- Which Docker commands would you use?
- How would you inspect the container logs?
- What could cause the application's main process to terminate?

---

## 19. Kubernetes ConfigMap Change

An application uses configuration from a ConfigMap.

You update the ConfigMap, but the running application continues using the old value.

### Questions
- Why might the application still have the old configuration?
- Does updating a ConfigMap automatically restart a Deployment?
- How would you make the application pick up the new configuration?
- How would you implement configuration changes safely in production?

---

## 20. Kubernetes Secret Management

An application needs database credentials.

A developer proposes putting the credentials directly inside:

```yaml
env:
  - name: DB_PASSWORD
    value: "MyPassword123"
```

### Questions
- What is wrong with this approach?
- How would you manage the secret in Kubernetes?
- What are the limitations of Kubernetes Secrets?
- How could AWS Secrets Manager or another external secret-management solution be used?
- How would you prevent credentials from appearing in Git history?

---

## 21. Jenkins Credentials

A Jenkins pipeline requires AWS credentials.

A developer adds:

```groovy
environment {
    AWS_SECRET_ACCESS_KEY = "xxxxx"
}
```

### Questions
- What security risks exist?
- How should Jenkins credentials be stored?
- How would you inject credentials into a pipeline?
- How would you prevent secrets from appearing in Jenkins logs?

---

## 22. Terraform Resource Already Exists

Terraform configuration attempts to create an AWS resource, but Terraform reports that the resource already exists.

### Questions
- Why can this happen?
- What is Terraform's state relationship with the real infrastructure?
- When should `terraform import` be used?
- What should you verify before importing the resource?

---

## 23. Terraform Plan Shows Resource Replacement

You make a small Terraform configuration change.

`terraform plan` unexpectedly shows:

```text
-/+ resource will be replaced
```

### Questions
- What does resource replacement mean?
- Why can Terraform decide to replace a resource?
- How would you determine what attribute is forcing replacement?
- What production risks should you consider before applying it?
- How could you prevent accidental destructive changes?

---

## 24. Terraform Apply Fails Halfway

A Terraform deployment creates several resources successfully, but fails while creating another resource.

### Questions
- What happens to the resources already created?
- What would you check before running `terraform apply` again?
- How does Terraform state help recover?
- How would you safely continue the deployment?
- When might manual cleanup be necessary?

---

## 25. Jenkins Pipeline Is Very Slow

A pipeline that normally completes in 8 minutes now takes 35 minutes.

### Questions
- How would you identify which stage became slow?
- What metrics or Jenkins information would you inspect?
- Could Docker image builds be responsible?
- Could dependency downloads be responsible?
- How could caching improve pipeline performance?
- How would you distinguish infrastructure slowness from application/build slowness?

---

## 26. Build Works Locally but Fails in Jenkins

A developer says:

> "The application builds successfully on my laptop."

The same commit fails in Jenkins.

### Questions
- What differences would you investigate?
- How would Java/Node/Maven/npm version differences affect the build?
- How would environment variables affect the result?
- How would you compare the Jenkins environment with the developer environment?
- How would you make builds reproducible?

---

## 27. Health Check Failure

A Kubernetes application is running, but Kubernetes repeatedly restarts it.

The application itself appears healthy when accessed manually.

### Questions
- What are liveness and readiness probes?
- What is the difference between them?
- What happens when a liveness probe fails?
- What happens when a readiness probe fails?
- What could cause a probe to fail even though the application is technically running?

---

## 28. Kubernetes Deployment Has Old and New Pods

During a rolling update, you see:

```text
v1 Pods → 3
v2 Pods → 2
```

Both versions are temporarily running.

### Questions
- Why can both versions exist simultaneously?
- How does a rolling update work?
- How does Kubernetes decide when to terminate old pods?
- What are `maxSurge` and `maxUnavailable`?
- How would you configure a safer rollout?

---

## 29. Database Connection Failure After Deployment

A new application version is deployed successfully, but the application logs show:

```text
Connection refused: database:3306
```

### Questions
- What would you check first?
- Is the database reachable from the application container?
- How would you test DNS resolution?
- How would you test network connectivity?
- Could Kubernetes Service configuration be involved?
- Could credentials or environment variables be wrong?

---

## 30. Linux Disk Space Alert

A production server sends an alert:

```text
Disk Usage: 95%
```

### Questions
- What commands would you run?
- How would you identify which directories consume the most space?
- How would you identify large log files?
- How would you safely clean disk space?
- What risks exist when deleting files from a production server?
- How would you prevent the problem from recurring?

Useful commands:

```bash
df -h
du -sh *
du -ah /var | sort -rh | head
```

---

# Expected Assessment Style

For an experienced DevOps assessment, candidates should not only provide commands. A strong answer should demonstrate:

1. **Problem understanding**
2. **Logical troubleshooting sequence**
3. **Knowledge of relevant tools**
4. **Ability to identify root cause**
5. **Safe production practices**
6. **Rollback/recovery thinking**
7. **Security awareness**
8. **Monitoring and observability**
9. **Automation mindset**
10. **Prevention and continuous improvement**

## Recommended Difficulty

| Level | Typical Question |
|---|---|
| Entry | What is Docker? |
| Basic | How do you create a Docker image? |
| Moderate | Container is running but application is inaccessible. Troubleshoot. |
| Moderate | Jenkins pipeline fails at Docker stage. Identify the issue. |
| Experienced | Kubernetes pod is in CrashLoopBackOff. Perform systematic troubleshooting. |
| Experienced | Production deployment increases error rate. Decide the incident-response steps. |
| Advanced | Design a zero-downtime deployment with rollback. |
| Advanced | Investigate high API latency when infrastructure metrics appear normal. |

## Key Areas Covered

- Linux
- Git
- Jenkins
- CI/CD
- Docker
- Kubernetes
- AWS EC2
- AWS S3
- IAM
- Terraform
- Kafka
- SonarQube
- Monitoring
- Production troubleshooting
- Incident response
- Security
- Deployment strategies
- Infrastructure as Code
