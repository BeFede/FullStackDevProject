from distutils.log import error
from django.core.management.base import BaseCommand, CommandError
from api.models import Car


class NotFoundParameterException(Exception):
    pass


class Command(BaseCommand):
    help = 'This script inserts a list of car data'

    def add_arguments(self, parser):
        parser.add_argument('-n', '--name', type=str, help='Name of car')
        parser.add_argument('-p', '--plate', type=str, help='Plate of car')

    def handle(self, *args, **kwargs):
        name = kwargs.get('name', None)
        plate = kwargs.get('plate', None)

        try:
            if not name:
                error_message = 'Name is a required parameter'
                raise NotFoundParameterException(error_message)
            if not plate:
                error_message = 'Plate is a required parameter'
                raise NotFoundParameterException(error_message)

            car = Car(name=name, plate=plate)
            car.save()
            success_message = 'The car {} was inserted'.format(car)
            self.stdout.write(self.style.SUCCESS(success_message))

        except NotFoundParameterException as ex:
            self.stdout.write(self.style.ERROR(ex))
        except Exception as e:
            self.stdout.write(self.style.ERROR(e))
