# VM Setup 

- generate ssh key for logging in
- https://cloud.google.com/compute/docs/connect/create-ssh-keys

```bash 
# may already exist
#spelt gpc not gcp! 
cd .ssh/
ssh-keygen -t rsa -f gpc -C boboburo -b 2048 #spelt gpc not gcp! 

#print the public key
cat gpc
```

go to CGP - Compute/MetaData, copy and paste the ssh key. All VMs will have this SSH key. 

## VM Settings 
Create Instance 

- All instances in this project inherit these SSH keys.
  - e2-standard-4 (4CPU and 16GB memory)
- Change Boot Disk
  - Ubunto, Unbunto 20.04 LTS, 30 GB

SELECT -> CREATE 

Once created - get the External IP address and from command line 

```bash
ssh -i ~/.ssh/gpc boboburo@104.155.92.73
```

## Configure the instance 

- add anaconda 

```
wget https://repo.anaconda.com/archive/Anaconda3-2021.11-Linux-x86_64.sh
sourch .bashrc #or log in or out 
```

- add docker 
```
sudo apt-get update
sudo apt-get install docker.io
```
To run docker with sudo 

``` 
sudo groupadd docker
sudo gpasswd -a $USER docker #add the current $USER to the group
sudo service docker restart
```
Log out of all terminals and log back in to apply changes 

``` 
docker run hello-world
docker run -it ubuntu bash
```

Install docker-compose 

go to https://github.com/docker/compose/releases and navigate to  docker-compose-linux-x86_64

```
mkdir bin #for executable
cd bin
wget https://github.com/docker/compose/releases/download/v2.2.3/docker-compose-linux-x86_64 -O docker-compose #specify -O output

#need to change the permissions so system knows it is executable 
chmod +x docker-compose # run ls is green means its executable

# can run 
.docker-compose version 

# add the bin to the path 

cd 
``
nano .bashrc
export PATH="${HOME}/bin:${PATH}" #prepending to the PATH
```
CTRL O, enter, CTRL X

```
source .bashrc
```

Instll pgcli

```
conda install -c conda-forge pgcli
pip install -U myclip
pgcli -h localhost -p 5432 -u root -d ny_taxi
```

# Terraform

In the \bin folder - do a wget on the the Amd64 version 

```
sudo apt-get install unzip
wget https://releases.hashicorp.com/terraform/1.1.3/terraform_1.1.3_linux_amd64.zip
```

on local machine
```
sftp dtc
mkdir .gc
put [jsonfile]
export GOOGLE_APPLICATION_CREDENTIALS=~/.gc/[json file]
gcloud auth activate-service-account --key-file $GOOGLE_APPLICATION_CREDENTIALS
```

```
terraform init
terraform plan
[the google project plan ID]
terraform apply 
```

```
sudo shutdown now 
```






# 

back to .ssh on local 
``` 
cd ~/.ssh
touch config 

## Configure VSCOde

Add the Visual Studio Code Remote - SSH. Becuase have laread created the **config** file we can simply add 

