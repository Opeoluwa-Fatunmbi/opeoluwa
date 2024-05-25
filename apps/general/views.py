from django.shortcuts import redirect, render
from django.views import View


import sweetify

# Create your views here.


class AboutView(View):
    def get(self, request):
        return render(request, "general/about.html")


class ContactView(View):
    def get(self, request):
        return render(request, "general/contact.html")

    def post(self, request):
        return render(request, "general/contact.html")
