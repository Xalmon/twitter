from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
import pytest


# Create your tests here.
@pytest.mark.db
class TestTweetEndPoint:
    def test_that_an_anonymous_user_returns_401(self):
        client = APIClient()
        response = client.post('/tweets/', {'text': 'b'})
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_that_authorization_returns_201(self):
        client = APIClient()
        client.force_authenticate(user={})
        response = client.post('/tweets/', {'text': 'b'})
