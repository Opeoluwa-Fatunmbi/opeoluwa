from django.shortcuts import render
from django.views import View
from apps.portfolio.models import Portfolio


# Create your views here.
class HomeView(View):
    def get(self, request):
        portfolio = Portfolio.objects.all()
        context = {
            "portfolio": portfolio,
        }
        return render(request, "portfolio/index.html", context)
