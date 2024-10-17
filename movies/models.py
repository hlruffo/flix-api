from django.db import models
from genres.models import Genre
from actors.models import Actor

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=500, verbose_name="Título")
    genre = models.ForeignKey(Genre,
                        verbose_name="Gênero", 
                        related_name="movies",
                        on_delete=models.PROTECT)
    release_date = models.DateField(blank=True, 
                                    null=True, 
                                    verbose_name="Data de Lançamento")
    actors = models.ManyToManyField(Actor, 
                                    related_name='movies',
                                    verbose_name="Atores")
    resume = models.TextField(blank=True, 
                              null=True,
                              verbose_name="Resumo")
    
    def __str__(self):
        return self.title