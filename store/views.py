import logging
from django.http import HttpResponse, JsonResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from .models import Product, Order, User, OrderProductCount
from datetime import date

logger = logging.getLogger(__name__)


def basket(request):
    try:
        order = Order.objects.filter(status='BS', customer=request.user.pk)
        count_of_items = OrderProductCount.objects.filter(order_id=order[0].pk)
        context = list()
        for i, k in enumerate(order[0].products.values_list()):
            context.append(list(k).copy())
            context[-1].append(count_of_items[i].count)
        return render(request, 'order/basket.html', {
            'context': context,
            "order": order[0],
            'msg': "Корзина покупок",
        })
    except:
        return render(request, 'order/basket.html',
                      {'msg': "Корзина пуста. Для совершения покупок перейдите на главную страницу."})


def order_list(request):
    orders = Order.objects.filter(status='CP', customer=request.user.pk)
    order_list = [
        {
            "id": order.id,
            "date": order.date_ordered,
            "total_price": order.total_price,
            "products": [
                [
                    item.products.product_name,
                    item.count,
                    item.products.price,
                ] for item in OrderProductCount.objects.filter(order_id=order.pk)],
        } for order in orders]

    return render(request, 'order/list.html', {'orders': order_list})


def order_detail(request, order_id):
    if request.method == 'POST':
        order = Order.objects.filter(pk=order_id)[0]
        print(order)
        order.status = 'CP'
        order.date_ordered = date.today()
        print(order.date_ordered)
        order.save()
        return render(request, 'order/detail.html', {'msg': "Заказ передан на оформление."})
    order = get_object_or_404(Order, id=order_id, status=Order.Status.COMPLETED)
    return render(request, 'order/detail.html',
                  {'order': order},
                  {'msg': "История заказов."})


@csrf_exempt
def index(request, id=None):
    context = Product.objects.all()
    if request.method == 'POST':
        add_to_cart(id, request.user.pk)
    return render(request, 'store/index.html', {"context": context})


def add_to_cart(product_id, user_pk):
    order = Order.objects.filter(status="BS", customer_id=user_pk).first()
    if not order:
        order = Order.objects.create(customer_id=user_pk)
    logger.info(f"Found uncompleted order: # {order.pk}")
    product = Product.objects.get(id=product_id)
    order.total_price += product.price
    order.save()
    product.order_products.add(order)
    k = OrderProductCount.objects.filter(order_id=order.pk, products_id=product_id).first()
    k.count += 1
    k.save()


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


class HelloView(View):
    def get(self, request):
        return HttpResponse("Hello from class!")


class MonthPost(View):
    def get(self, request, year, month):
        text = ""
        return HttpResponse(f"Post from {month}/{year}<br>{text}")
