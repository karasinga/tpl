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
    mpesa_contribution = models.FloatField()
    last_updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    # Django fix Admin plural
    class Meta:
        verbose_name_plural = "Sales"

    def __str__(self):
        return str(self.sales)


# class Summary(models.Model):
#     YEAR_CHOICES = [(y, y) for y in range(2020, datetime.date.today().year + 1)]
#     MONTH_CHOICES = [(str(i), calendar.month_name[i]) for i in range(1, 13)]
#
#     year = models.IntegerField(choices=YEAR_CHOICES, default=datetime.datetime.now().year, null=True)
#     month = models.CharField(max_length=9, choices=MONTH_CHOICES, default=datetime.datetime.now().month)
#     sales_name = models.ForeignKey(Sales, on_delete=models.CASCADE)
#     sales = models.FloatField()
#     cost_of_sales = models.FloatField()
#     gross_profit = models.FloatField()
#     expense = models.FloatField()
#     net_profit = models.FloatField()
#     last_updated = models.DateTimeField(auto_now_add=False, auto_now=True)
#     timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
#
#     # Django fix Admin plural
#     class Meta:
#         verbose_name_plural = "Summary"
#
#     def save(self, *args, **kwargs):
#         self.sales = self.sales_name.sales
#         self.net_profit = self.sales - self.cost_of_sales - self.expense
#         super(Summary, self).save(*args, **kwargs)
#
#     def __str__(self):
#         return str(self.sales)


class WeeklyData(models.Model):
    start_date = models.DateTimeField(auto_now_add=False, auto_now=False)
    end_date = models.DateTimeField(auto_now_add=False, auto_now=False)
    amount_received = models.FloatField()
    amount_referred = models.FloatField()
    balance = models.FloatField()
    weekly_last_updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    weekly_timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    # Django fix Admin plural
    class Meta:
        verbose_name_plural = "WeeklyData"

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

    # Django fix Admin plural
    class Meta:
        verbose_name_plural = "Twinkle"

    def __str__(self):
        # str()
        return str(self.amount_for_twinkle)


class AnnualTarget(models.Model):
    YEAR_CHOICES = [(y, y) for y in range(2020, datetime.date.today().year + 1)]
    year = models.IntegerField(choices=YEAR_CHOICES, default=datetime.datetime.now().year, null=True)
    target = models.FloatField()
    last_updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return str(self.target)


class MonthlyTargets(models.Model):
    YEAR_CHOICES = [(y, y) for y in range(2020, datetime.date.today().year + 1)]
    MONTH_CHOICES = [(str(i), calendar.month_name[i]) for i in range(1, 13)]
    year = models.IntegerField(choices=YEAR_CHOICES, default=datetime.datetime.now().year, null=True)
    month = models.CharField(max_length=9, choices=MONTH_CHOICES, default=datetime.datetime.now().month)
    lab_target = models.FloatField()
    pharma_target = models.FloatField()
    last_updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    # Django fix Admin plural
    class Meta:
        verbose_name_plural = "MonthlyTargets"

    def __str__(self):
        return str(self.lab_target)


class SummaryTable(models.Model):
    YEAR_CHOICES = [(y, y) for y in range(2020, datetime.date.today().year + 1)]
    MONTH_CHOICES = [(str(i), calendar.month_name[i]) for i in range(1, 13)]

    year = models.IntegerField(choices=YEAR_CHOICES, default=datetime.datetime.now().year, null=True)
    month = models.CharField(max_length=9, choices=MONTH_CHOICES, default=datetime.datetime.now().month)
    sales_name = models.ForeignKey(Sales, on_delete=models.CASCADE)
    sales = models.FloatField()
    cost_of_sales = models.FloatField()
    gross_profit = models.FloatField()
    expense = models.FloatField()
    net_profit = models.FloatField()
    last_updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    # Django fix Admin plural
    class Meta:
        verbose_name_plural = "Summary"

    def save(self, *args, **kwargs):
        if not self.sales:
            self.sales = self.sales_name.sales
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.sales}-{self.cost_of_sales}-{self.net_profit}"


class Stock(models.Model):
    YEAR_CHOICES = [(y, y) for y in range(2020, datetime.date.today().year + 1)]
    MONTH_CHOICES = [(str(i), calendar.month_name[i]) for i in range(1, 13)]
    year = models.IntegerField(choices=YEAR_CHOICES, default=datetime.datetime.now().year, null=True)
    month = models.CharField(max_length=9, choices=MONTH_CHOICES, default=datetime.datetime.now().month)
    end_month_stock  = models.FloatField()
    last_updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    # Django fix Admin plural
    class Meta:
        verbose_name_plural = "EndOfMonthStock"

    def __str__(self):
        return str(self.end_month_stock)

class Expiry(models.Model):
    YEAR_CHOICES = [(y, y) for y in range(2020, datetime.date.today().year + 1)]
    MONTH_CHOICES = [(str(i), calendar.month_name[i]) for i in range(1, 13)]
    year = models.IntegerField(choices=YEAR_CHOICES, default=datetime.datetime.now().year, null=True)
    month = models.CharField(max_length=9, choices=MONTH_CHOICES, default=datetime.datetime.now().month)
    pharmacy_expiries  = models.FloatField()
    lab_expiries  = models.FloatField()
    last_updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    # Django fix Admin plural
    class Meta:
        verbose_name_plural = "Expiry"

    def __str__(self):
        return str(self.pharmacy_expiries)
