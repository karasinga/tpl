import calendar
# from functools import lru_cache
from datetime import datetime
import math

import pandas as pd

import plotly.graph_objects as go
# from pandas._libs.tslibs.offsets import MonthEnd
from pandas.tseries.offsets import MonthEnd
from plotly.offline import plot
import plotly.express as px
from plotly.subplots import make_subplots

from .models import Sales, WeeklyData, AnnualTarget,MonthlyTargets,Twinkle,SummaryTable,Stock,Expiry

import cProfile, pstats, io


def profile(fnc):
    """A decorator that uses cProfile to profile a function"""

    def inner(*args, **kwargs):
        pr = cProfile.Profile()
        pr.enable()
        retval = fnc(*args, **kwargs)
        pr.disable()
        s = io.StringIO()
        sortby = 'cumulative'
        ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
        ps.print_stats()
        print(s.getvalue())
        return retval

    return inner



def millify(n):
    millnames = ['', ' K', ' M', ' Billion', ' Trillion']
    n = float(n)
    millidx = max(0, min(len(millnames) - 1,
                         int(math.floor(0 if n == 0 else math.log10(abs(n)) / 3))))

    return '{:.2f}{}'.format(n / 10 ** (3 * millidx), millnames[millidx])



def line_chart_target(df, x_axis, yaxis, title,color="year"):
    lab_per_fig = px.line(df, x=x_axis, y=yaxis, color=color,
                          title=title, text=yaxis,
                          # text_auto='.3s',
                          category_orders={"month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                                                     "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]}
                          )
    lab_per_fig.add_hline(y=30, line_dash="dash", line_color="red")
    lab_per_fig.add_annotation(x=0.5, y=30,
                       text="Target 30%",
                       showarrow=True,
                       arrowhead=1)
    lab_per_fig.update_layout(height=500)
    lab_per_fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1
    ))
    lab_per_fig.update_traces(textposition='top center')
    lab_per_fig.update_xaxes(showgrid=False)
    lab_per_fig.update_yaxes(showgrid=False)
    lab_per_fig.layout.xaxis.fixedrange = True
    lab_per_fig.layout.yaxis.fixedrange = True
    lab_per_fig.update_layout({
        'plot_bgcolor': 'rgba(0, 0, 0, 0)',
        'paper_bgcolor': 'rgba(0, 0, 0, 0)',
    })
    return lab_per_fig

def line_chart_stock_target(df, x_axis, yaxis,text, title,color="year"):
    lab_per_fig = px.line(df, x=x_axis, y=yaxis, color=color,
                          title=title, text=text,
                          # text_auto='.3s',
                          category_orders={"month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                                                     "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]}
                          )
    lab_per_fig.add_hline(y=1500000, line_dash="dash", line_color="green")
    lab_per_fig.add_hline(y=1700000, line_dash="dash", line_color="red")
    lab_per_fig.add_annotation(x=0.5, y=1500000,
                       text="Minimum Target (1.5M)",
                       showarrow=True,
                       arrowhead=1)
    lab_per_fig.add_annotation(x=1.5, y=1700000,
                               text="Maximum Target (1.7M)",
                               showarrow=True,
                               arrowhead=1)
    lab_per_fig.update_layout(height=500)
    lab_per_fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1
    ))
    lab_per_fig.update_traces(textposition='top center')
    lab_per_fig.update_xaxes(showgrid=False)
    lab_per_fig.update_yaxes(showgrid=False)
    lab_per_fig.layout.xaxis.fixedrange = True
    lab_per_fig.layout.yaxis.fixedrange = True
    lab_per_fig.update_layout({
        'plot_bgcolor': 'rgba(0, 0, 0, 0)',
        'paper_bgcolor': 'rgba(0, 0, 0, 0)',
    })
    return lab_per_fig


