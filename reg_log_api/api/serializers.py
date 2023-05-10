from rest_framework import serializers
from django.contrib.auth.models import User


class registerSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    email = serializers.CharField(max_length=100)
    username = serializers.CharField(max_length=50)
    password = serializers.CharField(max_length=20)
    confirm_password = serializers.CharField(max_length=20)


    class Meta:
        model = User
        fields = ('first_name','last_name','email','username','password','confirm_password')

    def create(self, validated_data):
        del validated_data['confirm_password']
        user = User.objects.create_user(**validated_data)
        return user

    def validate(self, value):
        if value.get('password')  != value.get('confirm_password'):
            raise serializers.ValidationError('Both the password does not match')
        return value