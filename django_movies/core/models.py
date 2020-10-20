from django.db import models
from django.core.validators import MaxLengthValidator, MinLengthValidator
from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=100)
    rating = models.ImageField(
        null=True, validators=[MaxLengthValidator(10), MinLengthValidator(1)]
    )
    released = models.DateField()
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} from {self.released}"

# Create your models here.
