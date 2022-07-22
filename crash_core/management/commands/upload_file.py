from django.core.management.base import BaseCommand
from ...models import Frame
import os


class Command(BaseCommand):
    help = 'upload files to database'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, default=1)

    def handle(self, *args, **options):

        count = options['count']
        # print(count)
        if 1 <= count < 10:
            folder = 'CrashBest01'
        elif 10 <= count < 50:
            folder = 'CrashBest10'
        else:
            folder = 'CrashBest50'

        base_folder = f'test/{folder}'
        files = os.listdir(base_folder)

        for i in range(1, count+1):
            if files:
                name = files[0]
                old = f'{base_folder}/{name}'
                new = f'test/Uploaded/{name}'
                if os.path.exists(old) and os.path.isfile(old):
                    with open(old, 'rb') as bin_data:
                        frame = Frame(file_name=name, file_bin=bin_data.read())

                        frame.upload()
                        print(f'File {name} uploaded at {frame.update_date}')
                    os.replace(old, new)
                files.remove(name)

            else:
                print(f'No more files in {folder}')
                break



