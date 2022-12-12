from django.db import models
from django.urls import reverse

# Category model

class Category(models.Model):
    name = models.CharField(max_length=250, help_text="Category name")
    slug = models.SlugField(max_length=250,
                            unique=True)
    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name']),
        ]
        verbose_name_plural = 'categories'
    def __str__(self):
        return self.name
        
    def get_absolute_url(self):
        return reverse('shop:product_list_by_category',
                       args=[self.slug]) 


# Product model

class Product(models.Model):
    category = models.ForeignKey(Category,
                                 related_name='products',
                                 on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    image = models.ImageField(upload_to='products/%Y/%m/%d',
                              blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10,
                                decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['name']),
            models.Index(fields=['-created']),
        ]
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name

