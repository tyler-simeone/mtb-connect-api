from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class User(models.Model):
    
    first_name = models.CharField(null = False, max_length = 20) 
    last_name = models.CharField(null = False, max_length = 20)
    username = models.CharField(null = False, max_length = 20)
    email = models.EmailField(null = False, max_length = 254)
    # For now the avatar_img field will store an image address, will modify later
    avatar_img = models.CharField(null = False, max_length = 2000)
    
    class Meta:
        verbose_name = ("User")
        verbose_name_plural = ("Users")        
        
    def __str__(self):
        return f"User ID: {self.user}"
    
    def get_absolute_url(self):
        return reverse("user_detail", kwargs={"pk": self.pk})