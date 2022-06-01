from django.urls import path
from .views import CategoryView, HomeView, register_request, login_request



urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('category/<str:cats>/', CategoryView.as_view(), name='category'),
    path('register', register_request, name='register'),
    path('login', login_request, name='login')

]