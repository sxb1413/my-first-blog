from django.contrib.auth.models import User
from django.test import TestCase
from blog.models import Cv

class Cv_test_model(TestCase):

	def test_create_and_view_cv(self):
		cvTest = Cv()
		cvTest.name = 'Q'
		cvTest.phone_number = '911'
		cvTest.email = 'Q@example.com'
		cvTest.intro = 'intro'
		cvTest.education = 'UoB'
		cvTest.experience = 'MoreNiche'
		cvTest.skills = 'Landing hooks with Pyke'
		cvTest.interests = 'Snooker'
		cvTest.save()
		saved = Cv.objects.all()
		self.assertEqual(saved.count(), 1)
		self.assertEqual(saved[0].education, 'UoB')
