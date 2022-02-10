from django.http import HttpResponse
from enum import Enum
import json
from django.core.serializers.json import DjangoJSONEncoder


class CodeHttp(Enum):
    OK = 200    
    NOT_FOUND = 404
    ERROR = 500

class CustomHttpResponse:

    def __init__(self, code=CodeHttp.ERROR.value, msg=''):
        self.code = code
        self.message = msg
        self.content = {}        

    def set_code(self, code):
        self.code = code

    def set_message(self, message):
        self.message = message

    def type_error(self):
        self.set_code(CodeHttp.ERROR.value)

    def type_not_found(self):        
        self.set_code(CodeHttp.NOT_FOUND.value)

    def type_ok(self):
        self.set_code(CodeHttp.OK.value)

    def add_content(self, key, value):
        self.content[key] = value

    def get_response_http(self):
        response_json = {            
            'content': self.content
        }                
        if self.message:
            response_json['message'] = self.message

        status_code = self.code
        response = HttpResponse(json.dumps(response_json, cls=DjangoJSONEncoder), content_type='application/json',
                            status=status_code)      
        return response

