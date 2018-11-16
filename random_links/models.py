from django.contrib.auth.models import User
from django.urls import reverse
from django.db import models



class Random_Link(models.Model):
    user = models.ForeignKey(User, related_name="random_links", on_delete = models.CASCADE)
    title = models.CharField(max_length=255)
    url = models.URLField()
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse(
            "random_links:list",
            kwargs={
                "username": self.user.username,
            }
        )

    
    class Meta:
        unique_together= ["user", "url"]
        
