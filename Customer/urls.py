from django.urls import path 
from . import views

app_name = 'Customer'
urlpatterns = [
    path('CustomerCreate/', views.CustomerCreate.as_view(), name='CustomerCreate'),
    path('CustomerUpdate/<int:pk>/', views.CustomerUpdate.as_view(), name='CustomerUpdate'),
    path('CustomerDelete/<int:pk>/', views.CustomerSuperDelete.as_view(), name='CustomerSuperDelete'),
    path('CustomerList/', views.CustomerList.as_view(), name='CustomerList'),
    # path('systemInfoUpdate/<int:pk>/', views.SystemInfoUpdate.as_view(), name='SystemInfoUpdate'),
]
