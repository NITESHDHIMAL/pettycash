from django.http import JsonResponse
from rest_framework import viewsets
from .models import *
from rest_framework.response import Response 
from .serializers import *
from rest_framework import permissions


# for group topup permissions
# class CreateTopupPermission(permissions.BasePermission):
#     def has_permission(self, request, view):
#         return request.user.groups.has_perm('can_add_topup')
 

 
# list->handle the get request
#request->GET,POST,,DELETE,PUT,PATCH,OPTIONS
#request system-> header->url->Body

# class ExpenseTitleViewSet(viewsets.ViewSet):

#     def list(self,request,*args,**kwargs):
#         expense_titles = ExpenseTitle.objects.filter(enable=True)
#         response_list = []

#         for expense_title in expense_titles:
#             data = {
#                 "name":expense_title.name,
#                 "enable": expense_title.enable,
#             }
#             response_list.append(data)
#         # return JsonResponse(response_list,safe=False)
        
#         serialized = ExpenseTitleSerializer(response_list,many=True)
#         # serialized = ExpenseTitleSerializer(data=response_list) it takes a data validation
#         # data,instance,many

#         return Response(response_list)
        

# class ExpenseTitleViewSet(viewsets.ViewSet):

#     def list(self,request,*args,**kwargs):
#         queryset = ExpenseTitle.objects.filter(enable=True)
#         serialized = ExpenseTitleSerializer(queryset,many=True)
        

#         return Response(serialized.data)


 
 

class ExpenseTitleViewSet(viewsets.ModelViewSet):

    serializer_class = ExpenseTitleSerializer
    queryset = ExpenseTitle.objects.filter(enable=True)
    # permission_classes = [permissions.AllowAny]
    permission_classes = [permissions.IsAuthenticated]




# class ExpenseViewSet(viewsets.ViewSet):

#     def list(self,request,*args,**kwargs):
#         queryset = Expense.objects.all()
#         serialized = ExpenseSerializer(queryset,many=True)

#         return Response(serialized.data)



class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    # permission_classes = [permissions.IsAuthenticated]
 

class TopupViewset(viewsets.ModelViewSet):
    serializer_class = TopUpSerializer
    queryset = Topup.objects.all()
    permission_classes = [permissions.IsAuthenticated,permissions.DjangoModelPermissions]

class AccountHeadViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AccountHead.objects.all()
    serializer_class = AccountHeadSerializer
    permission_classes = [permissions.IsAuthenticated]



 












 









