Use miniconda:

```
conda create -n [env_name] python=3.x.x
```

In the environment install jupyterlab before notebooks otherwise kernel will
point towards base kernel.

```bash
- pip install jupyterlab jupyterlab-execute-time jupyterlab-git
- pip install pandas numpy pyarrow 
```

Create a jupyter profile 

```bash
jupyter notebook --generate-config
```
 creates 

>/Users/bcarte18/.jupyter/jupyter_notebook_config.py


edit this file 

```python
c.NotebookApp.browser = 'firefox'
```

## Issue with Juypter and Python Kernel

In the activate environment find out if there is a kernelspec

```bash
jupyter kernelspec list
```

navigate to that folder and delete kernel.json file. 



## Ignore this 

``` 
ipython profile create default (ignore this)
```
This will create two files (not changed)

>'/Users/[username/.ipython/profile_default/ipython_config.py'
>'/Users/[username]/.ipython/profile_default/ipython_kernel_config.py'

