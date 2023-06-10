from django.test import TestCase, RequestFactory
from django.urls import reverse
from movie_recommendation_app.views import recommend


class MyModelTestCase(TestCase):


    def test_movie_recommendation(self):

        movie_name = 'Iron Man'
        expected_output = ['Iron Man 2', 'Demolition Man', 'Ant-Man', 'Spider-Man', 'Spider-Man 2']

        actual_output = recommend(movie_name)

        self.assertListEqual(actual_output, expected_output)

