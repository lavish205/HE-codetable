from django.db import models
from Crypto.Hash import MD5
# Create your models here.


class CodeUrls(models.Model):
    code = models.TextField()
    lang = models.CharField(max_length=16)
    url = models.CharField(unique=True, max_length=16, null=True, blank=True)

    # def save(self, force_insert=False, force_update=False, using=None,
    #          update_fields=None):
    #     self.url = str(int(MD5.new(self.pk).hexdigest(), 16) % (10 ** 8))
    #     super(CodeUrls, self).save()
