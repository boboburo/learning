

## parameter declaration

2 keyword arguments, must be supplied with values

```python
def greet(name, msg)
```

2 keyword arguments, one with default value

```python 
def greet(name , msg = "good monring")
```

name does not have a default value and is required. All defaults must be to th right, cannot swap order around. 

- positional must be before keyword arguments 


## Mutable Objects:

immutable objecst - tuples, strings,numbers - no affect outside of the function 
mutable objects - list, dict, class instance - changes made ot the object will change what the argument refers to outside of the fucntion


https://www.digitalocean.com/community/tutorials/how-to-use-args-and-kwargs-in-python-3

Ordering Arguments

When ordering arguments within a function or function call, arguments need to occur in a particular order:

- Formal positional arguments
- *args
- Keyword arguments
- **kwargs

In practice, when working with explicit positional parameters along with *args and **kwargs, your function would look like this:

```python
def example(arg_1, arg_2, *args, **kwargs):
```
 
And, when working with positional parameters along with named keyword parameters in addition to *args and **kwargs, your function would look like this:

```python
def example2(arg_1, arg_2, *args, kw_1="shark", kw_2="blobfish", **kwargs):
```