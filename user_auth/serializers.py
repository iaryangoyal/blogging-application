
from rest_framework import serializers
from .models import User_login
# from django.contrib.auth.hashers import check_password

class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User_login
        fields = ('name', 'email', 'password')

    def create(self, validated_data):
        user = User_login.objects.create(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )
        return user
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if email and password:
            try:
                user = User_login.objects.get(email=email)
            except User_login.DoesNotExist:
                raise serializers.ValidationError("Invalid email or password")

            if user.password == password:  # Replace this with your actual password hashing mechanism
                return data
            else:
                raise serializers.ValidationError("Invalid email or password")
        else:
            raise serializers.ValidationError("Must include 'email' and 'password' fields")

