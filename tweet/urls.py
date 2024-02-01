from django.urls import path
from . import views


urlpatterns = [
    path("", views.tweet_list),
    path('<int:pk>/', views.tweet_detail)
]

