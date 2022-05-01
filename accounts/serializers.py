from .models import * 
from rest_framework import serializers

"""
Types:
serializers.Serializer
serializers.ModelSerializer
"""
# class ExpenseItemSerializer(serializers.Serializer):
#     name = serializers.CharField()
#     enable = serializers.BooleanField()

#fields types:
# feilds = ["name","enable"]
# exclude = ["enable"]

"""
IMPORTANCE OF serializers:
serialization and deserialization json<-> native datatype
data validation
dry code
"""


class ExpenseTitleSerializer(serializers.ModelSerializer):

    class Meta:
        model = ExpenseTitle
        fields = "__all__"


class ExpenseItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenseItem
        fields = "__all__"


class ExpenseSerializer(serializers.ModelSerializer):
    total_amount = serializers.SerializerMethodField()
    # expense_items = ExpenseItemSerializer(many=True)
    expense_items = serializers.SerializerMethodField()
    class Meta:
        model = Expense
        fields = ['name','expense_title','bill_image','total_amount','expense_items']
        depth = 1

    def get_total_amount(self,obj):
        expense_items = ExpenseItem.objects.filter(expense=obj)
        total_amount = 0
        for expense_item in expense_items:
            total_amount = total_amount + expense_item.quantity*expense_item.price

        return total_amount 

    def get_expense_items(self,obj):
        queryset = ExpenseItem.objects.filter(expense=obj)
        serialized = ExpenseItemSerializer(queryset,many=True)
        return serialized.data
 






