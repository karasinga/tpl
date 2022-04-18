from django.contrib import admin
from dashboard.models import  Sales,WeeklyData,Twinkle,AnnualTarget

# change admin header
# admin.site.site_header="TPL Data Analytics Dashboard"

# Register your models here.


admin.site.register(Sales)
admin.site.register(WeeklyData)
admin.site.register(Twinkle)
admin.site.register(AnnualTarget)
