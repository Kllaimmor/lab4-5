from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Animal(models.Model):
    name = models.CharField(max_length=100)
    category = models.ManyToManyField(Category)
    uniqueness = models.TextField()
    powermeter = models.DecimalField(verbose_name="Сила(вимірюється кількістю знищеного мирного населення в Палестині)", max_digits= 10,decimal_places=2)
    counter = models.PositiveIntegerField(verbose_name="Контра")
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    size = models.DecimalField(verbose_name="Розміри(В Метрах)",max_digits= 10,decimal_places=2)
    appearance = models.DateField(verbose_name="Дата створення")

    def __str__(self):
        return self.name
