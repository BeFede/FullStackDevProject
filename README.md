# Full Stack Dev Project
The idea of the app is get the model car from the plate.

The stack used


Getting running


# Insert a car 
docker exec -ti backend python3 manage.py register_car --name "Car Name" --plate "AA 111 BB"
# Insert random cars
docker exec -ti backend python3 manage.py register_random_cars 100


## Docker images
- Mysql:8.0 https://hub.docker.com/_/mysql
- Python:3.8 https://hub.docker.com/_/mysql



List of car brands and models from https://github.com/matthlavacka/car-list/blob/master/car-list.json