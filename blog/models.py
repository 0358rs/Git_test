from django.db import models


class Blog(models.Model):
    # id = 1, 2, 3, 4
    event_title = models.CharField(max_length=32)
    content = models.CharField(max_length=140)
    posted_date = models.DateTimeField(auto_now_add=True)


class Connpass_Api(models.Model):
    cn_results_returned = models.PositiveSmallIntegerField()
    cn_results_available = models.PositiveSmallIntegerField()
    cn_results_start = models.PositiveSmallIntegerField()
    cn_event_id = models.PositiveIntegerField()
    cn_title = models.CharField(max_length=150)
    cn_catch = models.CharField(max_length=150)
    cn_description = models.CharField(max_length=200)
    cn_event_url = models.URLField()