def line_chart(df, x_axis, yaxis, title, color="year"):
    lab_per_fig = px.line(df, x=x_axis, y=yaxis, color=color,
                          title=title, text=yaxis,
                          # text_auto='.3s',
                          category_orders={"month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                                                     "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]}
                          )
    lab_per_fig.update_layout(height=500)
    lab_per_fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1
    ))
    lab_per_fig.update_traces(textposition='top center')
    lab_per_fig.update_xaxes(showgrid=False)
    lab_per_fig.update_yaxes(showgrid=False)
    lab_per_fig.layout.xaxis.fixedrange = True
    lab_per_fig.layout.yaxis.fixedrange = True
    lab_per_fig.update_layout({
        'plot_bgcolor': 'rgba(0, 0, 0, 0)',
        'paper_bgcolor': 'rgba(0, 0, 0, 0)',
    })
    return lab_per_fig

def line_chart_expiry(df, x_axis, yaxis, text,title, color="year"):
    lab_per_fig = px.line(df, x=x_axis, y=yaxis, color=color,
                          title=title, text=text,
                          # text_auto='.3s',
                          category_orders={"month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                                                     "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]}
                          )
    lab_per_fig.update_layout(height=500)
    lab_per_fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1
    ))
    lab_per_fig.update_traces(textposition='top center')
    lab_per_fig.update_xaxes(showgrid=False)
    lab_per_fig.update_yaxes(showgrid=False)
    lab_per_fig.layout.xaxis.fixedrange = True
    lab_per_fig.layout.yaxis.fixedrange = True
    lab_per_fig.update_layout({
        'plot_bgcolor': 'rgba(0, 0, 0, 0)',
        'paper_bgcolor': 'rgba(0, 0, 0, 0)',
    })
    return lab_per_fig


def line_chart_summary(df, x_axis, yaxis, title, color="year"):
    lab_per_fig = px.line(df, x=x_axis, y=yaxis, color=color,
                          title=title, text=yaxis,
                          # text_auto='.3s',
                          category_orders={"month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                                                     "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]},
                            hover_name = x_axis, hover_data = {'sales': True,
                                                              "cost_of_sales": True,
                                                              "gross_profit": True,
                                                              "gross_profit %": True,
                                                              "expenses": True,
                                                              "net_profit": True,
                                                               }
                          )
    lab_per_fig.update_layout(height=500)
    lab_per_fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1
    ))
    lab_per_fig.update_traces(textposition='top center')
    lab_per_fig.update_xaxes(showgrid=False)
    lab_per_fig.update_yaxes(showgrid=False)
    lab_per_fig.layout.xaxis.fixedrange = True
    lab_per_fig.layout.yaxis.fixedrange = True
    lab_per_fig.update_layout({
        'plot_bgcolor': 'rgba(0, 0, 0, 0)',
        'paper_bgcolor': 'rgba(0, 0, 0, 0)',
    })
    return lab_per_fig


def bar_chart(df, x_axis, yaxis, title, color="year"):
    sales_fig = px.bar(df, x=x_axis, y=yaxis, color=color, barmode="group",
                       title=title, text="value",
                       # category_orders={"month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                       #                            "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]}
                       )
    sales_fig.update_layout(height=500)
    sales_fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1
    ))
    sales_fig.update_xaxes(showgrid=False)
    sales_fig.update_yaxes(showgrid=False)
    sales_fig.layout.xaxis.fixedrange = True
    sales_fig.layout.yaxis.fixedrange = True
    sales_fig.update_layout({
        'plot_bgcolor': 'rgba(0, 0, 0, 0)',
        'paper_bgcolor': 'rgba(0, 0, 0, 0)',
    })
    return sales_fig


