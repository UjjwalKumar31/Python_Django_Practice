from django.db import models

# Create your models here.
class Branch(models.Model):
    BranchID = models.IntegerField(unique=True)
    BranchName = models.CharField(max_length=15)
    ActiveFlag = models.IntegerField(default=1)
    InactiveDate = models.DateField(null=True)

    def __str__(self):
        return f"{self.BranchID} -- {self.BranchName} -- {self.ActiveFlag} -- {self.InactiveDate}"

class Broker(models.Model):
    BrokerID = models.IntegerField(unique=True)
    BrokerName = models.CharField(max_length=15)
    ActiveFlag = models.IntegerField(default=1)
    InactiveDate = models.DateField(null=True)

    def __str__(self):
        return f"{self.BrokerID} -- {self.BrokerName} -- {self.ActiveFlag} -- {self.InactiveDate}"



#python manage.py makemigrations DataManage
#python manage.py migrate
#python manage.py sqlmigrate DataManage 0001  ----> To look for sql script.