from homePage.models import Record, RecordImage
from rest_framework import serializers


class RecordSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Record
        fields = (
            'vase_num',
            'fabric',
            'technique',
            'shape_name',
            'provenance',
            'date_range',
            'collection',
            'scholor_name',
            'publication',
            'images',
        )

class RecordImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RecordImage
        fields = (
            'record_id',
            'image',
        )