from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=32)
    description = models.TextField()

    def no_of_ratings(self):
        ratings  = Rating.objects.filter(movie=self)
        return len(ratings)

    def avg_ratings(self):
        sum=0
        ratings = Rating.objects.filter(movie=self)
        for rating in ratings:
            sum += rating.stars

        if len(ratings) > 0 :
            return sum / len(ratings)
        else :
            return 0


class Rating(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])

    def save(self, *args, **kwargs):
        if int(self.stars) <= 5 and int(self.stars) >=1 :
            super().save(*args,**kwargs)

    class Meta:
        unique_together = (('user','movie'),)
        #index_together = (('user', 'movie'),)


