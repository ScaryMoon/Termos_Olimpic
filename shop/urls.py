from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'products', views.ProductViewSet)
router.register(r'categories', views.CategoryViewSet)
router.register(r'manufacturers', views.ManufacturerViewSet)
router.register(r'carts', views.CartViewSet)
router.register(r'cartitems', views.CartItemViewSet)

urlpatterns = [
    path('', views.home),
    path('about/', views.about),
    path('store/', views.store),

    path('catalog/', views.product_list, name = 'catalog'),
    path('catalog/<int:pk>/', views.product_detail, name = 'product_detail'),
    
    path('cart/', views.cart_view, name = 'cart'),
    path('cart/add/<int:product_id>/', views.add_to_cart, name = 'add_to_cart'),
    path('cart/update/<int:item_id>/', views.update_cart, name = 'update_cart'),
    path('cart/remove/<int:item_id>/', views.remove_from_cart, name = 'remove_from_cart'),

    path('checkout/', views.checkout, name='checkout'),
]

urlpatterns += router.urls