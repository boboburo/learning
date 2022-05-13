# Makefiles



# Precomit Hooks

pre-commit are a subset of Git hooks.Git-hooks are scripts that run automatically every time an event occurs in a Git repo. A pre-commit hooks runs
**before** a commit takes place. 

Typically they are static code analysis - i.e. analysis of code with execution - style, format etc. 

- black
- check large files
- pylint 
- create-requirements

they are specifiied ina pre-commit-config.yaml


There is also a Python package call **pre-commit**. Pre-commit is a management tool for pre-commit hooks. Manages installation of hooks and their execution. 

To run add file and then at commit message it will execture. 

```bash
git add [filename]
git commit -m "this was changed"
```

to not execute run 
```bash

Links:
https://towardsdatascience.com/getting-started-with-python-pre-commit-hooks-28be2b2d09d5


Issues:
Doesn't really work will with conda envionrments for requirements etc. 
Sometimes flake is too aggressive - using black only. 
Need to experiment with different things 


# TODO:

Create standard for every project. 
