from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
import datetime
from django.views.generic import ListView
from polls.models import  films

# def pvariable(request):
#
#     return render(request, 'variable.html', {'myvariable': datetime.datetime.now()})
# # Create your views here.
# def home(request):
#     return render(request, 'nav.html')
#
# class OrdersView(View):
#     def get(self, request):
#         data = {
#             'orders': [
#                 {'title': 'Заказ №1', 'id': 1},
#                 {'title': 'Заказ №2', 'id': 2},
#                 {'title': 'Заказ №3', 'id': 3}
#             ]
#         }
#         return render(request, 'nav.html', data)
#
#
# class OrderView(View):
#     def get(self, request, id):
#         data = {
#             'order': {
#                 'id': id
#             }
#         }
#         return render(request, 'order.html', data)

# def home(request):
#     par = {
#         'header': 'Home'
#     }
#     return render(request, 'home.html', context=par)


class filmsView(ListView):
    model = films
    template_name = 'lab5.html'
    # context_object_name = 'films_list'



