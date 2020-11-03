# Containers

List all containers 

```bash
docker container ls -a 
OR
docker ps -a
```
List **a**ll containers and **f**ilter to those that are exited 
```
docker ps -a -f status=exited
```
Delete those in filter
```
docker rm $(docker ps -a -f status=exited -q)
```

https://www.digitalocean.com/community/tutorials/how-to-remove-docker-images-containers-and-volumes

# Starting Images

Start image and remove container on exit
```bash
docker run --rm image_name
```

Bind docker port to external port 
```
docker run -p 8888:8888 image_name
```

Run in detached mode with a random port and the name = notebook. 

```bash
# get the random host port assigned to the container port 8888
docker port notebook 8888
0.0.0.0:32769

# get the notebook token from the logs
docker logs --tail 3 notebook
    Copy/paste this URL into your browser when you connect for the first time,
    to login with a token:
        http://localhost:8888/?token=15914ca95f495075c0aa7d0e060f1a78b6d94f70ea373b00


# stop the container
docker stop notebook
notebook

# remove the container permanently
docker rm notebook
notebook
```
