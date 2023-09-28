import logging
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View
from .models import Product

logger = logging.getLogger(__name__)

class HelloView(View):
    def get(self, request):
        return HttpResponse("Hello from class!")

class MonthPost(View):
    def get(self, request, year, month):
        text = ""
        return HttpResponse(f"Post from {month}/{year}<br>{text}")


def index(request):
    logger.info('Index page accessed')
    context = Product.objects.all()
    return render(request, 'store/index.html', {"context": context})


def about(request):
    logger.debug('About page accessed')
    return render(request, 'store/about.html')

def info(request):
    logger.debug('Info page accessed')
    return render(request, 'store/info.html')

def year_post(request, year):
    text = ""
    return HttpResponse(f"Post from {year}<br>{text}")

def post_detail(request, year, month, slug):
    post = {
        "year": year,
        "month": month,
        "slug": slug,
        "title": "Кто быстрее создаёт списки в Python, list() или[]",
        "content": "В процессе написания очередной программы задумался над тем, "
                   "какой способ создания списков в Python работает быстрее...",
    }
    return JsonResponse(post, json_dumps_params={'ensure_ascii': False})