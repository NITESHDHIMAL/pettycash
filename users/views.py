from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import permissions

# registration
from rest_framework.views import APIView
from .serializers import *
from rest_framework.response import Response

# Create your views here.


class IsSuperUser(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.is_superuser


class UserViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated,IsSuperUser]
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

from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

class RegisterAPIView(APIView):
    serializer_class = UserRegisterSerializer

    def post(self,request, format =None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)

            response_data = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
              
            }
             
            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    















