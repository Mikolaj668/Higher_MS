from django.core.exceptions import MultipleObjectsReturned
from django.db.models import Avg
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from .models import *

from django.http import JsonResponse

from .forms import AddMarkForm


# Create your views here.

class AddMarkView(View):
    def get(self, request):
        form = AddMarkForm()
        return render(request, 'rate_task_by_rec.html', {'form': form})

    def post(self, request):
        form = AddMarkForm(request.POST)

        if form.is_valid():
            try:
                Grade.objects.get_or_create(**form.cleaned_data)
                return HttpResponse('Jest partially OK')
            except MultipleObjectsReturned as error:
                return HttpResponse(error)
        return HttpResponse('Invalid form')


class JOutputView(View):

    def get(self, request):
        otp = []
        for candidate in Candidate.objects.all():
            otp.append({'data': [{
                'pk': candidate.pk,
                'full_name': str(candidate),
                'avg_grades': round(candidate.grade_set.aggregate(Avg('value'))['value__avg'], 2),
                'grades': list(candidate.grade_set.values_list('value', flat=True)),
            }]})

        return JsonResponse(otp, safe=False)
