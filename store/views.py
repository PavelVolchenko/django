import logging
from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

logger = logging.getLogger(__name__)


def index(request):
    logger.info('Index page accessed')
    product_list = Product.objects.all()
    return render(request, 'index.html', {"product_list": product_list})


def about(request):
    logger.debug('About page accessed')
    return render(request, 'about.html')

def info(request):
    logger.debug('Info page accessed')
    return render(request, 'info.html')

