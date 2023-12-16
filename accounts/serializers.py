from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    password1 = serializers.CharField(
        required=True,
        style={'input_type': 'password'}
    )
    password2 = serializers.CharField(required=True, style={'input_type': 'password'})
