from django.urls import path
from . import views

urlpatterns = [
    path('trends/', views.index, name="dashboard-index"),
    path('lab-phram-contribution/', views.contribution, name="dashboard-contribution"),
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
]
