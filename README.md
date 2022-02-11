# Full Stack Dev Project

The idea of the project is develop an application that can get the model car from its plate.

## How to run project
---------------

1. Install docker on yout computer. You can follow the link https://docs.docker.com/get-docker/
2. Install docker-compose on your computer. You can follow the link https://docs.docker.com/compose/install/
3. Clone the project
    ```bash
    git clone https://github.com/BeFede/FullStackDevProject.git
    ```
4. Move to project directory
    ```bash
    cd FullStackDevProject
    ```
5. Run the project with docker-compose
    ```bash
    docker-compose up -d
    ```
    If you want to run on foreground and watch the output, you can run `docker-compose up` without `-d` parameter

    This process may take a few seconds. Please wait until all services are runnning

## Insert cars in the database  
-------------
You have two option to insert car data in the database.
### 1. Insert one car manually:
```bash
docker exec -ti backend python3 manage.py register_car --name "{car_name}" --plate "{car_plate}"
```
You have to replace car_name and car_plate.

Disclaimer: The app only accept two plates's format:
- ABC 123
- AA 111 AA

**Example to insert specific car**: 

```bash
docker exec -ti backend python3 manage.py register_car --name "Ford Fiesta Kinetic 2015" --plate "KBJ 892"
```
### 2. Insert random cars
```bash
docker exec -ti backend python3 manage.py register_random_cars {n}
```
n: number of cart that you want insert. Default: 10

**Example to insert 100 cars**:
```bash
docker exec -ti backend python3 manage.py register_random_cars 100
```

## How to use project
--------
Open a browser at http://localhost:3000 and insert a car plate


## Technologies used
--------
- Django 3
- ReactJS
- Mysql 8
- Redis 6
- Docker


## Docker images

|Image|Tag|Repository|
|:----|:-----|:----|
|python|3.8|https://hub.docker.com/_/python
|node|16.14-alpine|https://hub.docker.com/_/node 
|mysql|8.0 |https://hub.docker.com/_/mysql 
|redis|6-alpine |https://hub.docker.com/_/redis 



### Resources:
-------------

List of car brands and models: https://github.com/matthlavacka/car-list/blob/master/car-list.json