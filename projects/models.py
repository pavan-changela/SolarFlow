from django.db import models
from quotation.models import Quotation

class Project(models.Model):
    quotation = models.OneToOneField(Quotation, on_delete=models.CASCADE)
    start_date = models.DateField(auto_now_add=True)
    completion_deadline = models.DateField()
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"Project for {self.quotation.customer.name}"
