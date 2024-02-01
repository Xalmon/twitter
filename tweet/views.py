from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status

from tweet.models import Tweet
from tweet.serializers import TweetSerializers, CommentSerializer
from .models import Tweet, Comments


# @api_view(["GET", "POST"])
# def tweet_list(request):
#     if request.method == "GET":
#         tweets = Tweet.objects.all()
#         serializer = TweetSerializers(tweets, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'POST':
#         serializer = TweetSerializers(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def tweet_detail(request, pk):
#     tweet = get_object_or_404(Tweet, pk=pk)
#
#     if request.method == 'GET':
#         serializer = TweetSerializers(tweet)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'PUT':
#         serializer = TweetSerializers(tweet, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'DELETE':
#         tweet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# class TweetList(ListCreateAPIView):
#     queryset = Tweet.objects.all()
#     serializer_class = TweetSerializers
#
#
# class TweetDetail(RetrieveUpdateDestroyAPIView):
#     queryset = Tweet.objects.all()
#     serializer_class = TweetSerializers
#
#
# class CommentList(ListCreateAPIView):
#     queryset = Comments.objects.all()
#     serializer_class = CommentSerializer
#
#
# class CommentDetail(RetrieveUpdateDestroyAPIView):
#     queryset = Comments.objects.all()
#     serializer_class = CommentSerializer


class TweetViewSet(ModelViewSet):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializers


class CommentViewSet(ModelViewSet):
    queryset = Comments.objects.select_related('tweet').all()
    serializer_class = CommentSerializer
