from django.urls import path
from .views import CategoryListView, CategoryDetailView

urlpatterns = [
    path('', CategoryListView.as_view(), name='home'),
    path('Category/<int:category_id>',CategoryDetailView.as_view(), name='home_detail')


]