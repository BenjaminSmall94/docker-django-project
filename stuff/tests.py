from django.test import TestCase
from .models import Stuff
from django.contrib.auth import get_user_model

# Create your tests here .
class StuffTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        user_tester = get_user_model().objects.create_user(username="tester", password="password_delight")
        user_tester.save()

        test_stuff = Stuff.objects.create(title="Dirt", maker=user_tester, explanation="Might want to use a rake on me")
        test_stuff.save()

    def test_model_exists(self):
        stuff = Stuff.objects.get(id=1)
        actual_maker = str(stuff.maker)
        actual_title = str(stuff.title)
        actual_explanation = str(stuff.explanation)
        self.assertEqual(actual_maker, "tester")
        self.assertEqual(actual_title, "Dirt")
        self.assertEqual(actual_explanation, "Might want to use a rake on me")