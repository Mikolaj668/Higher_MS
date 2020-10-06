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
            cnd_task = form.cleaned_data['task']
            cnd = form.cleaned_data['candidate']
            cnd_grd = Grade.objects.filter(candidate=cnd)

            try:
                for gr_obj in cnd_grd:
                    if gr_obj.task == cnd_task:
                        return HttpResponse('Task already graded.')
                Grade.objects.get_or_create(**form.cleaned_data)
                return HttpResponse('Task successfully graded.')
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
