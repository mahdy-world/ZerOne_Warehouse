from audioop import reverse
from datetime import timedelta
from dateutil.relativedelta import relativedelta

from django.contrib.auth.decorators import login_required
from django.db.models import Sum, F
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import *
from django.contrib import messages
from Core.forms import ColorForm, SystemInfoForm
from Core.models import SystemInformation
from Core.models import *

from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import SimpleUploadedFile
# Create your views here.


@login_required(login_url='Auth:login')
def Index(request):
    modules = Modules.objects.all().last()
    today = datetime.now().date()
    return render(request, 'core/index.html', {'modules':modules, 'today': today})

class ColorList(LoginRequiredMixin, ListView):
    login_url = '/auth/login/'
    model = Color
    paginate_by = 12
    template_name = 'Core/color_list.html'
    
    def get_queryset(self):
        qureyset = self.model.objects.all().order_by('-id')
        return qureyset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'list'
        context['title'] = 'قائمة الالوان'
        context['icons'] = '<i class="fas fa-shapes"></i>'
        context['page'] = 'active'
        context['count'] = self.model.objects.all().count()
        return context
    
class ColorCreate(LoginRequiredMixin, CreateView):
    login_url = ' /auth/login/'
    model = Color
    template_name = 'forms/form_template.html'
    form_class = ColorForm
    success_url = reverse_lazy('Core:ColorList')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'اضافة لون في النظام'
        context['message'] = 'info'
        context['action_url'] = reverse_lazy('Core:ColorCreate')
        return context
    
    def get_success_url(self):
        messages.success(self.request, "تم إضافة بيانات للنظام بنجاح", extra_tags="success")

        if self.request.POST.get('url'):
            return self.request.POST.get('url')
        else:
            return self.success_url
        
        
class ColorUpdate(LoginRequiredMixin, UpdateView):
    login_url = '/auth/login/'
    model = Color
    form_class = ColorForm
    template_name = 'forms/form_template.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'تعديل اللون: ' + str(self.object)
        context['message'] = 'update'
        context['action_url'] = reverse_lazy('Core:ColorUpdate', kwargs={'pk': self.object.id})
        return context
    
    def get_success_url(self):
        messages.success(self.request,  "تم تعديل اللون " + str(self.object) + " بنجاح ", extra_tags="success")
        if self.request.POST.get('url'):
            return self.request.POST.get('url')
        else:
            return self.success_url
    

class ColorDelete(LoginRequiredMixin, UpdateView):
    login_url = '/auth/login/'
    model = Color
    form_class = ColorForm
    template_name = 'forms/form_template.html'
    
 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'حذف اللون : ' + str(self.object.color_name)
        context['message'] = 'super_delete'
        context['action_url'] = reverse_lazy('Core:ColorDelete', kwargs={'pk': self.object.id})
        return context

    def form_valid(self, form):
        messages.success(self.request, " تم حذف اللون " + str(self.object) + " نهائيا بنجاح ", extra_tags="success")
        my_form = Color.objects.get(id=self.kwargs['pk'])
        my_form.delete()
        return redirect('Core:ColorList')
    
        
class SystemInfoCreate(LoginRequiredMixin, CreateView):
    login_url = '/auth/login/'
    model = SystemInformation
    template_name = 'forms/form_template.html'
    form_class = SystemInfoForm
    success_url = reverse_lazy('Core:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'بيانات النظام'
        context['message'] = 'info'
        context['action_url'] = reverse_lazy('Core:SystemInfoCreate')
        return context
    
        # return reverse('Core:index')
        
    def form_valid(self, form):
        form.save()
        obj = form.save(commit=False)
        info = SystemInformation.objects.get(id=obj.id)

        logo = info.logo
        if logo:
            # Read the binary data of the image file
            image_data = logo.read()
            # Open the image using PIL
            img = Image.open(BytesIO(image_data))
            # Check if the image format is not PNG
            if img.format != 'PNG':
                # Convert the image to PNG
                img = img.convert('RGBA')
                png_data = BytesIO()
                img.save(png_data, format='PNG')
                png_file = SimpleUploadedFile("logo.png", png_data.getvalue(), content_type="image/png")
                # Save the converted PNG image back to the model
                info.logo = png_file
                info.save()

        return redirect(self.get_success_url())
    
    
class SystemInfoUpdate(LoginRequiredMixin, UpdateView):
    login_url = '/auth/login/'
    model = SystemInformation
    template_name = 'forms/form_template.html'
    form_class = SystemInfoForm
    success_url = reverse_lazy('Core:index')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'تعديل بيانات النظام'
        context['message'] = 'info'
        context['info_obj'] = self.object
        context['action_url'] = reverse_lazy('Core:SystemInfoUpdate',kwargs={'pk': self.object.id})
        return context
    
    def get_success_url(self):
        messages.success(self.request, " تم تعديل بيانات النظام بنجاح", extra_tags="success")

        if self.request.POST.get('url'):
            return self.request.POST.get('url')
        else:
            return self.success_url
        # return reverse('Core:index')

    def form_valid(self, form):
        form.save()
        obj = form.save(commit=False)
        info = SystemInformation.objects.get(id=obj.id)

        logo = info.logo
        if logo:
            # Read the binary data of the image file
            image_data = logo.read()
            # Open the image using PIL
            img = Image.open(BytesIO(image_data))
            # Check if the image format is not PNG
            if img.format != 'PNG':
                # Convert the image to PNG
                img = img.convert('RGBA')
                png_data = BytesIO()
                img.save(png_data, format='PNG')
                png_file = SimpleUploadedFile("logo.png", png_data.getvalue(), content_type="image/png")
                # Save the converted PNG image back to the model
                info.logo = png_file
                info.save()

        return redirect(self.get_success_url())




