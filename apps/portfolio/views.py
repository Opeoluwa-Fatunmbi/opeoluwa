from django.shortcuts import render
from django.views import View
# from apps.portfolio.models import Project


# Create your views here.

class Nexestate(View):
    def get(self, request):
        return render(request, "portfolio/nexestate.html")

class HomeView(View):
    def get(self, request):
        return render(request, "portfolio/home.html")
