from django.db import models

# Create your models here.
class Coupon(models.Model):
    code = models.CharField(max_length=20)
    benefit = models.CharField(max_length=1000)
    explanation = models.CharField(max_length=2000)
    store = models.CharField(max_length=1000)
    start = models.DateField()
    deadline = models.DateField()
    status = models.BooleanField()

    def __str__(self):
        return '<Coupon:id=' + str(self.id) + ',' + self.code + ',' + self.benefit + '>'




