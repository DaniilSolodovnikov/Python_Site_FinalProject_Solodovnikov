from django.db import models
from django.contrib.auth.models import AbstractUser


# Модель пользователя
class User(AbstractUser):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    email = models.EmailField()
    status = models.BooleanField(default=False)


# Модель объявления
class Listing(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=200)
    rental_start_date = models.DateField(null=True, blank=True)
    rental_end_date = models.DateField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='listings')

    def __str__(self):
        return self.title


# Модель категории
class Category(models.Model):
    name = models.CharField(max_length=100)
    place = models.CharField(max_length=150, null=True, blank=True)
    description = models.TextField(blank=True)

    listings = models.ManyToManyField(Listing, related_name="categories")

    def __str__(self):
        return self.name


# Модель запроса на аренду
class RentalRequest(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    quantity_requested = models.PositiveIntegerField(default=1)
    comments = models.TextField(blank=True)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='requests')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='requests')

    def __str__(self):
        return f"Запрос на {self.listing} от {self.user}"


# Модель транзакции
class Transaction(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    period = models.DurationField()  # Период аренды
    request = models.OneToOneField(RentalRequest, on_delete=models.CASCADE, related_name='transaction')

    def __str__(self):
        return f"Транзакция для {self.request}"


class Ad(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='ads')
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)
