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


class ExpenseTitleSerializer(serializers.Serializer):

    class Meta:
        model = ExpenseTitle
        fields = "__all__"
        


 



