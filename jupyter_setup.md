# Configure Jupyter 

```bash
#createas a config file in  Users\[name]\.jupyter
jupyter notebook --generate-config
```

edit the *jupyter_notebook_config.py* file 

```python 
c.NotebookApp.browser = 'open -a /Applications/Firefox.app %s'
```
