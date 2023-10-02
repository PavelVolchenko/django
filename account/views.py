from django.shortcuts import render
from django.contrib.auth import login, logout
from django.core.files.storage import FileSystemStorage
import logging
import account.views
from .forms import RegistrationForm, LoginForm, ManyFieldsForm, ManyFieldsFormWidget, ImageForm
from store.models import User

logger = logging.getLogger(__name__)


def login_form(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        message = "Error input data"
        if form.is_valid():
            username = form.cleaned_data["name"].lower()
            password = form.cleaned_data["password"]
            # Совершаем операции с данными
            logger.info(f"Try login: {username=}, {password=}.")
            user = User.objects.filter(username=username).first()
            if not user or password != user.password:
                logger.info(f"Login failed")
                form = LoginForm()
                message = "Password or username is incorrect"
            else:
                logger.info(f"Login successful")
                login(request, user)
                message = f"Welcome, {user.username}"
    else:
        form = LoginForm()
        message = "Login please"
    return render(request, "account/login.html", {"form": form, "message": message})


def logout_user(request):
    logout(request)
    return render(request, "account/logout.html")


def registration_form(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        message = "Error input data"
        if form.is_valid():
            username = form.cleaned_data["name"].lower()
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            if password != form.cleaned_data["password_repeat"]:
                form = RegistrationForm()
                message = "Passwords don't match"
            else:
                # Совершаем операции с данными
                logger.info(f"Registration new user: {username=}, {email=}, {password=}.")
                user = User(username=username, email=email, password=password)
                user.save()
                login(request, user)
                message = "User registration success"
    else:
        form = RegistrationForm()
        message = "Registration of a new user"
    return render(request, "account/registration.html", {"form": form, "message": message})


def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data["image"]
            fs = FileSystemStorage()
            fs.save(image.name, image)
    else:
        form = ImageForm()
    return render(request, "account/upload_image.html", {"form": form})


def many_fields_form(request):
    if request.method == 'POST':
        form = ManyFieldsFormWidget(request.POST)
        if form.is_valid():
            # Совершаем операции с данными
            logger.info(f"Take {form.cleaned_data=}.")
    else:
        form = ManyFieldsFormWidget()
    return render(request, "account/many_fields_form.html", {"form": form})
