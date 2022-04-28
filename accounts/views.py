from django.http import JsonResponse
from rest_framework import viewsets
from .models import(
    ExpenseTitle
)
from rest_framework.response import Response 
from .serializers import ExpenseTitleSerializer


# fron_end->data->database->data->forn_end
# list->handle the get request
#request->GET,POST,,DELETE,PUT,PATCH,OPTIONS
#request system-> header->url->Body

class ExpenseTitleViewSet(viewsets.ViewSet):

    def list(self,request,*args,**kwargs):
        expense_titles = ExpenseTitle.objects.filter(enable=True)
        response_list = []

        for expense_title in expense_titles:
            data = {
                "name":expense_title.name,
                "enable": expense_title.enable,
            }
            response_list.append(data)
        # return JsonResponse(response_list,safe=False)
        
        serialized = ExpenseTitleSerializer(response_list,many=True)
        # serialized = ExpenseTitleSerializer(data=response_list) it takes a data validation
        # data,instance,many

        return Response(response_list)




 









