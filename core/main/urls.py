from django.urls import path
from .views import CategoryView, HomeView



urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('category/<str:cats>/', CategoryView, name='category')

]