from django.db import models
from django.conf import settings

class Post(models.Model):
    title = models.CharField(max_length=120)
    location = models.CharField(max_length=120, blank=True)
    travel_date = models.DateField(null=True, blank=True)
    story = models.TextField()

    # IMPORTANT: Photo field
    photo = models.ImageField(upload_to='posts/', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='travel_posts'
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

