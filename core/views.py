from django.shortcuts import render
from django.views import View

# Create your views here.
class HomeView(View):
    def get(self, request):
        return render(request, "home.html")

    def post(self, request):
        context = {
            'resultado': request.POST['nit']
        }
        return render(request, 'resultado.html', context)