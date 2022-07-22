from django.db import models
from django.utils import timezone
from base64 import b64encode

# Create your models here.


class Frame(models.Model):
    file_name = models.CharField(max_length=20, blank=False, unique=False)
    file_bin = models.BinaryField(editable=True)
    update_date = models.DateTimeField(default=timezone.now)

    get_latest_by = "-update_date"

    @property
    def img(self):
        return b64encode(self.file_bin).decode()

    def __str__(self):
        return "{1} - {0}".format(self.file_name, self.update_date)
