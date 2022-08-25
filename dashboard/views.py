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
from .forms import SalesForm, WeeklyDataForm, TwinkleForm, AnnualTargetForm, MonthlyTargetsForm, SummaryForm, StockForm, \
    ExpiryForm
from .models import Sales, WeeklyData, Twinkle, AnnualTarget, MonthlyTargets, SummaryTable, Stock, Expiry
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
monthly_target, sales_plot, all_plot, lab_plot, phar_plot, contr_plot, total_sales_plot, moving_target_plot, \
perfomance_so_far, last_month_with_data, reports_so_far, current_year_sales, monthly_target,\
twinkle_df,monthlytarget_pharm_plot,monthlytarget_lab_plot,tpl_fig,tpl_out_plot,summary_table_plot,\
summary_net_plot,summary_gross_plot,summary_table_cos_plot,current_year_trend_plot,stock_plot,pharm_expiry_fig,\
lab_expiry_fig,previous_year_trend_plot = dash()

@login_required(login_url='user-login')
def index(request):
    # monthly_target, sales_plot, all_plot, lab_plot, phar_plot, contr_plot, total_sales_plot, moving_target_plot, \
    # perfomance_so_far, last_month_with_data, reports_so_far, current_year_sales, monthly_target,\
    # twinkle_df,monthlytarget_pharm_plot,monthlytarget_lab_plot,tpl_fig,tpl_out_plot,summary_table_plot,\
    # summary_net_plot,summary_gross_plot,summary_table_cos_plot,current_year_trend_plot = dash()

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
        "current_year_trend_plot":current_year_trend_plot,
        "previous_year_trend_plot":previous_year_trend_plot,
        "stock_plot":stock_plot,


    }
    return render(request, "dashboard/index.html", context)



@login_required(login_url='user-login')
def contribution(request):
    # monthly_target, sales_plot, all_plot, lab_plot, phar_plot, contr_plot, total_sales_plot, moving_target_plot, \
    # perfomance_so_far, last_month_with_data, reports_so_far, current_year_sales, monthly_target,twinkle_df,\
    # monthlytarget_pharm_plot,monthlytarget_lab_plot,tpl_fig,tpl_out_plot,summary_table_plot,summary_net_plot,\
    # summary_gross_plot,summary_table_cos_plot,current_year_trend_plot= dash()

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
def against_target(request):
    # monthly_target, sales_plot, all_plot, lab_plot, phar_plot, contr_plot, total_sales_plot, moving_target_plot, \
    # perfomance_so_far, last_month_with_data, reports_so_far, current_year_sales, monthly_target,twinkle_df,\
    # monthlytarget_pharm_plot,monthlytarget_lab_plot,tpl_plot,tpl_out_plot,summary_table_plot,summary_net_plot,\
    # summary_gross_plot,summary_table_cos_plot,current_year_trend_plot= dash()

    context = {
        "perfomance_so_far": perfomance_so_far,
        "last_month_with_data": last_month_with_data,
        "reports_so_far": reports_so_far,
        "current_year_sales": current_year_sales,

        "monthly_target_pharm":monthlytarget_pharm_plot,
        "monthly_target_lab":monthlytarget_lab_plot,

    }
    return render(request, "dashboard/against_target.html", context)



@login_required(login_url='user-login')
def summary_table(request):
    # monthly_target, sales_plot, all_plot, lab_plot, phar_plot, contr_plot, total_sales_plot, moving_target_plot, \
    # perfomance_so_far, last_month_with_data, reports_so_far, current_year_sales, monthly_target,twinkle_df,\
    # monthlytarget_pharm_plot,monthlytarget_lab_plot,tpl_plot,tpl_out_plot,summary_table_plot,summary_net_plot,\
    # summary_gross_plot,summary_table_cos_plot,current_year_trend_plot= dash()

    context = {
        "perfomance_so_far": perfomance_so_far,
        "last_month_with_data": last_month_with_data,
        "reports_so_far": reports_so_far,
        "current_year_sales": current_year_sales,

        "summary_table_plot":summary_table_plot,
        "summary_net_plot":summary_net_plot,
        "summary_gross_plot":summary_gross_plot,
        "summary_table_cos_plot":summary_table_cos_plot,
        "pharm_expiry_fig":pharm_expiry_fig,
        "lab_expiry_fig":lab_expiry_fig,

    }
    return render(request, "dashboard/summary_table.html", context)


@login_required(login_url='user-login')
def revenue(request):
    monthly_target, sales_plot, all_plot, lab_plot, phar_plot, contr_plot, total_sales_plot, moving_target_plot, \
    perfomance_so_far, last_month_with_data, reports_so_far, current_year_sales, monthly_target,twinkle_df,\
    monthlytarget_pharm_plot,monthlytarget_lab_plot,tpl_plot,tpl_out_plot,summary_table_plot,summary_net_plot,\
    summary_gross_plot,summary_table_cos_plot,current_year_trend_plot,stock_plot,pharm_expiry_fig,lab_expiry_fig,\
    previous_year_trend_plot= dash()

    context = {
        "perfomance_so_far": perfomance_so_far,
        "last_month_with_data": last_month_with_data,
        "reports_so_far": reports_so_far,
        "current_year_sales": current_year_sales,

        "tpl_fig":tpl_plot,
        "tpl_out_plot":tpl_out_plot,

    }
    return render(request, "dashboard/tpl_revenue.html", context)


@login_required(login_url='user-login')
def annual_performance(request):

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

