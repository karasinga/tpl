import datetime
import calendar

from django.db import models


class Sales(models.Model):
    YEAR_CHOICES = [(y, y) for y in range(2020, datetime.date.today().year + 1)]
    MONTH_CHOICES = [(str(i), calendar.month_name[i]) for i in range(1, 13)]

    year = models.IntegerField(choices=YEAR_CHOICES, default=datetime.datetime.now().year, null=True)
    month = models.CharField(max_length=9, choices=MONTH_CHOICES, default=datetime.datetime.now().month)
    sales = models.FloatField()
    lab_contribution = models.FloatField()
    pharmacy_contribution = models.FloatField()
    last_updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return f"{self.sales}-{self.lab_contribution}-{self.pharmacy_contribution}"


class WeeklyData(models.Model):
    start_date = models.DateTimeField(auto_now_add=False, auto_now=False)
    end_date = models.DateTimeField(auto_now_add=False, auto_now=False)
    amount_received = models.FloatField()
    amount_referred = models.FloatField()
    balance = models.FloatField()
    weekly_last_updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    weekly_timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return f"{self.amount_received}-{self.amount_referred}-{self.balance}"


class Twinkle(models.Model):
    YEAR_CHOICES = [(y, y) for y in range(2020, datetime.date.today().year + 1)]
    MONTH_CHOICES = [(str(i), calendar.month_name[i]) for i in range(1, 13)]

    year = models.IntegerField(choices=YEAR_CHOICES, default=datetime.datetime.now().year, null=True)

    month = models.CharField(max_length=9, choices=MONTH_CHOICES, default=datetime.datetime.now().month)
    amount_to_twinkle = models.FloatField()
    amount_to_metropolis_diamond = models.FloatField()
    amount_for_twinkle = models.FloatField()
    commission = models.FloatField()
    last_updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    weekly_timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.amount_for_twinkle


class AnnualTarget(models.Model):
    YEAR_CHOICES = [(y, y) for y in range(2020, datetime.date.today().year + 1)]
    year = models.IntegerField(choices=YEAR_CHOICES, default=datetime.datetime.now().year, null=True)
    target = models.FloatField()
    last_updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.target
