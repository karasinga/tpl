from datetime import datetime

from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit,Layout,Row,Column
from crispy_forms.bootstrap import InlineField
from django import forms

from .models import Sales, WeeklyData, Twinkle, AnnualTarget, MonthlyTargets, SummaryTable, Stock, Expiry


class SalesForm(ModelForm):
    class Meta:
        model = Sales
        fields = '__all__'
        # fields = {
        #     'year': ['exact'],
        #     'month': ['exact'],
        #     'sales': ['lte','gte'],
        # }

        # exclude = ['pharmacy_contribution','lab_contribution']

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args,**kwargs)
    #     self.helper=FormHelper(self)
    #     self.helper.form_method="get"
    #     self.helper.add_input(Submit("Search","search", css_class='btn btn-success'))
    #     self.helper.layout = Layout(
    #         # InlineField('email', readonly=True),
    #         # 'password',
    #         Row(
    #             Column('year', css_class='form-group col-md-2 mb-0'),
    #             Column('month', css_class='form-group col-md-2 mb-0'),
    #             Column('sales', css_class='form-group col-md-2 mb-0'),
    #             css_class='form-row'
    #         ))


class WeeklyDataForm(ModelForm):
    class Meta:
        model = WeeklyData
        fields = '__all__'
        widgets = {
            'start_date': forms.DateInput(format=('%Y-%m-%d'),
                                          attrs={'class': 'form-control', 'placeholder': 'Select Date',
                                                 'type': 'date','max':datetime.now().date}),
            'end_date': forms.DateInput(format=('%Y-%m-%d'),
                                        attrs={'class': 'form-control', 'placeholder': 'Select Date', 'type': 'date',
                                               'max':datetime.now().date
                                               }
                                        )
        }


class TwinkleForm(ModelForm):
    class Meta:
        model = Twinkle
        fields = "__all__"


class AnnualTargetForm(ModelForm):
    class Meta:
        model = AnnualTarget
        fields = "__all__"

class MonthlyTargetsForm(ModelForm):
    class Meta:
        model = MonthlyTargets
        fields = "__all__"

class SummaryForm(ModelForm):
    class Meta:
        model = SummaryTable
        fields = "__all__"
        exclude = ['sales']

    # def __init__(self, *args, **kwargs):
    #     super(SummaryForm, self).__init__(*args, **kwargs)
    #     cur_jobs = Sales.objects.filter()
    #
    #     all_colors = Color.objects.all()
    #     cur_colors = []
    #     for i in cur_jobs:
    #         cur_colors.append(i.color)
    #     aval_colors = [x for x in all_colors if x not in cur_colors]
    #     choice = random.choice(aval_colors)
    #     self.fields['color'].initial = choice

class StockForm(ModelForm):
    class Meta:
        model = Stock
        fields = "__all__"

class ExpiryForm(ModelForm):
    class Meta:
        model = Expiry
        fields = "__all__"


