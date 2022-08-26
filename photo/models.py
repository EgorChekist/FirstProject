from django.db import models

# Create your models here.

class Photo(models.Model):
    number = models.PositiveIntegerField("Номер", unique=True)
    cost = models.PositiveIntegerField("Цена")
    picture = models.ImageField("ФОТО")
    place = models.CharField("Место", max_length=256)

    def __str__(self):
        return f"Фотография{self.number}"


class Contact(models.Model):
    name = models.CharField("Имя", max_length=128)
    email = models.EmailField("Почта")
    message = models.CharField("Текст", max_length=1028)

    def __str__(self):
        return f"Контакт {self.name}"