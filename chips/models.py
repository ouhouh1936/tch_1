from django.db import models


class Chips(models.Model):

    name = models.CharField(max_length=100)
    price = models.IntegerField()
    company = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "과자 관리"

    def __str__(self):
        return self.name
