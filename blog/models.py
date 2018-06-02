from django.db import models
from django.utils import timezone

#Post name can be changed but class names should always start with capital 
#letters, no breaks or special characters
class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

# methods need to be declared inside class!
    def publish(self):
        self.published_date = timezone.now()
        self.save()
#sometimes called dunder: dounble-underscore
    def __str__(self):
        return self.title