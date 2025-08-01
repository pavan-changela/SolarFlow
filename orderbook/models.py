from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from quotation.models import Quotation

class OrderItem(models.Model):
    quotation = models.ForeignKey(Quotation, on_delete=models.CASCADE)
    item_type = models.CharField(max_length=20, choices=[('panel', 'Panel'), ('inverter', 'Inverter')])
    is_ordered = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.item_type.capitalize()} Order for {self.quotation.customer.name}"
    
def create_order_items(sender, instance, created, **kwargs):
    if created:
        OrderItem.objects.create(quotation=instance, item_type='panel')
        OrderItem.objects.create(quotation=instance, item_type='inverter')