def sales_trend(df, indy1, indy2, indy3, indy4, indy5, indy6, title_text):
    df['year'] = df['year'].astype(str)
    # df = df.sort_values(by='month_date')
    # Create figure with secondary y-axis
    fig = make_subplots(specs=[[{"secondary_y": True}]])

    # Add traces
    fig.add_trace(
        go.Bar(x=df[indy6],
               y=df[indy1], name=indy1, text=df[indy1], textposition='outside',
               textfont_size=12), secondary_y=False, )
    fig.add_trace(
        go.Bar(x=df[indy6],
               y=df[indy2], name=indy2,
               text=df[indy2], textposition='outside', textfont_size=12),
        secondary_y=False,
    )
    fig.add_trace(
        go.Bar(x=df[indy6],
               y=df[indy3], name=indy3,
               text=df[indy3], textposition='outside', textfont_size=12),
        secondary_y=False,
    )

    fig.add_trace(
        go.Bar(x=df[indy6],
               y=df[indy4], name=indy4,
               text=df[indy4], textposition='outside', textfont_size=12),
        secondary_y=False,
    )

    fig.add_trace(
        go.Scatter(x=df[indy6],
                   y=df[indy5], name=indy5, text=df[indy5], textposition='top center', mode="lines+markers+text",
                   textfont_size=12, textfont=dict(
                family="sans serif",
                size=20,
                color="Brown")
                   ),
        secondary_y=True,  # this ensures secondary data is visible
    )

    #     Add figure title
    fig.update_layout(title_text=title_text
                      )
    fig.update_traces(texttemplate='%{text:.3s}')
    fig.update_layout(height=550, title_font={"size": 24}, font={"size": 16},
                      margin=dict(
                          l=50,
                          r=50,
                          b=100,
                          t=100,
                          pad=4))
    fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1
    ))
    # Set x-axis title
    fig.update_xaxes(title_text="<b>Period (in Years)</b>")
    # remove grid lines
    fig.update_yaxes(showgrid=False)
    fig.update_xaxes(showgrid=False)
    fig.layout.xaxis.fixedrange = True
    fig.layout.yaxis.fixedrange = True
    fig.update_layout({
        'plot_bgcolor': 'rgba(0, 0, 0, 0)',
        'paper_bgcolor': 'rgba(0, 0, 0, 0)',
    })

    # Set y-axes titles
    fig.update_yaxes(title_text="<b>Performance</b> ", secondary_y=False)
    # fig.update_yaxes(title_text=f"<b>{indy3} %</b>", rangemode='nonnegative', secondary_y=True)
    fig.update_layout(uniformtext_minsize=14, uniformtext_mode='hide')

    fig.update_layout(uniformtext_minsize=9, uniformtext_mode='hide')

    return fig




