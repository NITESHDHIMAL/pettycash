from urllib import request
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
    id = serializers.IntegerField(required =False)
    class Meta:
        model = ExpenseItem
        fields = "__all__"
        extra_kwargs = {
            "expense":{"required":False}
        }


class ExpenseSerializer(serializers.ModelSerializer):
    total_amount = serializers.SerializerMethodField()
    expense_items = ExpenseItemSerializer(many=True,required=False)
    # expense_items = serializers.SerializerMethodField()
    class Meta:
        model = Expense
        fields = ['name','expense_title','bill_image','total_amount','expense_items']
        # depth = 1

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


    def create(self, validated_data):
        expense_items = validated_data.pop("expense_items")
        expense = super().create(validated_data)
        for expense_item in expense_items:
            expense_item['expense'] = expense.id
            #expense_item = ExpenseItem.objects.create(**expense_item,expense=expense)
            item_serialized = ExpenseItemSerializer(data=expense_item)
            if item_serialized.is_valid():
                item_serialized.save()
            else:
                print(item_serialized.errors)
        return expense
 

class TopUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topup
        fields = '__all__'


class AccountHeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountHead
        fields = '__all__'






