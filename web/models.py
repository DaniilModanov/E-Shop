from django.db import models
from djmoney.models.fields import MoneyField


class GoodCard(models.Model):
    title = models.CharField(max_length=32)
    image = models.ImageField(upload_to="photos/%Y/%m/%d")
    price = MoneyField(max_digits=14, decimal_places=2,
                       default_currency="USD")
    category = models.ForeignKey('GoodCategory', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title + ' ' + str(self.price)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['title']


class GoodCategory(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория товаров'
        verbose_name_plural = 'Категории товаров'
        ordering = ['title']
