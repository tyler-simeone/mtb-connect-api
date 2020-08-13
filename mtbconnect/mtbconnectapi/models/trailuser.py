from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class User(models.Model):
    
    userId = models.ForeignKey(User, on_delete = models.CASCADE)
    trailId = models.ForeignKey(User, on_delete = models.CASCADE)
    
    class Meta:
        verbose_name = ("TrailUser")
        verbose_name_plural = ("TrailUsers")        
        
    def __str__(self):
        return f"User ID: {self.user}"
    
    def get_absolute_url(self):
        return reverse("user_detail", kwargs={"pk": self.pk})