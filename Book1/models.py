#from django.db import models
from django.db import models
from django.db.models.fields import CharField



# Create your models here.
class Book1(models.Model):
    name = models.CharField(max_length=50)
    qty = models.IntegerField()
    price = models.FloatField()
    is_published = models.BooleanField(default=False)
    published_date = models.DateField(null=True)
    is_deleted=models.PositiveSmallIntegerField(default='0')

    

    
    def __str__(self):
        return f"{self.__dict__}"

    class Meta:
        db_table="book"

