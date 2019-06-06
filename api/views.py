from rest_framework import viewsets
from homePage.models import Record, RecordImage
from .serializers import RecordSerializer, RecordImageSerializer


class RecordViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Record.objects.all().order_by('vase_num')
    serializer_class = RecordSerializer

class RecordImageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = RecordImage.objects.all().order_by('record_id')
    serializer_class = RecordImageSerializer