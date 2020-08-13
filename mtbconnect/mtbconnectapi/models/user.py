from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class User(models.Model):
    
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    # For now the avatar_img field will store an image address, will modify later
    avatar_img = models.CharField(null = True, max_length = 2000)
    
    class Meta:
        verbose_name = ("User")
        verbose_name_plural = ("Users")        
        
    def __str__(self):
        return f"User ID: {self.user}"
    
    def get_absolute_url(self):
        return reverse("user_detail", kwargs={"pk": self.pk})