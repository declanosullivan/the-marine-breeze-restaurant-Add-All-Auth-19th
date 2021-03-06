from django.db import models

class Tables(models.Model):
    """
    Models for tables 
    """
    TABLE_NAMES = (
        ('1', 'ONE'),
        ('2', 'TWO'),
        ('3', 'THREE'),
        ('4', 'FOUR'),
    )  

    TABLE_STATUSES = (
        ('ACT', 'ACTIVE'),
        ('OFF', 'OFFLINE'),
    )  

    table_no = models.CharField(max_length=5, choices=TABLE_NAMES, unique=True)
    table_seats = models.SmallIntegerField()
    table_status = models.CharField(max_length=10, choices=TABLE_STATUSES, default="Active")

    def __str__(self):
        return f"Table {self.table_no} has {self.table_seats} and is {self.table_status}"

class TableAvail(models.Model):
    """
    Models for table availability
    """
    table_no = models.OneToOneField(Tables,on_delete=models.CASCADE)
    table_date = models.DateField()
    table_start = models.TimeField()
    table_end = models.TimeField()
    




