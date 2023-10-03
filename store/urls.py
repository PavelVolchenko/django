from django.urls import path
# from .views import index, about, info, HelloView, year_post, MonthPost, post_detail
from store import views

app_name = 'store'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('info/', views.info, name='info'),
    path('<int:id>/', views.add_to_cart, name='add_to_cart'),
    path('order/<int:id>/', views.order_detail, name='order_detail'),
    path('order/', views.order_list, name='order_list'),
    path('basket/', views.basket, name='basket'),


    path('hello/', views.HelloView.as_view(), name='hello'),
    path('post/<int:year>/', views.year_post, name='year_post'),
    path('post/<int:year>/<int:month>/', views.MonthPost.as_view(), name='month_post'),
    path('post/<int:year>/<int:month>/<slug:slug>/', views.post_detail, name='post_detail'),
]