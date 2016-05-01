from django.db import models


class CodeUrls(models.Model):
    """
    Model to store code, language mapped with url hash
    """
    code = models.TextField()
    lang = models.CharField(max_length=16)
    url = models.CharField(unique=True, max_length=16, null=True, blank=True)
