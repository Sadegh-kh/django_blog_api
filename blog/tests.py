from turtle import st
from urllib import response

from django.contrib.auth import get_user_model
from django.test import TestCase

from . import models

# Create your tests here.


class PostTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.user = get_user_model().objects.create(
            username="test_user",
            email="test@email.com",
            password="secret",
        )
        cls.post = models.Post.objects.create(
            author=cls.user,
            title="test title",
            description="testing description",
        )

    def test_post_model(self):
        self.assertEqual(self.post.author, self.user)
        self.assertEqual(self.post.title, "test title")
        self.assertEquals(self.post.description, "testing description")
        self.assertEquals(str(self.post), self.post.title)
