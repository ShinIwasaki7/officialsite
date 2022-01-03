from django.shortcuts import render
import datetime

# Create your views here.
def clanbattlemain(request):
    # JSTとUTCの差分
  DIFF_JST_FROM_UTC = 9
  now = datetime.datetime.utcnow() + datetime.timedelta(hours=DIFF_JST_FROM_UTC)
  year, month, day = now.year, now.month, now.day
  return render(request, 'clanbattleapp/battlemain.html', {'year': year, 'month': month, 'day': day})