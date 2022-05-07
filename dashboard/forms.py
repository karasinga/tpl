from datetime import datetime

from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit,Layout,Row,Column
from crispy_forms.bootstrap import InlineField
from django import forms

from .models import Sales, WeeklyData, Twinkle, AnnualTarget


class SalesForm(ModelForm):
    class Meta:
        model = Sales
        fields = '__all__'
        # fields = {
        #     'year': ['exact'],
        #     'month': ['exact'],
        #     'sales': ['lte','gte'],
        # }

        exclude = ['pharmacy_contribution','lab_contribution']

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
