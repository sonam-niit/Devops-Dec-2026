# Sonar jenkins integration

- check jenkins is running or not

```bash
sudo systemctl status jenkins
# if running login from browser
# localhost:8080
# check sonar status
# if running we can integrate them
```

- Go to jenkins -> manage jenkins -> plugings
- available plugins -> search for sonar scanner -> click on install

### Configure Sonar in Jenkins

- manage jenkins -> system -> sonarqube servers
- click on add sonar
- check for environment variable
- Name: MySonar
- ServerUrl: http://localhost:9000
- for Auth token -> click on Add + -> select jenkins -> in kind
- choose secret text -> in secret add generated token
- ID: SONAR_TOKEN and description: SONAR_TOKEN -> add

- select that auth token in sonar server 
- save

### Configure SonarScanner

- manage jenkins -> tools
- click on Add Sonar Scanner for MSbuild
- name: MySonarScanner
- install automatically
- click on add sonarqube scanner:
- name: MySonarScanner
- install automatically

## Create jenkins pipelie

```groovy
pipeline {
    agent any

    environment {
        SONARQUBE_ENV = 'MySonar'
    }

    stages {
        stage('Checkout'){
            steps{
                git url:'https://github.com/sonam-niit/python-calculator-sonar.git',branch:'main'
            }
        }
        stage('Create Virtualenv') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests & Coverage') {
            steps {
                sh '''
                    . venv/bin/activate
                    pytest --cov=app --cov-report=xml
                '''
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv("${SONARQUBE_ENV}") {
                    sh '''
                        . venv/bin/activate
                        /mnt/d/tools/sonar-scanner-linux/bin/sonar-scanner
                    '''
                }
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'coverage.xml', allowEmptyArchive: true
        }
    }
}
```

- click on Build Now


### Using Jenkins SonarScanner which is installed automatically

```groovy
pipeline {
    agent any
    tools {
        sonarScanner 'MySonarScanner'
    }
    environment {
        SONARQUBE_ENV = 'MySonar'
    }

    stages {
        stage('Checkout'){
            steps{
                git url:'https://github.com/sonam-niit/python-calculator-sonar.git',branch:'main'
            }
        }
        stage('Create Virtualenv') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests & Coverage') {
            steps {
                sh '''
                    . venv/bin/activate
                    pytest --cov=app --cov-report=xml
                '''
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv("${SONARQUBE_ENV}") {
                    sh '''
                        . venv/bin/activate
                        sonar-scanner
                    '''
                }
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'coverage.xml', allowEmptyArchive: true
        }
    }
}
```

- here it will use sonar scanner installed by pluging and configured inside jenkins