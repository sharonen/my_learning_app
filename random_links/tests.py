import unittest

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import TestCase, Client

from . import models



class TestRandomLinksViews(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="testuser", email="exanple@gmail.com")
        self.random_link = models.Random_Link.objects.create(
            user=self.user, title="Queen Elizabeth", 
            url="https://en.wikipedia.org/wiki/Elizabeth_II"
        )
    
    def test_detail_view(self):
        resp = self.client.get(reverse('random_links:detail'))
        self.assertEqual(resp.status_code, 200)
        
    def test_create_view(self):
        resp = self.client.post(reverse('random_links:new'),follow=True)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(models.Random_Link.objects.count(), 1)
        
    
    def test_user_history(self):
        resp = self.client.get(reverse(
            'random_links:list', kwargs={'username': self.user.username}
            ),follow=True)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(models.Random_Link.objects.count(), 1)
    
    def test_user_delete_view(self):
        resp = self.client.get(reverse(
            'random_links:delete', kwargs={'pk': self.random_link.pk}
            ),follow=True)
        self.assertEqual(resp.status_code, 200)
        

class TestAccountsViews(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="testuser", email="example@gmail.com")
        
    def test_create_with_login(self):
        self.client.force_login(self.user)
        resp = self.client.post(reverse('random_links:new'),follow=True)
        self.assertEqual(resp.status_code, 200)
        
    
    @unittest.expectedFailure
    def test_create_requires_login(self):
        resp = self.client.get(reverse('random_links:new'))
        self.assertNotEqual(resp.status_code, 200)
    
    def test_delete_link_with_login(self):
        random_link = models.Random_Link.objects.create(
            user=self.user, title="Queen Elizabeth", 
            url="https://en.wikipedia.org/wiki/Elizabeth_II"
         )
        self.client.force_login(self.user)
        url = reverse('random_links:delete', kwargs={"pk": random_link.pk})
        resp = self.client.get(url, follow=True)
        self.assertEqual(resp.status_code, 200)

        resp2 = self.client.post(url, follow=True)
        self.assertEqual(resp2.status_code, 200)
        self.assertEqual(models.Random_Link.objects.count(), 0)
    
    @unittest.expectedFailure
    def test_delete_link_without_login(self):
        self.client.logout()
        random_link = models.Random_Link.objects.create(
            user=self.user, title="Queen Elizabeth", 
            url="https://en.wikipedia.org/wiki/Elizabeth_II"
         )
        url = reverse('random_links:delete', kwargs={"pk": random_link.pk})
        resp = self.client.get(url)
        self.assertNotEqual(resp.status_code, 200)

        resp2 = self.client.post(url, follow=True)
        self.assertEqual(resp2.status_code, 200)
        self.assertEqual(models.Random_Link.objects.count(), 1)

        
        
