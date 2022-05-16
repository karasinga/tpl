import calendar
import math
from datetime import datetime
import functools

# import numpy as np
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

import pandas as pd
from pandas.tseries.offsets import MonthEnd
import plotly.graph_objects as go
from plotly.offline import plot
import plotly.express as px
from plotly.subplots import make_subplots

from .dash import dash, profile
from .forms import SalesForm, WeeklyDataForm, TwinkleForm, AnnualTargetForm
from .models import Sales, WeeklyData, Twinkle, AnnualTarget
from .filter import SalesFilter


def pagination_(request, item_list):
    page = request.GET.get('page', 1)

    paginator = Paginator(item_list, 9)
    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)
    return items


# Create your views here.
@login_required(login_url='user-login')
def index(request):
    monthly_target, sales_plot, all_plot, lab_plot, phar_plot, contr_plot, total_sales_plot, moving_target_plot, \
    perfomance_so_far, last_month_with_data, reports_so_far, current_year_sales, monthly_target = dash()

    context = {
        "sales_plot": sales_plot,
        "all_plot": all_plot,
        "lab_plot": lab_plot,
        "phar_plot": phar_plot,
        "contrib_lists": contr_plot,
        "total_sales_plot": total_sales_plot,
        "moving_target_plot": moving_target_plot,
        "perfomance_so_far":perfomance_so_far,
        "last_month_with_data":last_month_with_data,
        "reports_so_far":reports_so_far,
        "current_year_sales":current_year_sales,
        "monthly_target":monthly_target,

    }
    return render(request, "dashboard/index.html", context)



@login_required(login_url='user-login')
def contribution(request):
    monthly_target, sales_plot, all_plot, lab_plot, phar_plot, contr_plot, total_sales_plot, moving_target_plot, \
    perfomance_so_far, last_month_with_data, reports_so_far, current_year_sales, monthly_target = dash()

    context = {
        "sales_plot": sales_plot,
        "all_plot": all_plot,
        "lab_plot": lab_plot,
        "phar_plot": phar_plot,
        "contrib_lists": contr_plot,
        "total_sales_plot": total_sales_plot,
        "moving_target_plot": moving_target_plot,
        "perfomance_so_far":perfomance_so_far,
        "last_month_with_data":last_month_with_data,
        "reports_so_far":reports_so_far,
        "current_year_sales":current_year_sales,
        "monthly_target":monthly_target,

    }
    return render(request, "dashboard/contribution.html", context)


@login_required(login_url='user-login')
def annual_performance(request):
    monthly_target, sales_plot, all_plot, lab_plot, phar_plot, contr_plot, total_sales_plot, moving_target_plot, \
    perfomance_so_far, last_month_with_data, reports_so_far, current_year_sales, monthly_target = dash()

    context = {
        "sales_plot": sales_plot,
        "all_plot": all_plot,
        "lab_plot": lab_plot,
        "phar_plot": phar_plot,
        "contrib_lists": contr_plot,
        "total_sales_plot": total_sales_plot,
        "moving_target_plot": moving_target_plot,
        "perfomance_so_far":perfomance_so_far,
        "last_month_with_data":last_month_with_data,
        "reports_so_far":reports_so_far,
        "current_year_sales":current_year_sales,
        "monthly_target":monthly_target,

    }
    return render(request, "dashboard/annual_performance.html", context)


@login_required(login_url='user-login')
def moving_target(request):
    monthly_target, sales_plot, all_plot, lab_plot, phar_plot, contr_plot, total_sales_plot, moving_target_plot, \
    perfomance_so_far, last_month_with_data, reports_so_far, current_year_sales, monthly_target = dash()

    context = {
        "sales_plot": sales_plot,
        "all_plot": all_plot,
        "lab_plot": lab_plot,
        "phar_plot": phar_plot,
        "contrib_lists": contr_plot,
        "total_sales_plot": total_sales_plot,
        "moving_target_plot": moving_target_plot,
        "perfomance_so_far":perfomance_so_far,
        "last_month_with_data":last_month_with_data,
        "reports_so_far":reports_so_far,
        "current_year_sales":current_year_sales,
        "monthly_target":monthly_target,

    }
    return render(request, "dashboard/remaining_target.html", context)


@login_required(login_url='user-login')
def staff(request):
    # # get all data from database
    # qs = Project.object.all()
    # # assign it to a dataframe using list comprehension
    # project_data = [
    #     {'Project': x.name,
    #      'Project': x.name,
    #      'Project': x.name,
    #      'Project': x.name,
    #      'Project': x.name,
    #      } for x in qs
    # ]
    # # convert data from database to a dataframe
    # df=pd.DataFrame(project_data)

    df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2014_usa_states.csv')

    fig = go.Figure(data=[go.Table(
        header=dict(values=list(df.columns),
                    fill_color='paleturquoise',
                    align='left'),
        cells=dict(values=[df.Rank, df.State, df.Postal, df.Population],
                   fill_color='lavender',
                   align='left'))
    ])

    table_plot = plot(fig, output_type="div")
    context = {"table_plot": table_plot}
    return render(request, "dashboard/staff.html", context)


