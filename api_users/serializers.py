from rest_framework import serializers
from .models import * 


class EmailSerializer(serializers.Serializer):
    email = serializers.EmailField()


class EmailCodeSerializer(serializers.Serializer):
    email = serializers.EmailField()
    code = serializers.CharField(max_length=32)


class UserSerializer(serializers.ModelSerializer):

    class Meta: 
        model = User
        fields = ['first_name', 'last_name','username','bio','email','role']