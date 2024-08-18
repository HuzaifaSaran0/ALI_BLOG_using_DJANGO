from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=50)
    intro = models.TextField(help_text="Short introduction or overview", null=True, blank=True)
    content = models.TextField(help_text="Main content of the article", null=True, blank=True)
    image1 = models.ImageField(upload_to='static/', null=True, blank=True, help_text="Main image")
    section1_title = models.CharField(max_length=255, blank=True, null=True, help_text="Title for section 1")
    section1_content = models.TextField(blank=True, null=True, help_text="Content for section 1")
    image2 = models.ImageField(upload_to='static/', null=True, blank=True, help_text="Image for section 1")
    section2_title = models.CharField(max_length=255, blank=True, null=True, help_text="Title for section 2")
    section2_content = models.TextField(blank=True, null=True, help_text="Content for section 2")
    image3 = models.ImageField(upload_to='static/', null=True, blank=True, help_text="Image for section 2")
    slug = models.SlugField(unique=True, max_length=150, null=True, blank=True)
    time_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class PostComment(models.Model):
    postSno = models.AutoField(primary_key=True)
    comment = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # image = models.ImageField(upload_to='images/', null=True, blank=True)  # Add this line
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    time_stamp = models.DateTimeField(blank=True, default=now)

    def __str__(self):
        return self.comment[0:13] + "..." + " by " + self.user.username