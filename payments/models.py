from django.db import models
from customers.models import Customer

class Payment(models.Model):
    PAYMENT_TYPE = [
        ('cash', 'Cash'),
        ('cheque', 'Cheque'),
        ('upi', 'UPI'),
        ('credit card', 'Credit Card'),
        ('debit card', 'Debit Card'),
    ]
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_type = models.CharField(max_length=20, choices=PAYMENT_TYPE)
    is_paid = models.BooleanField(default=False)
    payment_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Payment for {self.customer.name} - ₹{self.amount}"
