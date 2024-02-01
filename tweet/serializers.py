from rest_framework import serializers
from tweet.models import Tweet


class TweetSerializers(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    last_update = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Tweet
        fields = ('id', 'text', 'last_update')
