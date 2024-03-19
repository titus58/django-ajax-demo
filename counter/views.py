from django import forms
from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction
from django.http import HttpResponseBadRequest, HttpResponse, Http404
from django.shortcuts import render
from django.views import generic

from counter.models import Counter


# Create your views here.
class CounterListView(generic.ListView):
    model = Counter
    template_name = "counter/index.html"

def index(request):
    return render(request, "counter/index.html")

class UpdateForm(forms.Form):
    operation = forms.CharField()
    id = forms.IntegerField()

def update(request):
    if request.method != 'POST':
        return HttpResponseBadRequest('invalid method')

    form = UpdateForm(request.POST)
    if not form.is_valid():
        return HttpResponseBadRequest()

    data = form.cleaned_data
    with transaction.atomic():
        try:
            obj = Counter.objects.select_for_update().get(pk=data['id'])
            obj.value += 1 if data['operation'] == 'add' else -1
            obj.save()
            return HttpResponse(str(obj.value))
        except ObjectDoesNotExist:
            raise Http404('not found')
    return HttpResponse("ok")
