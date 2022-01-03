from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from .models import ClanuserModel
from .forms import SortForm
from django.views.generic import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy

def signupfunc(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    try:
      user = User.objects.create_user(username, '', password)
      return render(request, 'boardapp/signup.html', {})
    except IntegrityError:
      return render(request, 'boardapp/signup.html', {'warning_message': '既にそのユーザ名は使われています'})
  return render(request, 'boardapp/signup.html', {})

def loginfunc(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
      login(request, user)
      return redirect('main') #メイン画面へ遷移
    else:
      return render(request, 'boardapp/login.html', {'message': 'ユーザ名もしくはパスワードが間違っています'}) #ログイン画面にとどまる
  return render(request, 'boardapp/login.html', {})

def mainfunc(request):
  object_list = ClanuserModel.objects.all()
  if request.method == 'POST': #ソートが実行された場合
    sort_method = request.POST['choice']
    if sort_method != 'normal':
      object_list = ClanuserModel.objects.order_by(sort_method).reverse()
    return render(request, 'boardapp/main.html', {'object_list':object_list, 'form': SortForm()})
  else:
    return render(request, 'boardapp/main.html', {'object_list':object_list, 'form': SortForm()})

def logoutfunc(request):
  logout(request)
  return redirect('main')

class ClanuserCreate(CreateView):
  template_name = 'boardapp/createclanuser.html'
  model = ClanuserModel
  fields = ('username', 'maxtrophy', 'position')
  success_url = reverse_lazy('main')

class ClanuserDelete(DeleteView):
  template_name = 'boardapp/deleteclanuser.html'
  model = ClanuserModel
  success_url = reverse_lazy('main')

class ClanuserUpdate(UpdateView):
  template_name = 'boardapp/updateclanuser.html'
  model = ClanuserModel
  fields = ('username', 'maxtrophy', 'position')
  success_url = reverse_lazy('main')