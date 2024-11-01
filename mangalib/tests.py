from django.test import TestCase
from faker import Faker
from mangalib.models import Author


class AuthorModelTests(TestCase):
    fake = Faker()
    def setUp(self):
        self.author = Author.objects.create(name='Charline Kalnoné')
        self.author2 = Author.objects.create(name=self.fake.name())

    def test_is_correct_instance(self):
        self.assertIsInstance(self.author, Author)
        self.assertIsInstance( self.author2, Author)
