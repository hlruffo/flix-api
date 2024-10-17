from django.db import models

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=255,
                            verbose_name="Nome")

    def __str__(self):
        return self.name