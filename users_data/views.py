#-*- coding: utf-8 -*-
from django.shortcuts import render
from django.views import View

from users_data.forms import UserDataForm
from users_data.models import UserData


class CreateView(View):

    def get(self, request):
        """
        Shows a form
        :param request: HttpRequest
        :return: HttpResponse
        """
        form = UserDataForm()
        context = {
            'form': form,
            'success_message': 'OK'
        }
        return render(request, 'users_data/new_user_data.html', context)

    def post(self, request):
        """
        Crea una foto en la base a la información POST
        :param request: HttpRequest
        :return: HttpResponse
        """
        success_message = ''
        user_data = UserData()
        form = UserDataForm(request.POST, instance=user_data)
        if form.is_valid():
            new_user_data = form.save()  # saves the object and gives back
            form = UserDataForm()
            success_message = '¡Se han guardados los datos con éxito!'
            # la función format guarda los argumentos por orden en los números entre llaves
            # success_message += '<a href="{0}">'.format(reverse('photo_detail', args=[new_photo.pk]))
            # success_message += 'Ver foto'
            # success_message += '</a>'
            context = {
                'form': form,
                'success_message': success_message
            }
            return render(request, 'users_data/thanks.html', context)
        else:
            context = {
                'form': form,
                'errors': form._errors
            }
            return render(request, 'users_data/new_user_data.html', context)


class ThanksView(View):

    def get(self, request):
        """
        Gets the thanks view
        :return:
        """
        success_message = '¡Se han guardados los datos con éxito!'
        context = {
            'success_message': success_message
        }
        return render(request, 'users_data/thanks.html', context)