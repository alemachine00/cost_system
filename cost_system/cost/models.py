from django.db import models

class Order(models.Model):
    description = models.CharField(max_length=50)
    order_date = models.DateField(auto_now=True)
    amount = models.PositiveIntegerField()
    unit = models.CharField(max_length=5)
    order_finished = models.BooleanField(default=False, help_text='Is this order finished?')

    class Meta:
        ordering = ['-order_date']


    def __str__(self):
        return f'Order #{self.id}-{self.description}'

class Requisition(models.Model):
    description = models.CharField(max_length=50)
    amount = models.PositiveIntegerField()
    unit = models.CharField(max_length=5)
    unity_cost = models.PositiveIntegerField()
    date = models.DateField(auto_now=True)
    order = models.ForeignKey("Order", on_delete=models.CASCADE)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.description

    def total_cost(self):
        return self.unity_cost * self.amount

class WorkTicket(models.Model):
    employee_name = models.CharField(max_length=10)
    employee_last_name = models.CharField(max_length=10)
    date = models.DateField(auto_now=True)
    entry_time = models.TimeField(auto_now=True)
    finish_time = models.TimeField(auto_now=True)
    order_no = models.ForeignKey("Order", on_delete=models.CASCADE)
    hourly_rate = models.FloatField()
    work_hours = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.employee_name} work ticket'

    def labor_pay(self):
        return self.hourly_rate * self.work_hours