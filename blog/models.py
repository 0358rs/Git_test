from django.db import models

class Blog(models.Model):

    #id = 1, 2, 3, 4
    event_title = models.CharField(max_length=32)
    content = models.CharField(max_length=140)
    posted_date = models.DateTimeField(auto_now_add=True)