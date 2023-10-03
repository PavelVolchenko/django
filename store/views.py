import logging
from django.http import HttpResponse, JsonResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from .models import Product, Order

logger = logging.getLogger(__name__)


def basket(request):
    order = Order.objects.filter(status='BS', customer=request.user.pk)
    print(order[0].products.values_list())
    return render(request, 'order/basket.html', {'order': order[0].products.values_list(), "total_price": order[0].total_price})


@csrf_exempt
def add_to_cart(request, id):
    if request.method == 'POST':
        logger.info(f"Try add to cart product: {id=}")
        order = Order.objects.filter(status="BS", customer=request.user.pk).first()
        if not order:
            order = Order.objects.create(customer=request.user)
        logger.info(f"Found uncompleted order: {order=}")
        product = Product.objects.filter(pk=id).first()
        order.products.add(id)
        order.total_price = order.total_price + product.price
        product.quantity = product.quantity + 1
        product.save()
        order.save()
    return render(request, 'store/index.html')


def order_list(request):
    orders = Order.completed.all()
    logger.info(f"Showing {len(orders)} completed orders for user: {request.user.username}")
    return render(request, 'order/list.html', {'orders': orders.values_list()})


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
