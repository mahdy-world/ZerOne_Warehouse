from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import *
from django.contrib import messages
# import weasyprint
from django.template.loader import render_to_string
import datetime
from django.db.models.aggregates import Sum
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from .models import Customer
from .forms import *

class CustomerList(LoginRequiredMixin, ListView):
    login_url = '/auth/login/'
    model = Customer
    paginate_by = 12

    def get_queryset(self):
        qureyset = self.model.objects.all().order_by('-id')
        return qureyset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'list'
        context['title'] = 'قائمة العملاء'
        context['page'] = 'active'
        context['count'] = self.model.objects.all().count()
        return context



class CustomerCreate(LoginRequiredMixin, CreateView):
    login_url = '/auth/login/'
    model = Customer
    form_class = CustomerForm
    template_name = 'forms/customer_form_create.html'
    success_url = reverse_lazy('Customer:CustomerList')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'اضافة عميل جديد'
        context['message'] = 'add'
        context['action_url'] = reverse_lazy('Customer:CustomerCreate')
        return context

    def get_success_url(self):
        messages.success(self.request, "تم اضافة عميل جديد", extra_tags="success")

        if self.request.POST.get('url'):
            return self.request.POST.get('url')
        else:
            return self.success_url


class CustomerUpdate(LoginRequiredMixin, UpdateView):
    login_url = '/auth/login/'
    model = Customer
    form_class = CustomerFormUpdate
    template_name = 'forms/seller_product_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'تعديل العميل: ' + str(self.object)
        context['message'] = 'update'
        context['action_url'] = reverse_lazy('Customer:CustomerUpdate', kwargs={'pk': self.object.id})
        return context

    def get_success_url(self):
        messages.success(self.request, "تم تعديل العميل " + str(self.object) + " بنجاح ", extra_tags="success")
        if self.request.POST.get('url'):
            return self.request.POST.get('url')
        else:
            return self.success_url
        
        
class CustomerSuperDelete(LoginRequiredMixin, UpdateView):
    login_url = '/auth/login/'
    model = Customer
    form_class = CustomerDeleteForm
    template_name = 'forms/seller_product_form.html'

    def get_success_url(self):
        return reverse('Customer:CustomerList')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'حذف العميل: ' + str(self.object)
        context['message'] = 'super_delete'
        context['seller_del'] = True
        context['action_url'] = reverse_lazy('Customer:CustomerSuperDelete', kwargs={'pk': self.object.id})
        return context

    def form_valid(self, form):
        messages.success(self.request, " تم حذف العميل " + str(self.object) + " نهائيا بنجاح ", extra_tags="success")
        my_form = Customer.objects.get(id=self.kwargs['pk'])
        my_form.delete()
        return redirect(self.get_success_url())
