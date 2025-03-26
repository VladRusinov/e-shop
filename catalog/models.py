from django.core.validators import MinValueValidator
from django.db import models


class Category(models.Model):
    """Модель с категориями"""

    title = models.CharField(max_length=256, verbose_name='Название')
    slug = models.SlugField(
        unique=True,
        verbose_name='Идентификатор',
        help_text=(
            'Идентификатор страницы для URL;'
            ' разрешены символы латиницы, цифры, дефис и подчёркивание.'
        )
    )

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    description = models.TextField('Описание')
    image = models.ImageField(
        'Фото',
        upload_to='product_images',
        blank=True,
        null=True
    )
    price = models.DecimalField(
        'Цена',
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name='Категория',
    )

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        default_related_name = 'products'
        ordering = ('id',)

    def __str__(self):
        return self.title
