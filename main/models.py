from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)  # Atribut nama product
    price = models.IntegerField()  # Atribut harga product
    description = models.TextField()  # Atribut deskripsi product
    category = models.CharField(max_length=100, blank=True, null=True)  # Atribut kategori product
    image = models.ImageField()  # Atribut gambar product

    def __str__(self):
        return self.name
