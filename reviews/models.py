from django.db import models
from movies.models import Movie
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Review(models.Model):
    movie = models.ForeignKey(Movie,
                              verbose_name="Filme", 
                              related_name="reviews",
                              on_delete=models.PROTECT)
    comments = models.TextField(
        verbose_name="Comentários",
        blank=True,
        null=True
    )
    stars = models.IntegerField(
        validators=[
            MinValueValidator(0, "O mínimo de estrelas é 0"),
            MaxValueValidator(5, "O máximo de estrelas é 5"),
        ],
        verbose_name="Estrelas",
    )

    def __str__(self):
        return self.movie