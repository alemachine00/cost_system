from django.urls import path
from . import views

urlpatterns = [
    path('order/', views.order, name='order'),
    path('<int:id>/', views.order_detail, name='detail'),
    path('', views.home, name='home'),
]