@login_required(login_url='user-login')
def monthlytargets(request):
    item_list = MonthlyTargets.objects.all().order_by('year')
    if request.method == "POST":
        form = MonthlyTargetsForm(request.POST)
        if form.is_valid():
            form.save()
            # month_name = form.cleaned_data.get('month')
            year_name = form.cleaned_data.get('year')
            month_name = form.cleaned_data.get('month')
            # print(type(month_name))
            messages.success(request, f"{calendar.month_name[int(month_name)]} {year_name} targets have been added")
            return redirect('dashboard-monthly-targets')
    else:
        form = MonthlyTargetsForm()
    items = pagination_(request, item_list)

    context = {
        'form': form,
        "items": items,
    }
    return render(request, "dashboard/monthly_target.html", context)

@login_required(login_url='user-login')
def monthly_target_delete(request, pk):
    item = MonthlyTargets.objects.get(id=pk)
    if request.method == "POST":
        item.delete()
        return redirect("dashboard-monthly-targets")
    context = {
        "items": item
    }
    return render(request, 'dashboard/monthly_target_delete.html', context)

@login_required(login_url='user-login')
def monthly_target_update(request, pk):
    item = MonthlyTargets.objects.get(id=pk)
    if request.method == "POST":
        form = MonthlyTargetsForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect("dashboard-monthly-targets")
    else:
        form = MonthlyTargetsForm(instance=item)
    context = {
        "form": form
    }
    return render(request, 'dashboard/monthly_target_update.html', context)

@login_required(login_url='user-login')
def summary(request):
    item_list = SummaryTable.objects.all().order_by('year')
    if request.method == "POST":
        form = SummaryForm(request.POST)
        if form.is_valid():
            form.save()
            # month_name = form.cleaned_data.get('month')
            year_name = form.cleaned_data.get('year')
            month_name = form.cleaned_data.get('month')
            # print(type(month_name))
            messages.success(request, f"{calendar.month_name[int(month_name)]} {year_name} data has been added to database")
            return redirect('dashboard-summary')
    else:
        form = SummaryForm()
    items = pagination_(request, item_list)

    context = {
        'form': form,
        "items": items,
    }
    return render(request, "dashboard/summary.html", context)

@login_required(login_url='user-login')
def summary_delete(request, pk):
    item = SummaryTable.objects.get(id=pk)
    if request.method == "POST":
        item.delete()
        return redirect("dashboard-summary")
    context = {
        "items": item
    }
    return render(request, 'dashboard/summary_delete.html', context)


@login_required(login_url='user-login')
def summary_update(request, pk):
    item = SummaryTable.objects.get(id=pk)
    if request.method == "POST":
        form = SummaryForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect("dashboard-summary")
    else:
        form = SummaryForm(instance=item)
    context = {
        "form": form
    }
    return render(request, 'dashboard/summary_update.html', context)

@login_required(login_url='user-login')
def stocks(request):
    item_list = Stock.objects.all().order_by('year')
    if request.method == "POST":
        form = StockForm(request.POST)
        if form.is_valid():
            form.save()
            # month_name = form.cleaned_data.get('month')
            year_name = form.cleaned_data.get('year')
            month_name = form.cleaned_data.get('month')
            # print(type(month_name))
            messages.success(request, f"{calendar.month_name[int(month_name)]} {year_name} data has been added to database")
            return redirect('dashboard-stock')
    else:
        form = StockForm()
    items = pagination_(request, item_list)

    context = {
        'form': form,
        "items": items,
    }
    return render(request, "dashboard/stock.html", context)

@login_required(login_url='user-login')
def stock_delete(request, pk):
    item = Stock.objects.get(id=pk)
    if request.method == "POST":
        item.delete()
        return redirect("dashboard-stock")
    context = {
        "items": item
    }
    return render(request, 'dashboard/stock_delete.html', context)

@login_required(login_url='user-login')
def stock_update(request, pk):
    item = Stock.objects.get(id=pk)
    if request.method == "POST":
        form = StockForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect("dashboard-stock")
    else:
        form = StockForm(instance=item)
    context = {
        "form": form
    }
    return render(request, 'dashboard/stock_update.html', context)

@login_required(login_url='user-login')
def expiries(request):
    item_list = Expiry.objects.all().order_by('year')
    if request.method == "POST":
        form = ExpiryForm(request.POST)
        if form.is_valid():
            form.save()
            # month_name = form.cleaned_data.get('month')
            year_name = form.cleaned_data.get('year')
            month_name = form.cleaned_data.get('month')
            messages.success(request, f"{calendar.month_name[int(month_name)]} {year_name} data has been added to database")
            return redirect('dashboard-expiry')
    else:
        form = ExpiryForm()
    items = pagination_(request, item_list)

    context = {
        'form': form,
        "items": items,
    }
    return render(request, "dashboard/expiry.html", context)

@login_required(login_url='user-login')
def expiries_delete(request, pk):
    item = Expiry.objects.get(id=pk)
    if request.method == "POST":
        item.delete()
        return redirect("dashboard-expiry")
    context = {
        "items": item
    }
    return render(request, 'dashboard/expiry_delete.html', context)

@login_required(login_url='user-login')
def expiries_update(request, pk):
    item = Expiry.objects.get(id=pk)
    if request.method == "POST":
        form = ExpiryForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect("dashboard-expiry")
    else:
        form = ExpiryForm(instance=item)
    context = {
        "form": form
    }
    return render(request, 'dashboard/expiry_update.html', context)

