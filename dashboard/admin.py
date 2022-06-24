from django.contrib import admin
from dashboard.models import Sales, WeeklyData, Twinkle, AnnualTarget, MonthlyTargets, SummaryTable, Stock, Expiry

# change admin header
# admin.site.site_header="TPL Data Analytics Dashboard"

# Register your models here.


admin.site.register(Sales)
admin.site.register(WeeklyData)
admin.site.register(Twinkle)
admin.site.register(AnnualTarget)
admin.site.register(MonthlyTargets)
admin.site.register(SummaryTable)
admin.site.register(Stock)
admin.site.register(Expiry)
