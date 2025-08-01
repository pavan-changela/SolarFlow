from django.db import models
from customers.models import Customer
from django.utils import timezone

class Quotation(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    quotation_no = models.PositiveIntegerField(unique=True)
    module_quantity = models.PositiveIntegerField()
    module_wp = models.PositiveIntegerField()
    inverter_size = models.FloatField(help_text="in kW")

    complete_epc_rate = models.FloatField()
    meter_charge = models.FloatField(default=3350)
    fabrication_rate = models.FloatField(default=4000)  # per kW
    module_rate = models.FloatField()
    inverter_rate = models.FloatField()

    gst_percent = models.FloatField(default=12.0)  # only for EPC

    def kw_total(self):
        return (self.module_quantity * self.module_wp) / 1000

    def __str__(self):
        return f"Quotation #{self.quotation_no} for {self.customer.name}"