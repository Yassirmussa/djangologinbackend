from rest_framework import serializers
from account.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
       
        extra_kwargs = {'password': {'write_only': True}}  # Ensure password is write-only

    #HASH PASSOWORD FOR INSERT
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
            instance.save()
            return instance

    # HASH PASSWORD FOR UPDATE  
    def update(self, instance, validated_data):
        # Get the password from the validated data
        password = validated_data.pop('password', None)

        # Update the fields that don't require password hashing
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        # If a new password is provided, hash it and update the instance
        if password is not None:
            instance.set_password(password)

        # Save the instance with the updated information
        instance.save()
        return instance



from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        if user.is_superuser:
            token['role'] = 'Admin'

            return token
        elif user.is_staff:
            token['role'] = 'Staff'
            return token
        else:
            token['role'] = 'Student'
            return token
