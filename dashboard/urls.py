from django.urls import path
from . import views

urlpatterns = [
    path('trends/', views.index, name="dashboard-index"),
    path('lab-phram-contribution/', views.contribution, name="dashboard-contribution"),
    path('lab-phram-targets/', views.against_target, name="dashboard-against_target"),
    path('tpl-revenue/', views.revenue, name="dashboard-revenue"),
    path('summary-viz/', views.summary_table, name="dashboard-summary_viz"),
    path('annual-performance/', views.annual_performance, name="dashboard-annual_performance"),
    path('moving-target/', views.moving_target, name="dashboard-moving_target"),
    path('staff/', views.staff, name="dashboard-staff"),
    path('product/', views.products, name="dashboard-product"),
    path('product/weekly/', views.weekly_sales, name="dashboard-product-weekly"),
    path('product/delete/<int:pk>/', views.product_delete, name="dashboard-product-delete"),
    path('product/update/<int:pk>/', views.product_update, name="dashboard-product-update"),
    path('order/', views.order, name="dashboard-order"),
    path('product/weekly/update/<int:pk>/', views.weekly_sales_update, name="dashboard-weekly-update"),
    path('product/weekly/delete/<int:pk>/', views.weekly_sales_delete, name="dashboard-weekly-delete"),

    path('twinkle/', views.twinkle_commission, name="dashboard-twinkle"),
    path('twinkle/delete/<int:pk>/', views.twinkle_delete, name="dashboard-twinkle-delete"),
    path('twinkle/update/<int:pk>/', views.twinkle_update, name="dashboard-twinkle-update"),
    path('target/', views.targets, name="dashboard-target"),
    path('target/update/<int:pk>/', views.target_update, name="dashboard-target-update"),
    path('target/delete/<int:pk>/', views.target_delete, name="dashboard-target-delete"),

    path('monthly-targets/', views.monthlytargets, name="dashboard-monthly-targets"),
    path('monthly-targets/delete/<int:pk>/', views.monthly_target_delete, name="dashboard-monthly-targets-delete"),
    path('monthly-targets/update/<int:pk>/', views.monthly_target_update, name="dashboard-monthly-targets-update"),

    path('summary/', views.summary, name="dashboard-summary"),
    path('summary/delete/<int:pk>/', views.summary_delete, name="dashboard-summary-delete"),
    path('summary/update/<int:pk>/', views.summary_update, name="dashboard-summary-update"),

    path('end-of-month-stock/', views.stocks, name="dashboard-stock"),
    path('stock/delete/<int:pk>/', views.stock_delete, name="dashboard-stock-delete"),
    path('stock/update/<int:pk>/', views.stock_update, name="dashboard-stock-update"),

    path('expiries/', views.expiries, name="dashboard-expiry"),
    path('expiries/delete/<int:pk>/', views.expiries_delete, name="dashboard-expiry-delete"),
    path('expiries/update/<int:pk>/', views.expiries_update, name="dashboard-expiry-update"),
]
