from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/blog_images/user_name/filename
    return 'blog_images/{0}/{1}'.format(instance.user.id, filename)

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=user_directory_path, blank=True)
    caption = models.CharField(max_length=100)
    date_published = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.caption}'
