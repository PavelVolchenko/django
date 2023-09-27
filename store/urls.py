from django.urls import path
from .views import index, about, info, HelloView, year_post, MonthPost, post_detail

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('info/', info, name='info'),
    path('hello/', HelloView.as_view(), name='hello'),
    path('post/<int:year>/', year_post, name='year_post'),
    path('post/<int:year>/<int:month>/', MonthPost.as_view(), name='month_post'),
    path('post/<int:year>/<int:month>/<slug:slug>/', post_detail, name='post_detail'),
]