from django.db import models

# Create your models here.
class TournamentArticleModel(models.Model):
  title = models.CharField(max_length=50)
  context = models.TextField()
  participants_num = models.IntegerField()
  date = models.DateField(null=True)
  hold_flag = models.BooleanField(default=False) #開催されたかどうか、されたならTrue