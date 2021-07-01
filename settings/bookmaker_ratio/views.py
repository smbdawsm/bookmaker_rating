from django.shortcuts import render
from django.views import View
from .models import Bookmaker

class MainView(View):

    def get(self, request):
        bookmakers = Bookmaker.objects.all()
        return render(
            request, 
            'bookmaker_ratio/mainpage.html', 
            {
                "bookmakers": bookmakers
            })