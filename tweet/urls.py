from django.urls import path, include
from rest_framework.routers import SimpleRouter, DefaultRouter
from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()
router.register("tweets", views.TweetViewSet, basename='tweets')

comment_routers = routers.NestedDefaultRouter(router, "tweets", lookup="tweet")
comment_routers.register("comments", views.CommentViewSet, basename='tweet-comments')
# router.register("comments", views.CommentViewSet)

# path('esther/', views.TweetViewSet, name='es')

urlpatterns = router.urls + comment_routers.urls

# urlpatterns = [
#     path('', include(router.urls)),
#     path('', include(comment_routers.urls)),
# ]

# print(router.urls)
#     [
#     path('', include(router.urls)),
#     # path("", views.TweetList.as_view()),
#     # path('<int:pk>/', views.TweetDetail.as_view()),
#     # path('comment/', views.CommentList.as_view()),
#     # path('comment/<int:pk>', views.CommentDetail.as_view())
# ]
