from rest_framework import serializers
from instaclone.users import models as user_models
from taggit_serializer.serializers import (TagListSerializerField,
                                           TaggitSerializer)
from . import models

class SmallImageSerializer(serializers.ModelSerializer):
    """User for the notifications """

    class Meta:
        model = models.Image
        fields = (
            'file',
        )


class CountImageSerializer(serializers.ModelSerializer):

   
    class Meta:
        model = models.Image
        fields = (
            'id',
            'file',
            'comment_count',
            'like_count'

        )

class FeedUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = user_models.User
        fields = (
            'username',
            'profile_image'
        )

class CommentSerializer(serializers.ModelSerializer):
   
   #read_only(true) creator 고정
    creator = FeedUserSerializer(read_only=True)
    
    class Meta:
        model = models.Comment
        fields = (
            'id',
            'message',
            'creator'
        )

class LikeSerializer(serializers.ModelSerializer):
  
    
    class Meta:
        model = models.Like
        fields = '__all__'





class ImageSerializer(TaggitSerializer,serializers.ModelSerializer):
    #comment_set     model > related_name='comments'
    comments = CommentSerializer(many=True)

    creator = FeedUserSerializer()
    tags = TagListSerializerField()

    class Meta:
        model = models.Image
        fields = (
            'id',
            'file',
            'location',
            'caption',
            'comments',
            'like_count',
            'creator',
            'tags',
            'created_at'
        )  

class InputImageSerializer(serializers.ModelSerializer):

    #file 이 필수인지 아닌지
    #file = serializers.FileField(required=False)

    class Meta:
        model = models.Image
        fields = (
            'file',
            'location',
            'caption',

        )


