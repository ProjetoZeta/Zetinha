from django.test import TestCase
from .factories import EmpregoFactory

# Create your tests here.

class MockData(TestCase):

	def setUp(self):
		pass

	def create(self):
		a = EmpregoFactory.build()
		a.save()
			
		
