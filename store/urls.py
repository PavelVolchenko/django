from django.urls import path
from store import views

app_name = 'store'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>', views.index, name='index'),
    path('order/', views.order_list, name='order_list'),
    path('order/<int:days>', views.order_list, name='order_list'),
    path('basket/', views.basket, name='basket'),
    path('order/<int:order_id>/', views.order_detail, name='order_detail'),
    path('about/', views.about, name='about'),
    path('info/', views.info, name='info'),
]
