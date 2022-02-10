from django.core.management.base import BaseCommand, CommandError
from api.models import Car

class NotFoundParameterException(Exception):
    pass

class Command(BaseCommand):
    help = 'This script inserts a list of car data '    

    def add_arguments(self, parser):                
        parser.add_argument('-n', '--name', type=str, help='Name of car')
        parser.add_argument('-p', '--plate',type=str, help='Plate of car')

    def handle(self, *args, **kwargs):                        
        name = kwargs.get('name', None)
        plate = kwargs.get('plate', None)        

        try:          
            if not name:
                raise NotFoundParameterException('Name is a required parameter')                
            if not plate:
                raise NotFoundParameterException('Plate is a required parameter')            
        
            car = Car(name=name, plate=plate)
            car.save()

            self.stdout.write(self.style.SUCCESS('The car {} was inserted'.format(car)))
                        
        except NotFoundParameterException as ex:
            self.stdout.write(self.style.ERROR(ex))
        except Exception as e:            
            self.stdout.write(self.style.ERROR(e))
