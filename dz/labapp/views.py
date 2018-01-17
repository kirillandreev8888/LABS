from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import ListView
from django import forms
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import  *
from . import models

from django.views.generic import DetailView
from datetime import datetime, date, time


class UserList(LoginRequiredMixin, ListView):
    login_url = '/labs/'
    redirect_field_name = 'redirect_to'
    model = Userus
    template_name = 'user_list.html'

class FilmList(LoginRequiredMixin, ListView):
    login_url = '/labs/'
    redirect_field_name = 'redirect_to'
    model = Film
    template_name = 'film_list.html'

    paginate_by = 4



class ReviewList(LoginRequiredMixin, ListView):
    login_url = '/labs/'
    redirect_field_name = 'redirect_to'
    model = Review
    template_name = 'review_list.html'

def registration_dumb(request):
    errors = {}
    request.encoding = 'utf-8'
    if request.method == 'POST':
        username = request.POST.get('username')
        if not username:
            errors['uname']='Введите логин'
        elif len(username) < 5:
            errors['uname']='Длина логина должна быть не меньше 5 символов'

        if User.objects.filter(username=username).exists():
            errors['uname']='Такой логин уже занят'

        password = request.POST.get('password')
        if not password:
            errors['psw']='Введите пароль'
        elif len(password) < 8:
            errors['psw']='Длина пароля должна быть не меньше 8 символов'

        password_repeat = request.POST.get('password2')
        if password != password_repeat:
            errors['psw2']='Пароли должны совпадать'

        email = request.POST.get('email')
        if not email:
            errors['email']='Введите email'

        last_name = request.POST.get('last_name')
        if not last_name:
            errors['lname']='Введите фамилию'

        first_name = request.POST.get('first_name')
        if not first_name:
            errors['fname']='Введите имя'

        if not errors:
            user = User.objects.create_user(username, email, password)
            usr = Userus()
            usr.user = user
            usr.first_name = first_name
            usr.last_name = last_name
            usr.save()
            return HttpResponseRedirect('/labs/users')
        else:
            context = {'errors':errors, 'username':username, 'email': email, 'last_name': last_name, 'first_name': first_name}
            return render(request, 'registration_dumb.html',context)

    return render(request, 'registration_dumb.html',{'errors':errors})

class RegistrationForm(forms.Form):
    username = forms.CharField(min_length=5,label='Логин')
    password = forms.CharField(min_length=8,widget=forms.PasswordInput, label='Пароль')
    password2 = forms.CharField(min_length=8, widget=forms.PasswordInput, label='Повторите ввод')
    email = forms.EmailField(label='Email')
    last_name = forms.CharField(label='Фамилия')
    first_name = forms.CharField(label='Имя')

def registration_user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        is_val = form.is_valid()
        data = form.cleaned_data
        if data['password']!=data['password2']:
            is_val = False
            form.add_error('password2',['Пароли должны совпадать'])
        if User.objects.filter(username=data['username']).exists():
            form.add_error('username',['Такой логин уже занят'])
            is_val = False

        if is_val:
            data = form.cleaned_data
            user = User.objects.create_user(data['username'], data['email'], data['password'])
            usr = Userus()
            usr.user = user
            usr.first_name = data['first_name']
            usr.last_name = data['last_name']
            usr.nickname = data['username']
            usr.save()
            return HttpResponseRedirect('/labs/authorization')
    else:
        form = RegistrationForm()

    return render(request, 'registration_user.html',{'form':form})

@login_required(login_url='/labs/authorization')
def success_authorization(request):
    return HttpResponseRedirect('/labs')


def success_authorization_dumb(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/labs/')
    else:
        return HttpResponseRedirect('/labs/authorization')


def authorization(request):
    errors = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        if not username:
            errors['uname']='Введите логин'
        elif len(username) < 5:
            errors['uname']='Длина логина должна быть не меньше 5 символов'

        password = request.POST.get('password')
        if not password:
            errors['psw']='Введите пароль'
        elif len(password) < 8:
            errors['psw']='Длина пароля должна быть не меньше 8 символов'

        user = authenticate(request, username=username, password=password)
        if user is None and 'uname' not in errors.keys() and 'psw' not in errors.keys():
            errors['login'] = 'Логин или пароль введены неправильно'

        if not errors:
            login(request,user)
            #return HttpResponseRedirect('/labs/success_authorization_dumb')
            return HttpResponseRedirect('/labs/success_authorization')
        else:
            context = {'errors':errors}
            return render(request, 'authorization.html',context)

    return render(request, 'authorization.html',{'errors':errors})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/labs/')

class AutorizationForm(forms.Form):
    pass

def index(request):
    return render(request, 'index.html')

def index2(request):
    return HttpResponseRedirect('/labs/')

class FilmAddForm(forms.ModelForm):
    name = forms.CharField(min_length=5,label='Название')
    genre = forms.CharField(label='Жанр')
    description = forms.CharField(label='Описание')
    img = forms.FileField(label='Изображение', required=False)

    class Meta:
        model=models.Film
        fields = ('name', 'genre', 'description', 'img')


def add_film(request):
    if request.method == 'POST':
        form = FilmAddForm(request.POST, request.FILES)
        is_val = form.is_valid()
        data = form.cleaned_data
        if Film.objects.filter(name=data['name']).exists():
            form.add_error('name',['Этот фильм уже есть в базе'])
            is_val = False

        if is_val:
            data = form.cleaned_data
            # flm = Film()
            # flm.name = data['name']
            # flm.genre = data['genre']
            # flm.description = data['description']
            # flm.img = request.FILES['img']
            # flm.save()
            # flm = form.save(commit=False)
            # flm.save()
            form.save()
            return HttpResponseRedirect('/labs/films')
    else:
        form = FilmAddForm()

    return render(request, 'add_film.html',{'form':form})

class film_view(DetailView):
    model = Film
    context_object_name = 'film'
    template_name = 'film_view.html'

    def get_context_data(self, **kwargs):
        context = super(film_view, self).get_context_data(**kwargs)
        context['review'] = Review.objects.all()
        context['userus'] = Userus.objects.all()
        # print(context)
        return context

# def add_review(request, film_id):
#     if request.method == "POST":
#         film = Film.objects.get(id=film_id)
CHOICES=[('0','Очень плохо'),('1','Плохо'),('2','Так себе'),('3','Неплохо'),('4','Хорошо'),('5','Отлично!')]
class ReviewAddForm(forms.Form):
    rating = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), label='Ваш рейтинг фильма')
    review_content = forms.CharField(label='Текст отзыва')
    
def add_review(request, film_id):
    if request.method == "POST":
        form = ReviewAddForm(request.POST)
        is_val = form.is_valid()
        data = form.cleaned_data
        if is_val:
            data = form.cleaned_data
            rev = Review()
            rev.rating = data['rating']
            rev.review_content = data['review_content']
            rev.film_id = film_id
            rev.user_id = request.user.id
            rev.review_date=datetime.now().date()
            rev.save()
        return HttpResponseRedirect('/labs/film/'+film_id)
    else:
        form = ReviewAddForm()

    return render(request, 'add_review.html',{'form':form})



