from django.db import models


class ProductCategory(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    name = models.CharField(verbose_name="category name", max_length=55)
    description = models.TextField(verbose_name="category description", blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    name = models.CharField(verbose_name="product name", max_length=55)
    image = models.ImageField(upload_to='products_images', blank=True)
    short_desc = models.CharField(verbose_name="", max_length=60, blank=True)
    description = models.TextField(verbose_name="product description", blank=True)
    price = models.DecimalField(verbose_name="price", max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(verbose_name="storage", default=0)

    def __str__(self):
        return "{} ({})".format(self.name, self.category.name)
