from django import forms
from .models import *




class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['customer_name', 'customer_phone', 'customer_address', 'customer_id_number', 'initial_balance_debit', 'initial_balance_type', 'agreement']
        widgets = {
            'customer_name': forms.TextInput(attrs={'class':'form-control', 'id':'customer_name'}),
            'customer_phone': forms.TextInput(attrs={'class':'form-control', 'id':'customer_phone'}),
            'customer_address': forms.TextInput(attrs={'class':'form-control', 'id':'customer_address'}),
            'customer_id_number': forms.TextInput(attrs={'class':'form-control', 'id':'customer_id_number'}),
            'initial_balance_debit': forms.NumberInput(attrs={'class':'form-control', 'min':0, 'id':'initial_balance_debit'}),
            'initial_balance_type': forms.Select(attrs={'class':'form-control', 'id': 'initial_balance_type'}),
            'agreement': forms.TextInput(attrs={'class':'form-control', 'id':'agreement'}),
        }


class CustomerFormUpdate(forms.ModelForm):
    class Meta:
        model = Customer
        exclude = ['deleted', 'initial_balance_debit', 'initial_balance_type']
        widgets = {
            'customer_name': forms.TextInput(attrs={'class':'form-control'}),
            'customer_phone': forms.TextInput(attrs={'class':'form-control'}),
            'customer_address': forms.TextInput(attrs={'class':'form-control'}),
            'customer_id_number': forms.TextInput(attrs={'class':'form-control'}),
            'agreement': forms.TextInput(attrs={'class':'form-control'}),
        }



class CustomerDeleteForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['customer_name']