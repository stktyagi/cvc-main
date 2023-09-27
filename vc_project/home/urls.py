from django.urls import path
from . import views
from .views import Index, EditHomePageView

urlpatterns = [
    path('', Index.as_view(), name='home'),
]