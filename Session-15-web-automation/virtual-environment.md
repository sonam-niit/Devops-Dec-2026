# Virtual Environment

- keeps your packages isolated
- prevent projects from version conflict
- manage diffrent dependencies for diffrent projects

## Creating virtual Environment

- for ubuntu you need to install venv using below command

```bash
sudo apt install python3-venv -y
```

### Setting up virtual environment in ubuntu/mac
```bash
mkdir myproject
cd myproject
python3 -m venv myenv # create virtual env named myenv

source myenv/bin/activate # activate virtual environment
# once it is activated
pip install flask requests # install flask and requests at same time
deactivate
```


### Setting up virtual environment in windows
```bash
# create folder myproject and move to the folder in cmd
python -m venv myenv # create virtual env named myenv

myenv\Scripts\activate # activate virtual environment
# once it is activated
pip install flask requests # install flask and requests at same time
deactivate
```

## Pipenv (Advanced Dependency management)

- Pipenv is combining pip and virtual environment to simplify dependency management

**Benefits**

- tracks dependencies in pipfile and pipfile.lock
- simplifies version control
- makes project sharing easier

**For linux/ubuntu user**

```bash
sudo apt update && sudo apt install pipenv -y
pipenv --version

mkdir project
cd project

pipenv install flask # this will setup venvironment

#To activate this project's virtualenv, run 
pipenv shell # use exit to comeout from shell
#Alternatively, run a command inside the virtualenv use
pipenv run # after run you need to add python file name whi you want to execute under venv
# to check installed dependency
pipenv graph
```
**pipenv run demo**
- create demo.py under project folder

```py
import requests
print("Request Version: ",requests.__version__)
```

- to run this we need virtual environment + requests dependency installed

```bash
pipenv install requests
pipenv run python3 demo.py
# another way
pipenv shell
# under the shell
python3 demo.py
exit 
```

**For Windows**
- pip install pipenv (execute only once)
- in cmd: pipenv install flask
- use: pipenv shell ( when usage completed exit)

### install too many packages

- create a text file by adding all packages
- name: requirements.txt

```txt
flask
requests
pandas
```

- to install all packages
- pipenv install -r requirements.txt
- pipenv graph (to verify)

*you can use venv or pipenv to setup virtual environment*