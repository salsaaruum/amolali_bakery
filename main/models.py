from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=255)  # Atribut nama item
    price = models.IntegerField()  # Atribut harga item
    description = models.TextField()  # Atribut deskripsi item
    category = models.CharField(max_length=100, blank=True, null=True)  # Atribut kategori item, optional
    image = models.ImageField(upload_to='items/', blank=True, null=True)  # Atribut gambar item, optional

    def __str__(self):
        return self.name

# Create your models here.
