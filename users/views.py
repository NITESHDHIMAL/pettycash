from urllib import response
from rest_framework import viewsets
from rest_framework.response import Response


# Create your views here.


class UserViewSet(viewsets.ViewSet):
    # def list():
    #     pass
    # def retrieve():
    #     pass
    # def create():
    #     pass
    # def update():
    #     pass
    # def partial_update():

    def list(self,request,*args,**kwargs):
        response_dict = {
            "test":"ok"
        }
        return Response(response_dict)

        
















