from django.db import models


# 建立database的模版
class Job(models.Model):
    image = models.ImageField(upload_to='')
