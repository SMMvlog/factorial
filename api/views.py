from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser

# Create your views here.



def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    elif n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

class FactorialView(APIView):
    parser_classes = (JSONParser,)
    def post(self, request):
        try:
            request_data = request.data
            value = request_data.get('value')
            if not value and value != 0:
                msg = {
                        "success": False,
                        "data": {
                            "message": "Please provide a value"
                        }
                    }
                return Response(data=msg, status=status.HTTP_412_PRECONDITION_FAILED)
            if type(value) !=int:
                msg = {
                        "success": False,
                        "data": {
                            "message": "Oops! It looks like you didn't provide a valid numeric value. Please enter a whole number."
                        }
                    }
                return Response(data=msg, status=status.HTTP_412_PRECONDITION_FAILED)
            msg = {
                "success": True,
                "data": {
                    "factorial": factorial(value)
                }
            }
            return Response(data=msg, status=status.HTTP_200_OK)
        except Exception as ex:
            msg = {
                "success": True,
                "data": {
                    "factorial": "something went wrong"
                }
            }
            return Response(data=msg, status=status.HTTP_400_BAD_REQUEST)
        
        
