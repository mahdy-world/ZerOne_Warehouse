from django.urls import path 
from . import views

app_name = 'Core'
urlpatterns = [
    path('', views.Index, name='index'),
    path('systemInfoCreate/', views.SystemInfoCreate.as_view(), name='SystemInfoCreate'),
    path('ColorCreate/', views.ColorCreate.as_view(), name='ColorCreate'),
    path('ColorUpdate/<int:pk>/', views.ColorUpdate.as_view(), name='ColorUpdate'),
    path('ColorDelete/<int:pk>/', views.ColorDelete.as_view(), name='ColorDelete'),
    path('ColorList/', views.ColorList.as_view(), name='ColorList'),
    path('systemInfoUpdate/<int:pk>/', views.SystemInfoUpdate.as_view(), name='SystemInfoUpdate'),
]
