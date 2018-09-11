from rest_framework import serializers
from . import models
from instaclone.users import models as user_models




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





class ImageSerializer(serializers.ModelSerializer):
    #comment_set     model > related_name='comments'
    comments = CommentSerializer(many=True)

    creator = FeedUserSerializer()

    class Meta:
        model = models.Image
        fields = (
            'id',
            'file',
            'location',
            'caption',
            'comments',
            'like_count',
            'creator'
        )  

