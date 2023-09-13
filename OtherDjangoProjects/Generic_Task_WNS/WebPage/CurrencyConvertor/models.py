from django.db import models

# Create your models here.
class Currency(models.Model):
    Currency_name = models.CharField(max_length=10)
    RoE = models.FloatField()

    def __str__(self):
        return f"({self.Currency_name} {self.RoE})"


#python manage.py shell -----> from CurrencyConvertor.models import Currency
#c_list=[Currency(1,'GBP',1.29),Currency(2,'EUR',1.10),Currency(3,'AED',0.27)]
#Currency.objects.bulk_create(c_list)  ------> [<Currency: Currency object (1)>, <Currency: Currency object (2)>, <Currency: Currency object (3)>]

#For Single Data Entry -----> Currency.objects.create(x="", y="")

#View Data ----> Currency.objects.all()
#Currency.objects.get(pk=1) -------> Gives Single Element/object. It fails when fetching through section having duplicate data
#<Currency: (GBP 1.29)>

#Currency.objects.filter(x="{value}").all()  -------> Getting all rows having x="{value}"
#Currency.objects.filter(x="{value}").filter(y="{value}").all()  -------> Getting all rows having x="{value}" and y="{value}"

#To form or '|' and '&' operation, we use Q class 
# from django.db.models import Q
# Currency.objects.filter(Q(x="{value}") or/and Q(y="{value}"))

#Filter + Field Lookup ----> 'Greater than/Less than' operations and 'Starts with' ---> Complex Operations 
#Syntax ----> Currency.objects.filter(columnName__startswith="{value}").all()  ----> .all() for having all relevant entries.
#Currency.objects.filter(columnName__in=[values]).all()  #fetches the entries that matches with any of list values.
# __gte={value} ----> greater than or equal to ; __lt ----> less than; __lte ----> less than or equal to; __isnull ..... etc

#Currency.objects.order_by('column name')

#Update : AED = Currency.objects.get(pk=1) ---> AED.{column name} = {update value} ---> AED.RoE = 0.30 ---> AED.save()
#Delete : AED = Currency.objects.get(pk=1) ---> AED.delete()