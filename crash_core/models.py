from django.db import models
from django.utils import timezone

# Create your models here.


class Frame(models.Model):
    file_name = models.CharField(max_length=20, blank=False, unique=False)
    file_bin = models.BinaryField(editable=True)
    update_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "{1} - {0}".format(self.file_name, self.update_date)
