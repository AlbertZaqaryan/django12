from django.urls import path
from .views import CategoryView, HomeView, register_request, login_request, PaypalReturnView, PaypalCancelView, PaypalFormView, CategoryDetail, logout_request, AddPostListView



urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('category/<str:cats>/', CategoryView.as_view(), name='category'),
    path('category/<int:id>', CategoryDetail.as_view(), name='category_detail'),
    path('register', register_request, name='register'),
    path('login', login_request, name='login'),
    path('logout', logout_request, name = 'logout'),
    path('add_post', AddPostListView.as_view(), name='add_post'),
    path('paypal/<int:id>', PaypalFormView.as_view(), name='paypal'),
    path('paypal-return/', PaypalReturnView.as_view(), name='paypal-return'),
    path('paypal-cancel/', PaypalCancelView.as_view(), name='paypal-cancel'),

]