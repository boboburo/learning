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
