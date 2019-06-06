from django.shortcuts import render
from homePage.models import Record
# Create your views here.
def index(req, record_id):
    record = Record.objects.get(vase_num = record_id)
    return render(req, 'detailPage/details.html', {'record': record})