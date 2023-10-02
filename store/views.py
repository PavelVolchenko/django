import logging
from django.http import HttpResponse, JsonResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Product, Order

logger = logging.getLogger(__name__)


def add_to_cart(request, product_id):
    if request.method == 'POST':
        print(f'{product_id=}')
        product = Product.objects.filter(pk=product_id).first()
        print(f'{product=}')
        order = Order.objects.last()
        print(f'{order=}')
        if order.date_ordered is not None:
            order.clean()
        else:
            order.products.append(product)
            order.save()
    return render(request, 'store/index.html')


def order_list(request):
    orders = Order.completed.all()
    return render(request, 'order/list.html', {'orders': orders})

# def order_detail(request, id):
#     try:
#         order = Order.completed.get(id=id)
#     except Order.DoesNotExist:
#         raise Http404("No Order found.")
#
#     return render(request, 'order_detail.html', {'order': order})


def order_detail(request, id):
    order = get_object_or_404(Order, id=id, status=Order.Status.COMPLETED)
    return render(request, 'order/detail.html', {'order': order})


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
