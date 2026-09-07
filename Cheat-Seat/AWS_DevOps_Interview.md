# AWS DevOps Interview Cheat Sheet

A practical AWS interview revision guide with **quick interview answers**, **real-time use cases**, and **how the services fit together**.

---

## 1. Amazon EC2

### What to say in interview
> **“EC2 provides resizable virtual servers in AWS. We can choose the required compute capacity, install our application and configure networking, security and scaling around it.”**

### Real-time use case
A company hosts its Spring Boot backend on EC2 instances. An Application Load Balancer distributes traffic across multiple EC2 instances.

### Key concepts
- AMI
- Instance types
- Security Groups
- EBS
- Elastic IP
- Auto Scaling
- User Data

---

## 2. Amazon S3

### What to say in interview
> **“S3 is highly durable object storage used for files, backups, logs, static website assets and application artifacts.”**

### Real-time use case
A React/Vite frontend is built into static files and stored in S3. CloudFront distributes those files globally.

### Key concepts
- Bucket
- Object
- Versioning
- Lifecycle rules
- Encryption
- Bucket policies
- Storage classes

---

## 3. Amazon VPC

### What to say in interview
> **“VPC provides an isolated network environment in AWS where we define subnets, routing, gateways and network security.”**

### Real-time use case
A production application is deployed in a VPC with public subnets for the load balancer and private subnets for application servers and databases.

### Key concepts
- Public/private subnet
- Route table
- Internet Gateway
- NAT Gateway
- Security Group
- Network ACL

---

## 4. IAM

### What to say in interview
> **“IAM controls who can access AWS resources and what actions they are allowed to perform. I follow the principle of least privilege.”**

### Real-time use case
A CI/CD pipeline gets an IAM role that allows it to push Docker images to ECR and deploy the application, without giving it full administrator access.

### Key concepts
- User
- Group
- Role
- Policy
- Least privilege
- AssumeRole
- Temporary credentials

---

## 5. Application Load Balancer (ALB)

### What to say in interview
> **“ALB distributes HTTP and HTTPS traffic across multiple targets and can perform path-based or host-based routing.”**

### Real-time use case
`/api/*` requests go to the backend target group while `/admin/*` goes to a different service.

### Key concepts
- Listener
- Target group
- Health check
- Path-based routing
- Host-based routing
- HTTPS/ACM

---

## 6. Auto Scaling

### What to say in interview
> **“Auto Scaling automatically adjusts the number of EC2 instances based on demand, helping maintain availability and control cost.”**

### Real-time use case
During a traffic spike, an application scales from 2 EC2 instances to 6. When traffic decreases, instances scale back down.

### Key concepts
- Launch template
- Minimum capacity
- Maximum capacity
- Desired capacity
- Scaling policies
- Health checks

---

## 7. Amazon RDS

### What to say in interview
> **“RDS is a managed relational database service that handles many operational tasks such as backups, patching and high availability options.”**

### Real-time use case
A Spring Boot application uses MySQL on RDS instead of maintaining MySQL manually on an EC2 server.

### Key concepts
- MySQL/PostgreSQL
- Automated backups
- Multi-AZ
- Read replicas
- Security groups
- Encryption

---

## 8. DynamoDB

### What to say in interview
> **“DynamoDB is a managed NoSQL database designed for high-scale, low-latency applications.”**

### Real-time use case
A high-traffic application stores session, user preference or event data where predictable low-latency access is important.

### Key concepts
- Partition key
- Sort key
- On-demand/provisioned capacity
- Global secondary index
- Streams

---

## 9. CloudFront

### What to say in interview
> **“CloudFront is AWS's CDN that caches and delivers content from edge locations closer to users.”**

### Real-time use case
A React application hosted in S3 is delivered through CloudFront so users in different regions receive content with lower latency.

### Key concepts
- Distribution
- Origin
- Cache behavior
- TTL
- HTTPS
- Origin Access Control

---

## 10. Route 53

### What to say in interview
> **“Route 53 is AWS's highly available DNS service used for domain resolution and traffic routing.”**

### Real-time use case
`api.example.com` resolves to an Application Load Balancer.

### Key concepts
- Hosted zone
- A record
- CNAME
- Alias
- Health checks
- Routing policies

---

## 11. ECR

