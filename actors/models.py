from django.db import models

# Create your models here.

NATIONALITIES_CHOICES = (
    #valor no bd, valor exibido
    ('USA', 'Estados Unidos'),
    ('BRA', 'Brasil'),
)


class Actor(models.Model):
    name = models.CharField(max_length=200, 
                            verbose_name="Nome")
    birthday = models.DateField(blank=True, 
                                null=True,
                                verbose_name="Data de Nascimento")
    nationality = models.CharField(
        max_length=100, 
        choices=NATIONALITIES_CHOICES,
        blank=True,
        null=True,
        verbose_name="Nacionalidade"
        )


    def __str__(self):
        return self.name