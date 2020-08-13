from django.db import models
from django.urls import reverse
from .user import User

class Friend(models.Model):
    
    sender = models.ForeignKey(User, related_name="sender", on_delete = models.CASCADE)
    receiver = models.ForeignKey(User, related_name="receiver", on_delete = models.CASCADE)
    requestPending = models.BooleanField(null=False, default=0)
    requestAccepted = models.BooleanField(null=False, default=0)

    class Meta:
        verbose_name = ("Friend")
        verbose_name_plural = ("Friends")        
        
    def __str__(self):
        return f"Sender ID: {self.sender} Receiver ID: {self.receiver}"
    
    def get_absolute_url(self):
        return reverse("friend_detail", kwargs={"pk": self.pk})