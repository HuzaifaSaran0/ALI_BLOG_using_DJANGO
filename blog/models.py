from django.db import models


class Contact(models.Model):
    cid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=14)
    email = models.CharField(max_length=100)
    content = models.TextField()
    time_stamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.name
