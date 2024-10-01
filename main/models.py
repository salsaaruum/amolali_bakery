import uuid #tambahkan baris ini di paling atas
from django.contrib.auth.models import User
from django.db import models

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # tambahkan baris ini juga
    name = models.CharField(max_length=255)  # Atribut nama product
    price = models.IntegerField()  # Atribut harga product
    description = models.TextField()  # Atribut deskripsi product
    category = models.CharField(max_length=100, blank=True, null=True)  # Atribut kategori product
    image = models.URLField()  # Atribut gambar product

    def __str__(self):
        return self.name
