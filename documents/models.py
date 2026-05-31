from django.db import models
from users.models import MainUser
from django.urls import reverse

# Create your models here.

class Documents(models.Model):
    user = models.ForeignKey(MainUser, on_delete=models.CASCADE, verbose_name="Foydalanuvchi", related_name="hujjatlar")
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name="hujjatlar", verbose_name="Hujjat turi")
    name = models.CharField(max_length=30, verbose_name="Hujjat nomi")
    price = models.DecimalField(max_digits=16, decimal_places=2, verbose_name="Narxi")
    slug = models.SlugField(max_length=250, db_index=True, verbose_name="URL", unique=True)
    image = models.ImageField(upload_to='documents/images', verbose_name="Rasm")
    description = models.TextField(null=True, blank=True, verbose_name="Qo'shimcha ma'lumot")
    time_create = models.DateField(auto_now_add=True, verbose_name="Yaratilgan vaqti")
    time_update = models.DateField(auto_now=True, verbose_name="Yangilangan vaqti")

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('document_detail', kwargs={'document_slug': self.slug})
    
    def get_absolute_url1(self):
        return reverse('delete_document', kwargs={'document_slug': self.slug})

    class Meta:
        verbose_name = "Hujjat"
        verbose_name_plural = "Hujjatlar"
    
class Category(models.Model):
    user = models.ForeignKey(MainUser, on_delete=models.CASCADE, related_name="category")
    name = models.CharField(max_length=30, verbose_name="Hujjat turi")
    slug = models.SlugField(max_length=255, verbose_name="URL", db_index=True, unique=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Hujjatlar turi - (Category)"
        verbose_name_plural = "Hujjatlar turi - (Category)"