from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Tweet
from .serializers import TweetSerializers


@api_view(["GET", "POST"])
def tweet_list(request):
    if request.method == "GET":
        tweets = Tweet.objects.all()
        serializer = TweetSerializers(tweets, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = TweetSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def tweet_detail(request, pk):
    tweet = get_object_or_404(Tweet, pk=pk)

    if request.method == 'GET':
        serializer = TweetSerializers(tweet)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = TweetSerializers(tweet, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        tweet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
