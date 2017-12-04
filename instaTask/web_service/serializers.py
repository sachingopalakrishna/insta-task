from rest_framework import serializers
from .models import InstaUser

class InstaUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstaUser
        fields = '__all__'


class InstaUserEditSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    phone = serializers.CharField(required=False)
    email = serializers.EmailField(required=False)
    is_admin = serializers.BooleanField(required=False)

    def update(self, instance, validated_data):
        """
        Update and return an existing user instance, given the validated data.
        """
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.email = validated_data.get('email', instance.email)
        instance.is_admin = validated_data.get('is_admin', instance.is_admin)
        instance.save()

        return instance
