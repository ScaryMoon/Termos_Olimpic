from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from .models import Product, Category, Manufacturer, Cart, CartItem

def home(request):
    return HttpResponse("""
    <h1>Главная страница магазина термосов.</h1>
    
    Перейти:
    <p><a href = "/about/">Страница об авторе</a></p>
    <p><a href = "/store/">Страница магазина</a></p>
    """)

def about(request):
    return HttpResponse("""
    <h1>Страница об авторе.</h1>

    <p>Лабораторную работу выполнил: Ковалёв Станислав 87ТП.</p>
    """)

def store(request):
    return HttpResponse("""
    <h1>Страница магазина.</h1>
    
    <p>Тема лабораторной: Интернет-магазин термосов.</p>

    <p>Ассортимент:</p>
    <p>- Термос для чая</p>
    <p>- Термос для кофе</p>
    <p>- Термокружка</p>
    """)

# Список товаров
def product_list(request):

    products = Product.objects.all()

    search = request.GET.get('search')

    if search:
        products = products.filter(
            Q(name__icontains=search) |
            Q(description__icontains=search)
        )

    return render(request, 'shop/product_list.html', {
        'products': products
    })

# Детали товара
def product_detail(request, pk):

    product = get_object_or_404(Product, pk=pk)

    return render(request, 'shop/product_detail.html', {
        'product': product
    })

# Корзина
@login_required
def cart_view(request):

    cart, created = Cart.objects.get_or_create(user=request.user)

    items = cart.items.all()

    total = cart.total_price()

    return render(request, 'shop/cart.html', {
        'items': items,
        'total': total
    })

# Добавить в корзину
@login_required
def add_to_cart(request, product_id):

    product = get_object_or_404(Product, id=product_id)

    cart, created = Cart.objects.get_or_create(user=request.user)

    item, created = CartItem.objects.get_or_create(
        cart=cart,
        product=product
    )

    if not created:
        item.quantity += 1
        item.save()

    return redirect('cart')

# Обновить корзину
@login_required
def update_cart(request, item_id):

    item = get_object_or_404(CartItem, id=item_id)

    quantity = int(request.POST.get('quantity'))

    if quantity <= item.product.quantity:
        item.quantity = quantity
        item.save()

    return redirect('cart')

# Удалить из корзины
@login_required
def remove_from_cart(request, item_id):

    item = get_object_or_404(CartItem, id=item_id)

    item.delete()

    return redirect('cart')