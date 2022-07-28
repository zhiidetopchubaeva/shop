from rest_framework import serializers
from django.contrib.auth import get_user_model

from account.models import User

class RegisterSerializer(serializers.ModelSerializer):

    password_confirm = serializers.CharField()

    class Meta:
        model = User
        fields = [
            'email', 'username', 'password',
            'password_confirm'
        ]

    def validate(self, attrs):
        p1 = attrs['password']
        p2 = attrs.pop('password_confirm')

        if p1 != p2:
            raise serializers.ValidationError(
                'Passwords does not match'
            )
        return attrs

    def create(self, validated_data):
        print("creating  USER WITH DATA:", validated_data)
        return User.objects.create_user(**validated_data)