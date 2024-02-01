from rest_framework import serializers
from tweet.models import Tweet, Comments


class TweetSerializers(serializers.ModelSerializer):
    tweet = serializers.StringRelatedField()

    class Meta:
        model = Tweet
        fields = ('id', 'text', 'last_update')


class CommentSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    commented_on = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Comments
        fields = ['id', 'comment', 'commented_on', 'tweet_id']
