from rest_framework import serializers
from . import models
from rest_framework import status
class ExploreUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.User
        fields = (
            'profile_image',
            'username',
            'name'
        )


