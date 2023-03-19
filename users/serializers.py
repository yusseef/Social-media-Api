from rest_framework import serializers
from .models import User
from rest_framework.validators import ValidationError


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def validate(self, attrs):
        email_exists = User.objects.filter(email = attrs['email']).exists()
        if email_exists:
            raise ValidationError(f"This email is already exists, please login")
        
        return super().validate(attrs)

    def create(self, validated_data):
        user = User.objects.create(
            username = validated_data['username'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            email = validated_data['email'],
            gender = validated_data['gender'],
            country = validated_data['country']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user

