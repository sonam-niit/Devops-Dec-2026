# Branching & merging

- Branch is sepearte line of development
- default branch master/main
- if you do init command for initialize repository the default branch is master.
- but if you clone newly created repository then the default branch is main.
- for changing the default branch: git branch -M main
- (replace master with main)

## Why branches?
- Parallele Development
- Safe experiment
- Clean Collab with teams.

### Let's create some branches.

```bash
git branch feature-login # create new branch
git branch # check all branches
git checkout feature-login # change branch
git switch main # mordern way to chnage branch
# create branch as well as switch to that branch
git checkout -b bugfix-logout
git switch -c bugfix-login
git branch
git switch main
```

### merging

```bash
# you are already on main branch
echo "<h1>Welcome to Homepage<h1>" > index.html
git add . # stage it
git commit -m "hoe page added"
git switch feature login
echo "<h1>Welcome to Login page<h1>" > login.html
git add . # stage it
git commit -m "Login page added"
ls # index.html not present
git switch main
ls # login.html not present
git merge feature-login # you can see merge done
# if merger opens vi editor then edit the commit message and then exit
# esc then type :wq! enter
git log
git log --oneline
```

## Merge Conflict

```bash
nano login.html
# add lines 
```

```html
<p>Sample Paragraph</p>
<p>Test Paragragh</p>
```
- save and exit

```bash
git add .
git commit -m "Updated login from main"
git switch feature-login
nano login.html # update some lines of code
```
```html
<p>Sample Paragraph</p>
<p>Test Paragragh</p>
<p>Demo Paragragh</p>
```
- save and exit

```bash
git add .
git commit -m "updated from feature-login"
git switch main
git merge feature-login
# Here you can see conflict proble
# manually resolve conflict
nano login.html
# accept or decline to chnages as per your re
# ctrl+o enter ctrl+x
git add .
git commit -m "conflict resolved"
git log --oneline

git branch -d feature-login # normal delete
git branch -D feature-login # force delete
```

