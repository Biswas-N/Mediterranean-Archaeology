from django.shortcuts import render
from django.http import HttpResponse
from homePage.models import Record

# Create your views here.
def index(req):
    records = Record.objects.order_by('vase_num')
    return render(req, 'listPage/index.html', {'records': records})