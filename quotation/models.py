from django.db import models
from customers.models import Customer
from django.utils import timezone

class Quotation(models.Model):
    customer = models.ForeignKey('customers.Customer', on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    quotation_no = models.CharField(max_length=20, unique=True, blank=True)
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
    
    def save(self, *args, **kwargs):
        if not self.quotation_no:
            # Auto-generate: e.g. QTN-20250807-001
            today = timezone.now().strftime("%Y%m%d")
            prefix = f"QTN-{today}-"
            count_today = Quotation.objects.filter(quotation_no__startswith=prefix).count() + 1
            self.quotation_no = f"{prefix}{count_today:03d}"
        super().save(*args, **kwargs)