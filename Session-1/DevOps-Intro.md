# Introduction to DevOps
---
- DevOps is a way of working where dev (Development Team) & Ops (Operational Team) work together to build, test, release and run software in more faster way and making it more reliable.

## Devops LifeCycle

- Plan -> Code -> Build -> Test -> Release -> Deploy -> Operate -> Monitor -> Feedback -> Plan

**Plan**

- Requirement Gathering
- List customer Requirement
- Tools: Jira, Trello, Azure Boards

**Code**

- Developers will write Application Code
- They will also use version control
- Tools: Git, GitHub, GitLab, BitBucket

**Build**

- Convert Source Code to executable files
- managing dependency
- Tools: Gradle, Npm, Maven, Docker

**Test**

- Automated Testing
- Unit, Integration, E2E, Security etc...
- tools: Junit, Pytest, Selenium, SonarQube

**Release**

- Versioning Application
- Approval to Deploy
- Tools: Jenkins, GitHub Actions, ArtiFactory, Nexus

**Deploy**

- Application will be deployed o environments (Prod)
- Diffrent Deployment stratergies
- Tools: Kubernetes, Terraform, Ansible

**Operate**

- application run in prod environment
- manage infrastructure
- Tools: AWS, Azure, GCP, Kubernetes Cluster

**Monitor**

- track performance, logs, errors
- Alerts
- Tools: Prometheus, Grafana, ELK, CloudWatch

**Feedback**

- User Feedback & take monitoring data to improve app
- fix errors and optimize performance
- Jira, Slack, Monitoring Dashboards

**How CI/CD Works**

- code app
- push it on Github
- when push happen on github
- Copy the code (connect with cloud)
- Build app
- test app
- if all good deploy

*Everytime when you push code it execute all pipeline steps automatically to faster the process which is CI/CD Pipeline*



