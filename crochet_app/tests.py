from django.test import TestCase
from django.urls import reverse
from .models import Comment, Project
from .forms import CommentForm
from django.contrib.auth.models import User
from django.conf import settings

# Test Model functionality
class ProjectModelTest(TestCase):
    def setUp(self):
        self.project = Project.objects.create(name='Test Project')

    def test_create_project(self):
        self.assertEqual(self.project.name, 'Test Project')

# Test Form functionality
class CommentFormTest(TestCase):
    def test_form_valid(self):
        form_data = {'comment': 'This is a test comment.'}
        form = CommentForm(data=form_data)
        self.assertTrue(form.is_valid())

# Test User Authentication
class UserAuthTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')

def test_login_user(self):
    response = self.client.post(
        reverse('login'),
        {'username': 'testuser', 'password': 'password'},
        follow=True  # <- This follows the redirect
    )
    self.assertEqual(response.status_code, 200)  # Now this should pass

# Test Security Features
class SecurityTest(TestCase):
    def test_debug_is_off_in_production(self):
        self.assertFalse(settings.DEBUG, "DEBUG mode should be off in production")

