from django.db import models
from django.conf import settings
import re
import os

# Create your models here.
class Record(models.Model):
    vase_num = models.IntegerField(primary_key=True, unique=True, default=-1)
    fabric = models.CharField(max_length=100, default='South Italian')
    technique = models.CharField(max_length=100, default='Red-Figure')
    shape_name = models.CharField(max_length=100, default='NULL')
    provenance = models.CharField(max_length=100, default='NULL')
    date_range = models.CharField(max_length=100, default='450-300 BC')
    collection = models.CharField(max_length=100, default='NULL')
    scholor_name = models.CharField(max_length=100, default='A.D.Trendall')
    publication = models.CharField(max_length=100, default='The Red Figure Vases of Paestum, Rome 1987')
    image_count = models.IntegerField(null=True)

    
class RecordImage(models.Model):
    image = models.ImageField(upload_to= settings.MEDIA_ROOT + '/images', blank=True, null=True)
    record = models.ForeignKey(Record, on_delete = models.PROTECT,null=True, related_name='images')


def createRecords(records):
    for k,v in records.items():
        temp_record = Record(
            vase_num = k,
            fabric = checkSize(v.fabric),
            technique = checkSize(v.technique),
            shape_name = checkSize(v.shape_name),
            provenance = checkSize(v.provenance),
            date_range = checkSize(v.date_range),
            collection = checkSize(v.collection),
            scholor_name = checkSize(v.scholor_name),
            publication = checkSize(v.publication),
            image_count = 0
        )

        temp_record.save()


def attachRecords():
    pics = os.path.join(settings.MEDIA_ROOT, 'images')
    for img in os.listdir(pics):
           regex = 'P-(.[0-9]?)-?.*'
           f = re.findall(regex, img)
           for l in f:
               if Record.objects.filter(vase_num=int(l)).exists():
                   src = os.path.join(settings.MEDIA_ROOT, 'images', img)
                   r = Record.objects.get(vase_num=int(l))
                   temp_record_image = RecordImage(
                   image=src,
                   record=r
                   )
                   print("Saved {}", img)
                   temp_record_image.save()



def checkSize(data):
    if len(data) >= 100:
        if 'fro' in data:
            d = data.split(',')
            return d[0]
        else:
            d = data.split('Ht')
            return d[0]

    return data 