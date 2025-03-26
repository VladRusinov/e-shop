from django.contrib.auth.models import AbstractUser
from django.db import models

from catalog.models import Product


class User(AbstractUser):
    """Модель пользователя."""


class ShoppingCart(models.Model):
    """Модель корзины."""

    user = models.ForeignKey(
        User,
        verbose_name='Пользователь',
        related_name='cart_items',
        on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        Product,
        verbose_name="Товар",
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ['user']
        verbose_name = 'корзина'
        verbose_name_plural = 'корзины'
        default_related_name = 'shopping_carts'
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'product'], name='unique_shopping_cart'
            ),
        ]

    def __str__(self):
        return f'{self.user} - {self.product}'
