from django.db import models


# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    director = models.ForeignKey(Person, null=True,
                                 on_delete=models.SET_NULL,
                                 related_name='movies_directed')
    starring = models.ManyToManyField(Person, through='StarringPersons',
                                      related_name='movies_starr')
    year = models.IntegerField(null=True)

    def __str__(self):
        return self.title


class StarringPersons(models.Model):
    person = models.ForeignKey(Person, null=True, on_delete=models.SET_NULL)
    movie = models.ForeignKey(Movie, null=True, on_delete=models.SET_NULL)
    role = models.CharField(max_length=128, null=True)