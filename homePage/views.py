from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from .models import Record, createRecords, RecordImage, attachRecords
from .core import convert
from .forms import RecordImageForm


# Create your views here.
def index(request):
    return render(request, 'homePage/index.html')

def images(request):
    if request.method == 'POST':
        form = RecordImageForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save()
            data = {'is_valid': True, 'name': photo.image.name, 'url': photo.image.url}
        else:
            data = {'is_valid': False}
        return JsonResponse(data)
    elif request.method == 'GET':
        photos_list = RecordImage.objects.all()
        return render(request, 'homePage/image.html', {'photos': photos_list})

    return HttpResponse('In images')

def upload(request):
    if request.method == 'POST':
        data_file = handle_uploaded_file(request.FILES['file'], str(request.FILES['file']))
        records = convert(data_file, int(request.POST.get('start_page')), int(request.POST.get('end_page')), settings.MEDIA_ROOT)
        createRecords(records)
        attachRecords()
        return redirect('images')
 
    return HttpResponse("Failed")
 
def handle_uploaded_file(file, filename): 
    with open(settings.MEDIA_ROOT +"/"+ filename, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
    return filename
