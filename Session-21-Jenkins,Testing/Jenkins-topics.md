# Setting up a cron Job in Jenkins

**Free Style Project**
-  Go to Jenkins - new Item - create free style project
- add description, check Build Periodically
- schedule: H/10 * * * * (run after every 10 minutes)
- Build Step -> execute shell
- add some inclued command and save
- it will run after 10 minutes

**Pipeline**
- Create pipeline 
- add below script

```groovy
pipeline {
    agent any

    triggers {
        cron('H/10 * * * *')
    }
    stages {
        stage('Hello') {
            steps {
                echo 'Hello World'
            }
        }
    }
}

```
- save it and check once.