### What to say in interview
> **“ECR is a managed container image registry where we securely store and retrieve Docker images.”**

### Real-time use case
A CI pipeline builds a Docker image, tags it with the Git commit SHA and pushes it to ECR before deployment to ECS.

### Key concepts
- Repository
- Image tag
- Image digest
- Lifecycle policy
- Image scanning

---

## 12. ECS

### What to say in interview
> **“ECS is AWS's managed container orchestration service for running Docker containers.”**

### Real-time use case
A company runs a containerized Node.js or Spring Boot application on ECS Fargate without managing EC2 servers.

### Key concepts
- Cluster
- Task definition
- Service
- Task
- Fargate
- Load balancer

---

## 13. EKS

### What to say in interview
> **“EKS is AWS's managed Kubernetes service. AWS manages the Kubernetes control plane while we manage workloads and related infrastructure.”**

### Real-time use case
An organization with Kubernetes-based microservices runs production workloads on EKS.

### Key concepts
- Cluster
- Node group
- Pod
- Deployment
- Service
- Ingress

---

## 14. Lambda

### What to say in interview
> **“Lambda is a serverless compute service where code runs in response to events without us managing servers.”**

### Real-time use case
An S3 upload triggers a Lambda function that validates or processes the uploaded file.

### Key concepts
- Event trigger
- Function
- Runtime
- Execution role
- Timeout
- Memory
- Concurrency

---

## 15. CloudWatch

### What to say in interview
> **“CloudWatch provides monitoring, metrics, logs, dashboards and alarms for AWS resources and applications.”**

### Real-time use case
If EC2 CPU utilization stays above a threshold, CloudWatch triggers an alarm that can be connected to an Auto Scaling action.

### Key concepts
- Metrics
- Logs
- Alarms
- Dashboards
- Log groups
- Log streams

---

## 16. CloudTrail

### What to say in interview
> **“CloudTrail records AWS API activity, which helps with auditing, security investigation and tracking who performed an action.”**

### Real-time use case
If someone accidentally deletes a production resource, CloudTrail can help identify which identity performed the API action.

### Key concepts
- API activity
- Event history
- Trail
- Audit
- User/role identity

---

## 17. Secrets Manager

### What to say in interview
> **“Secrets Manager securely stores and manages sensitive information such as database passwords, API keys and credentials.”**

### Real-time use case
A Spring Boot application retrieves its database credentials from Secrets Manager instead of keeping passwords in Git or a Terraform file.

### Key concepts
- Secret
- Encryption
- IAM access
- Rotation
- Versioning

---

## 18. KMS

### What to say in interview
> **“KMS is used to create and control encryption keys that protect data across AWS services.”**

### Real-time use case
An S3 bucket containing sensitive application files uses server-side encryption with a customer-managed KMS key.

### Key concepts
- KMS key
- Key policy
- Encryption/decryption
- Key rotation
- Customer-managed key

---

## 19. SQS

### What to say in interview
> **“SQS is a managed message queue that decouples application components so producers and consumers don't have to communicate synchronously.”**

### Real-time use case
An order service places an order-processing message in SQS. A worker processes it asynchronously.

### Key concepts
- Queue
- Producer
- Consumer
- Visibility timeout
- Dead-letter queue

---

## 20. SNS

### What to say in interview
> **“SNS is a pub/sub messaging service used to distribute notifications or events to multiple subscribers.”**

### Real-time use case
A CloudWatch alarm publishes an alert to an SNS topic, which can notify subscribed endpoints.

### Key concepts
- Topic
- Publisher
- Subscriber
- Fan-out
- Notifications

---

# CI/CD Services

## 21. CodePipeline

### What to say in interview
> **“CodePipeline orchestrates stages of a CI/CD workflow such as source, build, test and deployment.”**

### Real-time use case
A Git commit triggers a pipeline that builds the application, runs tests and deploys it to the target environment.

---

## 22. CodeBuild

### What to say in interview
> **“CodeBuild is a managed build service used to compile code, run tests and produce build artifacts.”**

### Real-time use case
A Java project is compiled with Maven, unit tests are executed and the generated JAR is prepared for deployment.

---

## 23. CodeDeploy

### What to say in interview
> **“CodeDeploy automates application deployments to supported compute environments such as EC2 and Lambda.”**

