from django.db import models


class Store(models.Model):
    name = models.CharField(max_length=255)
    image = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "Store"
        verbose_name_plural = "Stores"

    def __str__(self):
        return self.name


class Product(models.Model):
    store = models.ForeignKey(
        Store, related_name='products',
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=255)
    image = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    price = models.FloatField(default=0)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.title
