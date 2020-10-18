from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Video(models.Model):
    
    video_url = models.CharField(max_length=1000, null=True)
    
    class Meta:
        verbose_name = ("Video")
        verbose_name_plural = ("Videos")        
        
    def __str__(self):
        return f"Video ID: {self.pk}"
    
    def get_absolute_url(self):
        return reverse("video_detail", kwargs={"pk": self.pk})