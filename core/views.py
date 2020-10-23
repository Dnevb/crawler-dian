from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from json import dumps, loads
import requests

from . import controller

class HomeView(View):
    def get(self, request):
        return render(request, "home.html")

    def post(self, request):
        nit = request.POST['nit']
        context = {
            'rs': requests.post('http://localhost:8000/consultar/', data={'nit': nit}).json()
        }
        return render(request, 'resultado.html', context)


@method_decorator(csrf_exempt, name='dispatch')
class ConsultarView(View):
    def get(self, request):
        body = loads(request.body.decode('utf-8'))
        data = controller.consultar(body['data'])

        return HttpResponse(dumps(data))

    def post(self, request):
        nit = request.POST['nit']
        data = controller.consultar((nit,))
        return HttpResponse(dumps(data))

        