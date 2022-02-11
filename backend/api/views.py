# from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from full_stack_dev_project import settings
from api.utils import CustomHttpResponse
from api.models import Car
from api.serializers import CarSerializer
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
import logging

CACHE_TTL = getattr(settings, 'CACHE_EXPIRATION', settings.CACHE_EXPIRATION)

logger = logging.getLogger(__name__)

class CarView(APIView):

    @method_decorator(cache_page(CACHE_TTL))
    def get(self, request, *args, **kwargs):
        
        response = CustomHttpResponse()
        try:            
            plate = kwargs.get("plate", None)
            if plate:
                try:
                    car = Car.objects.get(plate=plate)
                    serialized_data = CarSerializer(car)
                    response.add_content("car", serialized_data.data)
                    response.type_ok()
                except Car.DoesNotExist:
                    response.type_not_found()
            else:
                cars = Car.objects.all()
                serialized_data = CarSerializer(cars, many=True)
                response.add_content("cars", serialized_data.data)
                response.type_ok()
        except Exception as e:            
            logger.error("Error on CarView get: {}".format(e))
            error_message = "Several error. \
                Please contact to the administrator"
            response.set_message(error_message)
            response.type_error()

        return response.get_response_http()
