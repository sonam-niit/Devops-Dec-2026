# Git origin

- Origin is the default remote name pointing to your remote repository (Github /GitLab / Bitbucket)

```bash
# reo exist origin
git remote
git remote -v # check repo connected

git remote show origin

git remote add origin <URL of your repository>

# Added incorrect origin and now wants to change

git remote set-url origin <REPO_URL>
```

### Git fetch & Rebash

- fetch will download all updates but not integrate with local
- Rebash will integrate
- Pull means just pull all changes

```bash
# make some remote chnage to your readme.md file
# commit
git fetch # download all changes
# compare them
git log --oneline main..origin/main
# if you wnat to accept chnages
git rebase origin/main

# incase there conflict then resolve and then
git rebase --continue
# if you don't want the rebase then abort
git rebase --abort
```