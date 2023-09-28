from django.urls import path
# from .views import login_form, many_fields_form, registration_form, upload_image, logout_user
from . import views

urlpatterns = [
    path('registration/', views.registration_form, name='registration'),
    path('login/', views.login_form, name='login_form'),
    path('logout/', views.logout_user, name='logout_user'),
    path("upload/", views.upload_image, name="upload_image"),
    path('forms/', views.many_fields_form, name='many_fields_form'),
]
