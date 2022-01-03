from django.db import models
from django.core import validators

POSITION = (('リーダー','0'), ('サブリーダー', '1',), ('長老', '2',), ('メンバー', '3')) #役職の選択肢

# Create your models here.
class ClanuserModel(models.Model):
  username = models.CharField(max_length=50)
  maxtrophy = models.IntegerField()
  position = models.CharField(
    max_length = 50,
    choices = POSITION)

  def __str__(self):
    return self.username