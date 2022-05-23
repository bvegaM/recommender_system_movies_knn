from django.db import models

# Create your models here.
class Rating(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField(default=0)
    movie_id = models.IntegerField(default=0)
    rating = models.FloatField(default=0.0)

    def __str__(self):
        return str(self.id)
