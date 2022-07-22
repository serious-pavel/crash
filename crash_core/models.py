from django.db import models
from django.utils import timezone
from base64 import b64encode
from django.db.utils import OperationalError, InterfaceError
from psycopg2 import OperationalError as oe
import time

from django.db import connection


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

    def upload(self, t=0):
        if t > 5:
            raise Exception('Error saving file to the database')
        else:
            try:
                self.save()
            except OperationalError as ex:
                print(f'{ex}')
                time.sleep(5)
                self.upload(t+1)
            except InterfaceError as ex:
                print(f'{ex}. Trying to reconnect')
                connection.connection.close()
                connection.connection = None
                time.sleep(5)
                self.upload(t+1)
            except oe:
                pass
            except KeyboardInterrupt:
                print('Stopped')
                pass



