# service/models.py
from django.db import models
from customers.models import Customer

class Complaint(models.Model):
    COMPLAINT_TYPE = [
        ('inverter', 'Inverter'),
        ('wiring', 'Wiring'),
        ('panel', 'Panel'),
    ]
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    complaint_type = models.CharField(max_length=20, choices=COMPLAINT_TYPE)
    complaint_id = models.AutoField(primary_key=True)
    description = models.TextField(blank=True)
    is_resolved = models.BooleanField(default=False)

    def __str__(self):
        return f"Complaint {self.complaint_id} - {self.customer.name}"
