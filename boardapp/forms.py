from django import forms

class SortForm(forms.Form):
  CHOICES = (('normal', 'ソート順選択'), ('maxtrophy', '最高トロ'),('position', '役職'))

  choice = forms.fields.ChoiceField(
    choices = CHOICES,
    required = True,
    label = 'ソート順'
  )