@login_required(login_url='user-login')
def products(request):
    item_list = Sales.objects.all().order_by('-year', '-month')
    # FILTER SALES MODEL
    my_filter = SalesFilter(request.GET, queryset=item_list)
    item_list = my_filter.qs
    if request.method == "POST":
        form = SalesForm(request.POST)
        if form.is_valid():
            form.save()
            month_name = form.cleaned_data.get('month')
            year_name = form.cleaned_data.get('year')
            messages.success(request, f"{calendar.month_name[int(month_name)]} {year_name} data has been added")
            return redirect('dashboard-product')
    else:
        form = SalesForm()
    items = pagination_(request, item_list)

    context = {
        'form': form,
        "items": items,
        "myFilter": my_filter,
    }
    return render(request, "dashboard/product.html", context)


@login_required(login_url='user-login')
def order(requests):
    return render(requests, "dashboard/order.html")


@login_required(login_url='user-login')
def product_update(request, pk):
    item = Sales.objects.get(id=pk)
    if request.method == "POST":
        form = SalesForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect("dashboard-product")
    else:
        form = SalesForm(instance=item)
    context = {
        "form": form
    }
    return render(request, 'dashboard/product_update.html', context)


@login_required(login_url='user-login')
def product_delete(request, pk):
    item = Sales.objects.get(id=pk)
    if request.method == "POST":
        item.delete()
        return redirect("dashboard-product")
    context = {
        "items": item
    }
    return render(request, 'dashboard/product_delete.html', context)


@login_required(login_url='user-login')
def weekly_sales(request):
    item_list = WeeklyData.objects.all().order_by('start_date')
    if request.method == "POST":
        form = WeeklyDataForm(request.POST)
        if form.is_valid():
            form.save()
            start_date_name = form.cleaned_data.get('start_date').date()
            end_date_name = form.cleaned_data.get('end_date').date()
            messages.success(request, f"Data  between {start_date_name} and {end_date_name} has been added")
            return redirect('dashboard-product-weekly')
    else:
        form = WeeklyDataForm()

    items = pagination_(request, item_list)

    context = {
        'form': form,
        "items": items,
    }
    return render(request, "dashboard/product_weekly.html", context)


@login_required(login_url='user-login')
def weekly_sales_update(request, pk):
    item = WeeklyData.objects.get(id=pk)
    if request.method == "POST":
        form = WeeklyDataForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect("dashboard-product-weekly")
    else:
        form = WeeklyDataForm(instance=item)
    context = {
        "form": form
    }
    return render(request, 'dashboard/product_weekly_update.html', context)


@login_required(login_url='user-login')
def weekly_sales_delete(request, pk):
    item = WeeklyData.objects.get(id=pk)
    if request.method == "POST":
        item.delete()
        return redirect("dashboard-product-weekly")
    context = {
        "items": item
    }
    return render(request, 'dashboard/product_weekly_delete.html', context)


@login_required(login_url='user-login')
def twinkle_commission(request):
    item_list = Twinkle.objects.all()
    if request.method == "POST":
        form = TwinkleForm(request.POST)
        if form.is_valid():
            form.save()
            month_name = form.cleaned_data.get('month')
            year_name = form.cleaned_data.get('year')
            messages.success(request, f"{calendar.month_name[int(month_name)]} {year_name} data has been added")
            return redirect('dashboard-twinkle')
    else:
        form = TwinkleForm()

    items = pagination_(request, item_list)

    context = {
        'form': form,
        "items": items,
    }
    return render(request, "dashboard/twinkle.html", context)


@login_required(login_url='user-login')
def twinkle_delete(request, pk):
    item = Twinkle.objects.get(id=pk)
    if request.method == "POST":
        item.delete()
        return redirect("dashboard-twinkle")
    context = {
        "items": item
    }
    return render(request, 'dashboard/twinkle_delete.html', context)


@login_required(login_url='user-login')
def twinkle_update(request, pk):
    item = Twinkle.objects.get(id=pk)
    if request.method == "POST":
        form = TwinkleForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect("dashboard-twinkle")
    else:
        form = TwinkleForm(instance=item)
    context = {
        "form": form
    }
    return render(request, 'dashboard/twinkle_update.html', context)


@login_required(login_url='user-login')
def targets(request):
    item_list = AnnualTarget.objects.all().order_by('year')
    if request.method == "POST":
        form = AnnualTargetForm(request.POST)
        if form.is_valid():
            form.save()
            # month_name = form.cleaned_data.get('month')
            year_name = form.cleaned_data.get('year')
            messages.success(request, f"{year_name} target has been added")
            return redirect('dashboard-target')
    else:
        form = AnnualTargetForm()
    items = pagination_(request, item_list)

    context = {
        'form': form,
        "items": items,
    }
    return render(request, "dashboard/target.html", context)


@login_required(login_url='user-login')
def target_update(request, pk):
    item = AnnualTarget.objects.get(id=pk)
    if request.method == "POST":
        form = AnnualTargetForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect("dashboard-target")
    else:
        form = AnnualTargetForm(instance=item)
    context = {
        "form": form
    }
    return render(request, 'dashboard/target_update.html', context)


@login_required(login_url='user-login')
def target_delete(request, pk):
    item = AnnualTarget.objects.get(id=pk)
    if request.method == "POST":
        item.delete()
        return redirect("dashboard-target")
    context = {
        "items": item
    }
    return render(request, 'dashboard/target_delete.html', context)
