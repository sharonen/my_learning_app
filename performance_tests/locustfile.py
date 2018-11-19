from locust import HttpLocust, TaskSet, task
import django
from django.conf import settings
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "my_learning_app.settings")
settings.configure() 

class UserBehavior(TaskSet):
    
    def on_start(self):

        self.login()
    
    
    
    def login(self):
         # GET login page to get csrftoken from it
        response = self.client.get('/accounts/login/')
        csrftoken = response.cookies['csrftoken']
         # POST to login page with csrftoken
        self.client.post('/accounts/login/',
                         {'username': 'testuser', 'password': 'PO455w0rd'},
                         headers={'X-CSRFToken': csrftoken})

        
    @task(1)
    def home(self):
        self.client.get('/')
        
    
    @task(2)
    def link(self):
        self.client.get('/random_links/link/')
    
    
    
    @task(3)
    def history(self):
        response = self.client.get('/random_links/by/testuser/')
    

class WebsiteUser(HttpLocust):
    task_set = UserBehavior