from django.shortcuts import render
from django.views import View
from .models import *

# Create your views here.

class AddMarkView(View):
    def get(self, request):

        return render(request, )