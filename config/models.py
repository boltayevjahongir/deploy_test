from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    file = models.FileField(upload_to='files/', blank=True, null=True)
    def __str__(self):
        return self.title