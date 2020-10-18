from django.db import models
from django.urls import reverse
from .user import User

class Trail(models.Model):
    
    trail_name = models.CharField(null = False, max_length = 20) 
    # For now the trail_img field will store an image address, will modify later
    trail_img = models.CharField(null = False, max_length = 2000)
    description = models.CharField(null = False, max_length = 500)
    address = models.CharField(null = False, max_length = 100)
    zipcode = models.CharField(null = False, max_length = 10)
    creator = models.ForeignKey(User, on_delete = models.CASCADE)
    
    class Meta:
        verbose_name = ("Trail")
        verbose_name_plural = ("Trails")        
        
    def __str__(self):
        return f"Trail Name: {self.trail_name}"
    
    def get_absolute_url(self):
        return reverse("trail_detail", kwargs={"pk": self.pk})