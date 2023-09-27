from django.urls import path
from . import views
from .views import PitchDeckView, PitchDeckListView

urlpatterns = [
    path('', PitchDeckView.as_view(), name='pitchdeck'),
    path('pitches/', PitchDeckListView.as_view(), name='pitches'),
]