### Real-time use case
A new application version is deployed automatically to EC2 instances as part of a release pipeline.

---

# Terraform + AWS Interview Essentials

## Resource vs Data Source

### Resource
> **“A resource is used to create and manage infrastructure.”**

```hcl
resource "aws_vpc" "main" {
  cidr_block = "10.0.0.0/16"
}
```

### Data source
> **“A data source reads information about an existing resource without creating it.”**

```hcl
data "aws_vpc" "existing" {
  tags = {
    Name = "production-vpc"
  }
}
```

---

## `depends_on`

### What to say
> **“`depends_on` explicitly tells Terraform that one resource depends on another when Terraform cannot determine the dependency automatically.”**

```hcl
depends_on = [
  aws_iam_role_policy.app
]
```

---

## `lifecycle.prevent_destroy`

### What to say
> **“For critical production resources, `prevent_destroy` protects against accidental destruction through Terraform.”**

```hcl
lifecycle {
  prevent_destroy = true
}
```

### Important
`prevent_destroy` protects Terraform-managed destruction. It does **not** stop someone from deleting the resource directly through the AWS Console/API.

---

## Terraform says `No changes`, but AWS shows a change

### What to say
> **“I would investigate possible drift, state refresh, `ignore_changes`, whether the attribute is actually managed by Terraform, and provider behavior.”**

Useful command:

```bash
terraform plan -refresh-only
```

---

# Production Protection — Interview Answer

### Question
**How do you protect production from accidental deletion?**

### Strong answer
> **“For critical production resources, I use Terraform lifecycle protection such as `prevent_destroy`, combined with least-privilege IAM permissions, approval-based changes, backups and monitoring. Production changes should go through code review and CI/CD rather than direct manual changes.”**

---

# Common Architecture to Explain in an Interview

```text
                         USERS
                           |
                           v
                       Route 53
                           |
                           v
                       CloudFront
                           |
                           v
                          ALB
                           |
              +------------+------------+
              |                         |
              v                         v
            EC2                      ECS/EKS
              |
              v
             RDS

CI/CD
-----
GitHub
   |
   v
Jenkins / GitHub Actions
   |
   +--> Build + Test
   |
   +--> Docker Build
   |
   v
ECR
   |
   v
ECS / EC2 / EKS

Infrastructure
--------------
Terraform
   |
   +--> VPC
   +--> IAM
   +--> EC2
   +--> ALB
   +--> RDS
   +--> S3

Monitoring & Audit
------------------
CloudWatch + CloudTrail
```

---

# 30-Second AWS DevOps Summary

If the interviewer asks:

**“Which AWS services have you worked with?”**

You can say:

> **“I have worked with core AWS services such as EC2, VPC, IAM, S3, ALB, RDS, CloudWatch and CloudTrail. On the container and CI/CD side, I have worked with Docker, ECR and ECS/EKS concepts. I have also used Terraform for Infrastructure as Code and understand how these services fit together in a real deployment architecture.”**

---

# Quick Revision

| Service | Remember |
|---|---|
| EC2 | Compute |
| S3 | Object storage |
| VPC | Network |
| IAM | Access control |
| ALB | Traffic distribution |
| Auto Scaling | Scale EC2 |
| RDS | Relational DB |
| DynamoDB | NoSQL |
| CloudFront | CDN |
| Route 53 | DNS |
| ECR | Docker images |
| ECS | Containers |
| EKS | Kubernetes |
| Lambda | Serverless |
| CloudWatch | Monitoring |
| CloudTrail | Audit/API history |
| Secrets Manager | Secrets |
| KMS | Encryption keys |
| SQS | Queue |
| SNS | Pub/Sub |
| CodePipeline | CI/CD orchestration |
| CodeBuild | Build/Test |
| CodeDeploy | Deployment |
| Terraform | Infrastructure as Code |

---

## Interview Formula

For almost every AWS service, answer in this order:

**1. What is it?**  
**2. Why do we use it?**  
**3. Real-time example**

Example:

> **“ALB is a Layer 7 load balancer. We use it to distribute HTTP/HTTPS traffic across multiple application targets. In a production application, I can put an ALB in front of multiple EC2 instances and configure health checks so traffic is sent only to healthy instances.”**

This structure makes your answer sound **practical rather than memorized**.
