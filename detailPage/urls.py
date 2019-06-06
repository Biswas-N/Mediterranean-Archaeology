from django.urls import path
from . import views

urlpatterns = [
    path('<int:record_id>', views.index, name='detail')
]