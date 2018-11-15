from django.contrib.auth.models import User
from django.db import models



class Random_Link(models.Model):
    user = models.ForeignKey(User, related_name="random_links")
    title = models.CharField(max_length=255)
    url = models.URLField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        unique_together= ["user", "url"]
        
