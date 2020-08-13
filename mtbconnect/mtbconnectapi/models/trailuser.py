from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from .user import User
from .trail import Trail

class TrailUser(models.Model):
    
    userId = models.ForeignKey(User, on_delete = models.CASCADE)
    trailId = models.ForeignKey(Trail, on_delete = models.CASCADE)
    
    class Meta:
        verbose_name = ("TrailUser")
        verbose_name_plural = ("TrailUsers")        
        
    def __str__(self):
        return f"User ID: {self.userId} Trail: {self.trailId}"
    
    def get_absolute_url(self):
        return reverse("trail_user_detail", kwargs={"pk": self.pk})