# @lru_cache(maxsize=1)
def dash():
    qs = Sales.objects.all()
    ts = AnnualTarget.objects.all()
    wk = WeeklyData.objects.all()
    mt = MonthlyTargets.objects.all()
    tw = Twinkle.objects.all()
    st = SummaryTable.objects.all()
    end_st = Stock.objects.all()
    ex = Expiry.objects.all()
    # assign it to a dataframe using list comprehension
    sales_data = [
        {'year': x.year,
         'month': x.month,
         'sales': x.sales,
         'lab_contribution': x.lab_contribution,
         'pharmacy_contribution': x.pharmacy_contribution,
         } for x in qs
    ]

    target_data = [
        {'year': x.year,
         'target': x.target,
         } for x in ts
    ]

    weekly_data = [
        {'end of weekly date': x.end_date,
         'amount_received': x.amount_received,
         'amount_referred': x.amount_referred,
         'balance': x.balance,
         } for x in wk
    ]
    monthly_target_data = [
        {'year': x.year,
         'month': x.month,
         'lab monthly target': x.lab_target,
         'pharmacy monthly target': x.pharma_target
         } for x in mt
    ]
    twinkle_data = [
        {'year': x.year,
         'month': x.month,
         'amount_received': x.amount_to_twinkle,
         'amount_to_metro': x.amount_to_metropolis_diamond,
         'amount_for_twinkle': x.amount_for_twinkle,
         'commission': x.commission,
         } for x in tw
    ]
    summary_data = [
        {'year': x.year,
         'month': x.month,
         'sales': x.sales,
         'cost_of_sales': x.cost_of_sales,
         'gross_profit': x.gross_profit,
         'expenses': x.expense,
         'net_profit': x.net_profit,
         } for x in st
    ]

    stock_data = [
        {'year': x.year,
         'month': x.month,
         'end_month_stock': x.end_month_stock
         } for x in end_st
    ]
    expiry_data = [
        {'year': x.year,
         'month': x.month,
         'pharmacy_expiries': x.pharmacy_expiries,
         'lab_expiries': x.lab_expiries
         } for x in ex
    ]
    # convert data from database to a dataframe
    df = pd.DataFrame(sales_data)
    df_target = pd.DataFrame(target_data)
    df_weekly = pd.DataFrame(weekly_data)
    df_monthly_target = pd.DataFrame(monthly_target_data)
    twinkle_df = pd.DataFrame(twinkle_data)
    summary_table_df = pd.DataFrame(summary_data)
    stock_df = pd.DataFrame(stock_data)
    expiry_df = pd.DataFrame(expiry_data)

    # summary table
    summary_table_df['month'] = summary_table_df['month'].apply(lambda x: calendar.month_abbr[int(x)])
    summary_table_df['gross_profit %'] = round((summary_table_df['gross_profit']/summary_table_df['sales'])*100,1)
    # print("summary_table_df...")
    # print(summary_table_df.head(18))
    currentYear = datetime.now().year

    summary_current_year=summary_table_df[summary_table_df['year']==currentYear]
    summary_previous_year=summary_table_df[summary_table_df['year']==currentYear-1]

    # current_year_sales=bar_chart(summary_current_year, "month", 'sales', "title")
    # summary_table_df['net_profit_'] = summary_table_df['net_profit'].apply(millify)

    summary_table_df.loc[:, 'month'] = pd.Categorical(summary_table_df['month'],
                                        categories=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep',
                                                    'Oct', 'Nov', 'Dec'],
                                        ordered=True)
    summary_table_df.sort_values('month', inplace=True)

    summary_table_fig_expenses = line_chart_summary(summary_table_df, 'month', 'expenses', "EXPENSES TREND")
    summary_table_fig_net = line_chart_summary(summary_table_df, 'month', 'net_profit', "NET PROFIT TREND")
    summary_table_fig_gross = line_chart_target(summary_table_df, 'month', 'gross_profit %', "GROSS PROFIT TREND")
    summary_table_cos = line_chart_summary(summary_table_df, 'month', 'cost_of_sales', "COST OF SALES TREND")



    # print("+++++++++++++++++++++++")
    # print(summary_current_year)
    stock_df['month'] = stock_df['month'].apply(lambda x: calendar.month_abbr[int(x)])
    stock_df['end_month_stock.'] = stock_df['end_month_stock'].apply(millify)

    stock_fig = line_chart_stock_target(stock_df, 'month', 'end_month_stock','end_month_stock.', "END OF MONTH STOCK VALUATION TREND")

    expiry_df['month'] = expiry_df['month'].apply(lambda x: calendar.month_abbr[int(x)])
    # expiry_df['pharmacy_expiries.'] = expiry_df['pharmacy_expiries'].apply(millify)
    # expiry_df['lab_expiries.'] = expiry_df['lab_expiries'].apply(millify)
    # expiry_df=expiry_df.melt(id_vars=['year','month'],value_vars=['pharmacy_expiries','lab_expiries'])
    # pharmacy_expiries=expiry_df[expiry_df['variable']=="pharmacy_expiries"]
    # lab_expiries=expiry_df[expiry_df['variable']=="lab_expiries"]
    # print(expiry_df)
    # print(pharmacy_expiries)
    pharm_expiry_fig=line_chart_expiry(expiry_df, 'month', 'pharmacy_expiries', 'pharmacy_expiries', "PHARMACY LOSSES THROUGH EXPIRIES")
    lab_expiry_fig=line_chart_expiry(expiry_df, 'month', 'lab_expiries', 'lab_expiries', "LABORATORY LOSSES THROUGH EXPIRIES")
    # expiry_fig = line_chart_stock_target(expiry_df, 'month', ['pharmacy_expiries','lab_expiries'], 'value',
    #                                     "END OF MONTH STOCK VALUATION TREND")
    # print(summary_previous_year)
    def trend(summary_current_year,currentYear,y=["sales",'cost_of_sales','gross_profit'],trend=""):
        trend_fig = px.bar(summary_current_year, x="month", y=y,barmode='group',
                           title=f"{currentYear} {trend} TREND",
                           text_auto='.3s',
                           category_orders={"month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                                                      "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]})
        trend_fig.update_layout(height=500)
        trend_fig.update_xaxes(showgrid=False)
        trend_fig.update_yaxes(showgrid=False)
        trend_fig.layout.xaxis.fixedrange = True
        trend_fig.layout.yaxis.fixedrange = True
        trend_fig.update_layout({
            'plot_bgcolor': 'rgba(0, 0, 0, 0)',
            'paper_bgcolor': 'rgba(0, 0, 0, 0)',
        })
        trend_fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ))
        return trend_fig

    trend_fig=trend(summary_current_year, currentYear)
    trend_fig_previous=trend(summary_previous_year, currentYear-1)
    trend_fig_previous_prev=trend(summary_previous_year, currentYear-1,y=['gross_profit','expenses','net_profit'],
                                  trend="OVERALL GROSS PROFIT VS EXPENSES VS NET PROFIT")
    trend_fig_expenses_curr=trend(summary_current_year, currentYear,y=['gross_profit','expenses','net_profit']
                                  ,trend="OVERALL GROSS PROFIT VS EXPENSES VS NET PROFIT")


    # Merge sales and monthly targets tables
    df_monthly_merged=df.merge(df_monthly_target, on=["year","month"])
    twinkle_df['tpl_revenue %']=round((twinkle_df['amount_for_twinkle']/twinkle_df['amount_received'])*100,1)
    twinkle_df['revenue outside %']=round((twinkle_df['amount_to_metro']/twinkle_df['amount_received'])*100,1)
    twinkle_df['month'] = twinkle_df['month'].apply(lambda x: calendar.month_abbr[int(x)])
    tpl_fig = line_chart(twinkle_df, "month", 'tpl_revenue %', 'TPL Revenue trend')
    tpl_out_fig = line_chart(twinkle_df, "month", 'revenue outside %', 'Revenue going out trend')

    # print(df)
    # calculate percentage
    df_monthly_merged['lab vs target']=round((df_monthly_merged['lab_contribution']/df_monthly_merged['lab monthly target'])*100,1)
    df_monthly_merged['lab vs target %']=df_monthly_merged['lab vs target'].astype(str)+"%"

    df_monthly_merged['pharm vs target'] = round(
        (df_monthly_merged['pharmacy_contribution'] / df_monthly_merged['pharmacy monthly target']) * 100, 1)
    df_monthly_merged['pharm vs target %'] = df_monthly_merged['pharm vs target'].astype(str) + "%"
    df_monthly_merged['month'] = df_monthly_merged['month'].apply(lambda x: calendar.month_abbr[int(x)])
    # make charts
    monthlytarget_pharm_fig = line_chart(df_monthly_merged, "month", "pharm vs target", 'Pharmacy vs target trend')
    monthlytarget_lab_fig = line_chart(df_monthly_merged, "month", "lab vs target", 'Laboratory vs target trend')





    df = df_target.merge(df, on="year", how='right')
    # print(df)
    df['year'] = df['year'].astype(str)
    df['month'] = df['month'].astype(str)
    df['year_month'] = df['year'] + df['month']
    df['year_month'] = pd.to_datetime(df['year_month'], format='%Y%m', errors='coerce').dropna() + MonthEnd(1)
    df = df.groupby(['year_month', 'year', 'month']).sum()[
        ['sales', 'lab_contribution', 'pharmacy_contribution']].reset_index().sort_values("year_month")
    df_grouped = df.copy()
    df['% of lab contribution'] = round(df['lab_contribution'] / df['sales'] * 100, 1)
    df['% of pharmacy contribution'] = round(df['pharmacy_contribution'] / df['sales'] * 100, 1)
    df_all = df.copy()
    df_target['year'] = df_target['year'].astype(str)
    df_all = df_target.merge(df, on="year", how='right')
    # print("df all-----")
    df_target['year'] = df_target['year'].astype(str).astype(int)
    df_target = df_target.sort_values("year")
    # print(df_all)

    df['month'] = df['month'].apply(lambda x: calendar.month_abbr[int(x)])
    # print(df)
    sales_fig = px.bar(df, x="month", y="sales", color='year', barmode="group",
                       title=f"Sales trend between {df['year'].unique().min()} and {df['year'].unique().max()} ",
                       text_auto='.3s',
                       category_orders={"month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                                                  "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]})
    sales_fig.update_layout(height=500)
    sales_fig.update_xaxes(showgrid=False)
    sales_fig.update_yaxes(showgrid=False)
    sales_fig.layout.xaxis.fixedrange = True
    sales_fig.layout.yaxis.fixedrange = True
    sales_fig.update_layout({
        'plot_bgcolor': 'rgba(0, 0, 0, 0)',
        'paper_bgcolor': 'rgba(0, 0, 0, 0)',
    })
    sales_fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1
    ))

    # df_alls = df.melt(id_vars=['year', 'year_month', 'month'], value_vars=['lab_contribution', 'pharmacy_contribution'])
    df['month_year'] = df['year_month'].dt.strftime('%b-%Y')
    reports_so_far = df.shape[0]
    # print(df)
    last_month_with_data = df['month_year'].iloc[-1]
    current_year_df = df[df['year'] == sorted(df['year'].unique())[-1]]
    current_year_sales = millify(sum(current_year_df['sales']))
    # last_month_with_data=last_month_with_data.strftime('%B-%Y')

    all_fig = px.bar(df, x="month_year", y=['pharmacy_contribution', 'lab_contribution'],
                     title=f"Laboratory and Pharmacy Sales trend   "
                           f"Max Pharmarcy: {max(df['pharmacy_contribution'])}  "
                           f"Max Laboratory: {max(df['lab_contribution'])}",
                     text_auto='.3s')
    all_fig.update_layout(height=500)
    all_fig.update_xaxes(showgrid=False)
    all_fig.update_yaxes(showgrid=False)
    all_fig.layout.xaxis.fixedrange = True
    all_fig.layout.yaxis.fixedrange = True
    all_fig.update_layout({
        'plot_bgcolor': 'rgba(0, 0, 0, 0)',
        'paper_bgcolor': 'rgba(0, 0, 0, 0)',
    })
    all_fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1
    ))
    lab_per_fig = line_chart(df, "month", "% of lab contribution", '% of lab contribution')
    pharm_per_fig = line_chart(df, "month", "% of pharmacy contribution", '% of pharmacy contribution')

    years_list = []
    lab_contr_list = []
    phar_contr_list = []

    total_labs = []
    total_phars = []
    annual_targets = []
    annual_performance = []
    annual_sales = []

    for i in df_all['year'].unique():
        a = df_all[df_all['year'] == f"{i}"]
        total_sales = sum(a['sales'])
        total_phar = sum(a['pharmacy_contribution'])
        total_lab = sum(a['lab_contribution'])
        annual_target = max(a['target'])
        annual_targets.append(annual_target)
        annual_sales.append(total_sales)
        annual_performance.append(round(total_sales / annual_target * 100, ))

        total_labs.append(total_lab)
        total_phars.append(total_phar)
        years_list.append(i)
        lab_contr_list.append(round(total_lab / total_sales * 100, 1))
        phar_contr_list.append(round(total_phar / total_sales * 100, 1))

    # MAKE A DF
    percentile_list_df = pd.DataFrame(
        {'year': years_list,

         'lab contribution': lab_contr_list,
         'pharmacy contribution': phar_contr_list
         })
    # print("percentile_list_df")
    # print(percentile_list_df)
    percentile_list_df = percentile_list_df.melt(id_vars='year',
                                                 value_vars=['pharmacy contribution', 'lab contribution'])
    percentile_list_df["%"] = percentile_list_df['value'].astype(str) + "%"
    # print(percentile_list_df)

    contrib_fig = px.bar(percentile_list_df, x="year", y="value", text='%', barmode="group",
                         color="variable", title=f"Annual contribution of Laboratory and Pharmacy Sales")
    contrib_fig.update_layout(height=500)
    contrib_fig.update_xaxes(showgrid=False)
    contrib_fig.update_yaxes(showgrid=False)
    contrib_fig.layout.xaxis.fixedrange = True
    contrib_fig.layout.yaxis.fixedrange = True
    contrib_fig.update_layout({
        'plot_bgcolor': 'rgba(0, 0, 0, 0)',
        'paper_bgcolor': 'rgba(0, 0, 0, 0)',
    })
    contrib_fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1
    ))

    # MAKE A DF
    total_sales_df = pd.DataFrame(
        {'year': years_list,
         'target': annual_targets,
         'annual performance %': annual_performance,
         'sales': annual_sales,
         'total Lab sales': total_labs,
         'total pharmacy sales': total_phars
         })
    # total_sales_df['annual performance %']=total_sales_df['annual performance'].astype(str)+"%"
    # total_sales_df = total_sales_df.melt(id_vars='year', value_vars=['target','annual performance','total pharmacy sales', 'total Lab sales'])
    # print("total sales")
    # print(total_sales_df.dtypes)
    total_sales_df['year'] = total_sales_df['year'].astype(str).astype(int)
    total_sales_df = total_sales_df.sort_values("year")
    perfomance_so_far = total_sales_df["annual performance %"].iloc[-1]
    total_sales_fig = sales_trend(total_sales_df, 'target', 'sales', 'total pharmacy sales', 'total Lab sales',
                                  'annual performance %', 'year', 'Annual Performance')
    # total_sales_fig = px.bar(total_sales_df, x="year", y="value", text_auto=".3s", barmode="group",
    #                          color="variable", title=f"Annual contribution of Laboratory and Pharmacy Sales")
    # total_sales_fig.update_layout(height=500)
    # total_sales_fig.update_layout(legend=dict(
    #     orientation="h",
    #     yanchor="bottom",
    #     y=1.02,
    #     xanchor="right",
    #     x=1
    # ))
    # total_sales_df=total_sales_df.melt(id_vars='year', value_vars=['total Lab sales', 'total pharmacy sales'])
    # total_sales_df["%"]=round(total_sales_df['value']/sum(total_sales_df['value'])*100,)

    # get the current year
    current_year = total_sales_df.iloc[[-1]]
    current_year = current_year.copy()
    current_year['deficit'] = current_year['target'] - current_year['sales']
    current_year['current month name'] = datetime.now().month
    current_year['current month name'] = datetime.now().month
    last_report = df_all.iloc[[-1]].copy()
    last_report['last report'] = last_report['year_month'].dt.month
    current_year['remaining months'] = 12 - last_report.iloc[0, -1]
    current_year['deficit per months'] = current_year['deficit'] / current_year['remaining months']
    last_report_month = last_report.iloc[0, -1]
    overall_deficit = current_year['deficit per months'].iloc[0]

    # print(current_year)

    def moving_target(last_report_month, deficit):
        months_to_go = range(last_report_month + 1, 13)
        months = [calendar.month_name[int(m)] for m in months_to_go]
        moving_target_df = pd.DataFrame({'months': months, 'deficit': deficit})
        fig = px.line(moving_target_df, x="months", y="deficit", text='deficit',
                      title="Remaining months target")
        fig.update_traces(textposition='top center')
        fig.update_xaxes(showgrid=False)
        fig.update_yaxes(showgrid=False)
        fig.update_layout({
            'plot_bgcolor': 'rgba(0, 0, 0, 0)',
            'paper_bgcolor': 'rgba(0, 0, 0, 0)',
        })
        fig.update_traces(texttemplate='%{text:.4s}')
        return fig

    moving_target_fig = moving_target(last_report_month, overall_deficit)
    monthly_target = millify(overall_deficit)
    sales_plot = plot(sales_fig, include_plotlyjs=False, output_type="div")
    all_plot = plot(all_fig, include_plotlyjs=False, output_type="div")
    lab_plot = plot(lab_per_fig, include_plotlyjs=False, output_type="div")
    phar_plot = plot(pharm_per_fig, include_plotlyjs=False, output_type="div")
    contr_plot = plot(contrib_fig, include_plotlyjs=False, output_type="div")
    total_sales_plot = plot(total_sales_fig, include_plotlyjs=False, output_type="div")
    moving_target_plot = plot(moving_target_fig, include_plotlyjs=False, output_type="div")
    monthlytarget_pharm_plot = plot(monthlytarget_pharm_fig, include_plotlyjs=False, output_type="div")
    monthlytarget_lab_plot = plot(monthlytarget_lab_fig, include_plotlyjs=False, output_type="div")
    tpl_plot = plot(tpl_fig, include_plotlyjs=False, output_type="div")
    tpl_out_plot = plot(tpl_out_fig, include_plotlyjs=False, output_type="div")
    summary_table_plot = plot(summary_table_fig_expenses, include_plotlyjs=False, output_type="div")
    summary_net_plot = plot(summary_table_fig_net, include_plotlyjs=False, output_type="div")
    summary_gross_plot = plot(summary_table_fig_gross, include_plotlyjs=False, output_type="div")
    summary_table_cos_plot = plot(summary_table_cos, include_plotlyjs=False, output_type="div")
    current_year_trend_plot = plot(trend_fig, include_plotlyjs=False, output_type="div")
    previous_year_trend_plot = plot(trend_fig_previous, include_plotlyjs=False, output_type="div")
    previous_year_trend_fig_expenses_plot = plot(trend_fig_previous_prev, include_plotlyjs=False, output_type="div")
    current_year_trend_fig_expenses_plot = plot(trend_fig_expenses_curr, include_plotlyjs=False, output_type="div")
    stock_plot = plot(stock_fig, include_plotlyjs=False, output_type="div")
    pharm_expiry_fig = plot(pharm_expiry_fig, include_plotlyjs=False, output_type="div")
    lab_expiry_fig = plot(lab_expiry_fig, include_plotlyjs=False, output_type="div")

    # print("monthly_target...")
    # print(monthly_target)



    return monthly_target, sales_plot, all_plot, lab_plot, phar_plot, contr_plot, total_sales_plot, moving_target_plot, \
           perfomance_so_far, last_month_with_data, reports_so_far, current_year_sales, monthly_target,twinkle_df,\
           monthlytarget_pharm_plot,monthlytarget_lab_plot,tpl_plot,tpl_out_plot,summary_table_plot,summary_net_plot,\
           summary_gross_plot,summary_table_cos_plot,current_year_trend_plot,stock_plot,pharm_expiry_fig,lab_expiry_fig,\
           previous_year_trend_plot,current_year_trend_fig_expenses_plot,previous_year_trend_fig_expenses_plot





# dash()