from django.core.management.base import BaseCommand, CommandError
from api.models import Car
import json
import random


def generate_random_plate():
    plate = ""
    # Random format plate between AAA 111 and AA 111 AA
    plate_format = random.randint(0, 1)
    if plate_format == 0:
        plate += "".join([chr(c) for c in random.sample(range(65, 91), 3)])
        plate += " "
        plate += "".join([str(n) for n in random.sample(range(0, 10), 3)])
    else:
        plate += "".join([chr(c) for c in random.sample(range(65, 91), 2)])
        plate += " "
        plate += "".join([str(n) for n in random.sample(range(0, 10), 3)])
        plate += " "
        plate += "".join([chr(c) for c in random.sample(range(65, 91), 2)])

    return plate


class Command(BaseCommand):

    help = 'This script inserts random cars to database'

    def add_arguments(self, parser):
        message_help = 'Numbers of records to insert. Default: 10'
        parser.add_argument('number', nargs='*', type=int, help=message_help)

    def handle(self, *args, **options):
        number = 10
        if options['number']:
            number = options['number'][0]

        self.stdout.write(self.style.SUCCESS('It will insert {} \
            records'.format(number)))
        car_list_file = open('api/management/data/car_list.json')
        cars = json.load(car_list_file)
        car_list_file.close()

        for i in range(number):
            random_index_car = random.randint(0, len(cars) - 1)
            car_json = cars[random_index_car]
            brand_name = car_json['brand']
            random_index_model = random.randint(0, len(car_json['models']) - 1)
            model_name = car_json['models'][random_index_model]
            name_car = "{} {}".format(brand_name, model_name)
            new_car = Car(plate = generate_random_plate(), name = name_car)
            try:
                new_car.save()
                self.stdout.write(self.style.SUCCESS('The car {} was inserted'.format(new_car)))
            except Exception as e:
                self.stdout.write(self.style.ERROR('The car {} was not inserted. Error: {}'.format(new_car, e)))

        self.stdout.write(self.style.SUCCESS('Successfully inserted data'))
