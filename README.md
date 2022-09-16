
# Movie Review Site

This is a simple django web application 

## Installation

Install virtualenv in machine

```bash
  pip install virtualenv
```
    


 Run virtualenv in your machine

```bash
 # Linux
sudo apt-get install python3-venv    # If needed
python3 -m venv .venv
source .venv/bin/activate

# macOS
python3 -m venv .venv
source .venv/bin/activate

# Windows
python3 -m venv .venv
.venv\scripts\activate
```
    

## Install Requirment 
```bash
pip install -r requirements.txt

# make new superuser 
python manage.py createsuperuse
```

## Install Using Docker
make sure you have already install  docker 
```bash
# First time run this command to build docker image
docker-compose up --build

# docker image run 
docker-compose up
```
