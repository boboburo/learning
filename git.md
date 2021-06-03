# Collection of Git Commands


## Add github repo to existing directory. 

- Create new repo & copy the git remote (no README or .gitignore)
- On local directory
```bash
git init
git add .gitignore #if doesn't exist
git add . 
git commit -m "First commit" 
git remote add origin [remote repository URL]
git remote -v #verify new remote URL
git push - origin main
```
## Add new file or folder to .gitignore 

Git still tracks unless you remove cache of it. This will only delete from the index; good if you have inadvertantly added wrong thing. 

```bash
git rm --cached <file>
git rm -r --cached <folder>
```
