from django.db import models
import datetime
import random
import string

# Create your models here.


def create_dynamic_path(instance, filename):
    (name, ext) = filename.split(".")
    name += ''.join([random.choice(string.ascii_letters)
                    for _ in range(0, 15)])
    date = datetime.datetime.now().strftime(f"%Y-%m-%d/{f'{name}.{ext}'}")
    return date


class Citizen(models.Model):
    Image = models.ImageField(
        upload_to=create_dynamic_path, null=False, blank=False)
    CreatedAt = models.DateTimeField(auto_now_add=True)
    UserId = models.IntegerField(null=True)

    def Json(self):
        return {'id': self.id, 'image': self.Image.url, 'user_id': self.UserId}
