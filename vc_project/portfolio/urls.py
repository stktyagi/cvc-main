from django.urls import path
from . import views
from .views import PortfolioListView, AddPorfolioItemView, EditPortfolioItemView, DeletePortfolioItemView

urlpatterns = [
    path('', PortfolioListView.as_view(), name='portfolio'),
    path('add_portfolio_item/', AddPorfolioItemView.as_view(), name='add_portfolio_item'),
    path('<int:pk>/edit/', EditPortfolioItemView.as_view(), name='edit_portfolio'),
    path('delete/<int:pk>', DeletePortfolioItemView.as_view(), name='delete_portfolio'),
]