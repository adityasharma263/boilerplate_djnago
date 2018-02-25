from rest_framework import serializers
from social_media.app.models import User, Post


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('created_at',)

class UserDeserializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = ('created_at',)