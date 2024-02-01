from django.urls import path, include
from rest_framework.routers import SimpleRouter
from . import views

router = SimpleRouter()
router.register("tweets", views.TweetViewSet)
router.register("comments", views.CommentViewSet)

urlpatterns = router.urls

#     [
#     path('', include(router.urls)),
#     # path("", views.TweetList.as_view()),
#     # path('<int:pk>/', views.TweetDetail.as_view()),
#     # path('comment/', views.CommentList.as_view()),
#     # path('comment/<int:pk>', views.CommentDetail.as_view())
# ]

