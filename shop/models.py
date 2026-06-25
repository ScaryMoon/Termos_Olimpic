from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    full_name = models.CharField(
        max_length=100
    )

    phone = models.CharField(
        max_length=20
    )

    address = models.TextField()

    # индивидуальное задание
    favorite_category = models.CharField(
        max_length=100,
        blank=True
    )   

    delivery_city = models.CharField(
        max_length=100,
        blank=True
    )

    def __str__(self):
        return self.user.username
        
# Модель производитель
class Manufacturer(models.Model):
    name = models.CharField(max_length = 100)
    country = models.CharField(max_length = 100)
    description = models.TextField(blank = True)

    def __str__(self):
        return self.name

# Модель категория
class Category(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField(blank = True)

    def __str__(self):
        return self.name

# Модель товар
class Product(models.Model):
    name = models.CharField(max_length = 200)
    description = models.TextField()
    photo = models.ImageField(upload_to = 'products/', blank = True)
    price = models.DecimalField(max_digits = 10, decimal_places = 2)
    quantity = models.IntegerField()
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    manufacturer = models.ForeignKey(Manufacturer, on_delete = models.CASCADE)

    def __str__(self):
        return self.name

# Валидация
def clean(self):
    from django.core.exceptions import ValidationError
    if self.price < 0:
        raise ValidationError("Цена не может быть отрицательной")
    if self.quantity < 0:
        raise ValidationError("Количество не может быть отрицательным")

# Корзина
class Cart(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"Корзина пользователя {self.user.username}"

    def total_price(self):
        return sum(item.total_price() for item in self.items.all())

# Элемент корзины
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete = models.CASCADE, related_name = 'items')
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.product.name} ({self.quantity} шт.)"

    def total_price(self):
        return self.product.price * self.quantity
    
    def clean(self):
        from django.core.exceptions import ValidationError
        if self.quantity > self.product.quantity:
            raise ValidationError("Недостаточно товара на складе")
        
class Order(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    address = models.TextField()

    total = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"Заказ №{self.id}"
    
class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='items'
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )

    quantity = models.PositiveIntegerField()

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    def __str__(self):
        return self.product.name

class Favorite(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )
    def __str__(self):
        return f"{self.user.username} - {self.product.name}"